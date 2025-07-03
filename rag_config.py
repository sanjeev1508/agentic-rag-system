# rag_config.py

# NVIDIA LLaMa 4 via Maverick
NVIDIA_API_KEY = "Instert your API key"
NVIDIA_API_URL = "Instert your API URL"

# Grok API
GROK_API_KEY = "Instert your API key"

# Vector DB Config
VECTOR_DB_PATH = "data/embeddings/faiss_index.pkl"

# Embedding model (optional fallback)
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Chunking configs
CHUNK_SIZE = 512
CHUNK_OVERLAP = 64
