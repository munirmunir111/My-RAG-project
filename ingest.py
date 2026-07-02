import os
import gc

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

DATA_PATH = "data"
DB_PATH = "vectordb"

# Embedding model
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# Chunk settings
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

db = None

# Process PDFs one by one
for filename in os.listdir(DATA_PATH):

    if not filename.lower().endswith(".pdf"):
        continue

    pdf_path = os.path.join(DATA_PATH, filename)

    print(f"\n{'=' * 50}")
    print(f"Processing: {filename}")
    print(f"{'=' * 50}")

    try:
        # Load PDF
        loader = PyPDFLoader(pdf_path)
        pages = loader.load()

        print(f"Pages loaded: {len(pages)}")

        # Split into chunks
        chunks = text_splitter.split_documents(pages)

        print(f"Chunks created: {len(chunks)}")

        # Create DB for first PDF
        if db is None:
            if os.path.exists(DB_PATH) and os.listdir(DB_PATH):
                print("Loading existing vector database...")
                db = FAISS.load_local(
                    DB_PATH,
                    embeddings,
                    allow_dangerous_deserialization=True
                )
                db.add_documents(chunks)
            else:
                print("Creating new vector database...")
                db = FAISS.from_documents(
                    chunks,
                    embeddings
                )
        else:
            print("Adding chunks to existing database...")
            db.add_documents(chunks)

        # Save after every PDF
        db.save_local(DB_PATH)

        print(f"Saved successfully: {filename}")

        # Free RAM
        del pages
        del chunks
        gc.collect()

    except Exception as e:
        print(f"Error processing {filename}")
        print(e)

print("\n======================================")
print("Vector Database Created Successfully!")
print("Database location: vectordb/")
print("======================================")