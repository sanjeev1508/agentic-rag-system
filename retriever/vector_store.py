# retriever/vector_store.py

import faiss
import numpy as np
import os
import pickle
from rag_config import VECTOR_DB_PATH

class VectorStore:
    def __init__(self):
        self.index = None
        self.text_chunks = []

    def build_index(self, embeddings, texts):
        self.index = faiss.IndexFlatL2(len(embeddings[0]))
        self.index.add(np.array(embeddings).astype('float32'))
        self.text_chunks = texts
        with open(VECTOR_DB_PATH, "wb") as f:
            pickle.dump((self.index, self.text_chunks), f)

    def load_index(self):
        if os.path.exists(VECTOR_DB_PATH):
            with open(VECTOR_DB_PATH, "rb") as f:
                self.index, self.text_chunks = pickle.load(f)
            return True
        return False

    def query(self, query_embedding, top_k=3):
        if not self.index:
            return []
        D, I = self.index.search(np.array([query_embedding]).astype('float32'), top_k)
        return [
            {"content": self.text_chunks[i], "score": float(D[0][idx])}
            for idx, i in enumerate(I[0])
        ]

# ✅ This must be present at the bottom
vector_store = VectorStore()
