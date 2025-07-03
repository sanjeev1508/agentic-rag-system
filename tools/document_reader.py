import os
import fitz  # PyMuPDF

def read_pdf(path):
    text = ""
    with fitz.open(path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def load_documents_from_folder(folder_path="data/documents"):
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            full_path = os.path.join(folder_path, filename)
            documents.append(read_pdf(full_path))
        elif filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), encoding="utf-8") as f:
                documents.append(f.read())
    return documents