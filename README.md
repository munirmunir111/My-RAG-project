# 📚 Offline RAG (Retrieval-Augmented Generation)

This project is an Offline RAG (Retrieval-Augmented Generation)system using a dummy dataset of 10,000 text documents.The system
retrieves relevent information from local documents relevent information from local documents using FAISS and generates answers with a local LLM through Ollama.

## Project Objective :
The objective of this project is to build an offline Question Answering system that can retrieve relevant information from local documents and generation accurate answers using RAG.
##  Features

- Offline Question Answering 
- No Internet Required
- No API Key 
- No API Cost
- Local LLM using Ollama
- FAISS Vector Database
- Fast Document Retrieval
- Secure Local storage

## 🛠 Technologies Used

- Python
- LangChain
- Ollama
- FAISS
- Nomic Embed Text

## 📂 Project Structure

```
MY-RAG-PROJECT/
│
├── data/
├── vectordb/
├── generate_dummy_data.py
├── ingest.py
├── query.py
├── requirements.txt
└── README.md
```
## Dataset
- Dummy Dataset
-10,000 Text Documents
-Used for indexing and Retrieval Testing
## 🔄 Project Workflow

1. Generate dummy data.
2. Run ingest.py to create embeddings.
3. Store embeddings in the FAISS vector database.
4. Run query.py.
 5. Ask a question.
6. Retrieve  relevant documents.
7. Generate the final answer using the local LLM.

## ▶️ How to Run

```
pip install -r requirements.txt
python generate_dummy_data.py
python ingest.py
python query.py
```

## Demo :

1. Run `python generate_dummy_data.py`
2. Run `python ingest.py`
3. Run `python query.py`
4. Enter a question.
5. The system retrieves relevant documents.
6. The local LLM generates the final answer.
