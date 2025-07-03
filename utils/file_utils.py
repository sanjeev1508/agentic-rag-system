import os

def ensure_dirs():
    os.makedirs("data/documents", exist_ok=True)
    os.makedirs("data/embeddings", exist_ok=True)
    os.makedirs("logs", exist_ok=True)

def save_text_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def load_text_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
