from retriever.embedder import embed_text
from retriever.vector_store import vector_store
from rag_config import CHUNK_SIZE, CHUNK_OVERLAP

import os

# You should load real docs here, we use dummy data

def load_documents():
    files = os.listdir("data/documents")
    documents = []
    for fname in files:
        with open(os.path.join("data/documents", fname), encoding="utf-8") as f:
            documents.append(f.read())
    return documents

def chunk_text(text):
    chunks = []
    for i in range(0, len(text), CHUNK_SIZE - CHUNK_OVERLAP):
        chunk = text[i:i + CHUNK_SIZE]
        if len(chunk) > 50:
            chunks.append(chunk)
    return chunks

def prepare_index():
    docs = load_documents()
    all_chunks = []
    for doc in docs:
        all_chunks.extend(chunk_text(doc))
    embeddings = [embed_text(c) for c in all_chunks]
    vector_store.build_index(embeddings, all_chunks)

if not vector_store.load_index():
    prepare_index()

def retrieve_documents(query):
    query_vec = embed_text(query)
    return vector_store.query(query_vec, top_k=3)
