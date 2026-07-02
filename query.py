from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_community.vectorstores import FAISS

DB_PATH = "vectordb"

# Load embeddings
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# Load vector DB
db = FAISS.load_local(
    DB_PATH,
    embeddings,
    allow_dangerous_deserialization=True
)

# Load LLM
llm = OllamaLLM(
    model="llama3.2"
)

print("RAG System Ready!")
print("Type 'exit' to quit.\n")

while True:
    question = input("Question: ")

    if question.lower() == "exit":
        break

    docs = db.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    print("\nAnswer:")
    print(response)
    print("\n" + "=" * 60 + "\n")