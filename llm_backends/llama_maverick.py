# llama_maverick.py

import requests
from rag_config import NVIDIA_API_KEY, NVIDIA_API_URL

def query_llama(prompt):
    headers = {
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "meta/llama3-70b-instruct",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3
    }

    response = requests.post(NVIDIA_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"LLaMA API Error: {response.status_code} - {response.text}")
