# Agentic RAG System

This is a modular, multi-agent Retrieval-Augmented Generation (RAG) system that uses a controller and reasoning agent to answer user queries based on uploaded documents. The system uses FAISS for vector storage, sentence-transformers for embeddings, and supports LLM APIs like NVIDIA and Groq.

---

## Features

- Multi-agent architecture (Controller + Reasoning Agent)
- Document chunking & vector embedding
- FAISS-based semantic search
- Streamlit-based user interface
- Secure API key handling

---

## Project Structure

AI AGENT/
├── agents/
│   ├── agent.py
│   └── controller.py
├── retriever/
│   ├── embedder.py
│   ├── retriever.py
│   └── vector_store.py
├── utils/
│   └── file_utils.py
├── ui/
│   └── app.py
├── data/
│   ├── documents/
│   └── embeddings/
├── rag_config.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md


## Install dependencies

```pip install -r requirements.txt```

## Add your API keys in rag_config.py

```NVIDIA_API_KEY = Insert your API key```
```NVIDIA_API_URL = Insert your API URL```
```GROK_API_KEY = Insert your Groq API key```

## Add documents

Place .txt files inside the data/documents/ directory. These will be chunked and indexed automatically.

## Run the Streamlit app

```streamlit run ui/app.py```

