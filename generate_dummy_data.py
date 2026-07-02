from fpdf import FPDF
import os

# data folder banao agar nahi hai
os.makedirs("data", exist_ok=True)

# 100 PDFs banengi
for i in range(100):
    pdf = FPDF()

    # Har PDF mein 100 pages
    for page in range(100):
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        text = f"""
        Report Number: {i}
        Page Number: {page + 1}

        Artificial Intelligence (AI) is transforming industries worldwide.
        Machine Learning is a subset of AI that enables systems to learn from data.
        Deep Learning uses neural networks for complex pattern recognition.
        Natural Language Processing helps computers understand human language.
        Retrieval-Augmented Generation (RAG) combines vector search with LLMs.
        FAISS is commonly used for vector storage and similarity search.
        Ollama allows running local LLMs without internet access.
        This is dummy data generated for a RAG project containing 10,000 pages.
        """

        pdf.multi_cell(0, 10, text)

    pdf.output(f"data/report{i}.pdf")

print("100 PDFs created successfully!")
print("Total pages created: 10000")