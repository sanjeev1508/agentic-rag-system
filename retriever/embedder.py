# retriever/embedder.py

from sentence_transformers import SentenceTransformer
from rag_config import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)

def embed_text(text):
    return model.encode(text, show_progress_bar=False)
