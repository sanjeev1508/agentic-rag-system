from retriever.retriever import retrieve_documents
from llm_backends.llama_maverick import query_llama
from config import *
import streamlit as st

st.set_page_config(page_title="Agentic RAG", layout="wide")
st.title("Agentic RAG System")

query = st.text_input("Enter a query:")

if query:
    with st.spinner("Retrieving knowlegde"):
        retrieved_documents = retrieve_documents(query)
        context = "\n\n".join([doc['content'] for doc in retrieved_documents])

    with st.spinner("Thinking"):
        final_prompt = f""" Use the following context to answer the question.\n\nContext:\n{context}\n\nQuestion:\n{query}"""
        answer = query_llama(final_prompt)
    
    st.subheader("Answer:")

    st.write(answer)

    st.subheader("Retrieved Docs:")
    for i, doc in enumerate(retrieved_documents):
        st.markdown(f"**Doc {i+1}:**")
        st.code(doc['context'][:1000])