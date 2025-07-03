from retriever.retriever import retrieve_documents
from llm_backends.llama_maverick import query_llama

class AgentExecutor:
    def __init__(self):
        pass

    def run(self, query: str):
        # Step 1: Retrieve relevant context chunks
        relevant_chunks = retrieve_documents(query)
        context = "\n".join([str(chunk["content"]) for chunk in relevant_chunks])



        # Step 2: Format prompt for LLM
        prompt = f"""
You are a clinical assistant helping to analyze patient data.

Refer to the following context extracted from a patient's record and answer the user's query.

Context:
{context}

User Query:
{query}

Answer:"""

        # Step 3: Query the LLM (NVIDIA LLaMA 3/4)
        try:
            response = query_llama(prompt)
        except Exception as e:
            response = f"LLM query failed: {e}"

        return response
