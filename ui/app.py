import sys
import os

# Ensure base path is added for proper local imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from utils.file_utils import ensure_dirs
from agents.controller import ControllerAgent

# Page config
st.set_page_config(page_title="Agentic RAG UI", layout="wide")
st.title("Agentic Retrieval-Augmented Generation")

# Create required directories
ensure_dirs()

# Initialize agent
controller = ControllerAgent()

# Input query
query = st.text_input("Ask a question:")

# On submit
if query:
    with st.spinner("Running agentic reasoning..."):
        result = controller.run(query)
    st.subheader("Final Answer")
    st.write(result)
