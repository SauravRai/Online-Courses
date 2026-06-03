#Dependencies which needs to be installed 
#pip install openai chromadb

import os
import re
import logging
import pysqlite3
import sys
sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")
import chromadb


from openai import OpenAI

# =====================================================
# OpenAI Client
# =====================================================

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)

# =====================================================
# Logging
# =====================================================

logging.basicConfig(
    filename="banking_agent_rag_logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# =====================================================
# ChromaDB
# =====================================================

chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection(
    name="banking_docs"
)

# =====================================================
# PII Masking
# =====================================================

def mask_pii(text):

    text = re.sub(
        r"\b\d{8,}\b",
        "[ACCOUNT_MASKED]",
        text
    )

    text = re.sub(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        "[EMAIL_MASKED]",
        text
    )

    return text

# =====================================================
# Embedding Function
# =====================================================

def get_embedding(text):

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding

# =====================================================
# Load Knowledge Base
# =====================================================

def load_documents():

    with open(
        "bank_policies.txt",
        "r",
        encoding="utf-8"
    ) as f:

        content = f.read()

    chunks = [
        chunk.strip()
        for chunk in content.split("\n\n")
        if chunk.strip()
    ]

    return chunks

# =====================================================
# Build Vector Store
# =====================================================

def build_vector_store():

    docs = load_documents()

    existing = collection.count()

    if existing > 0:
        return

    for idx, doc in enumerate(docs):

        embedding = get_embedding(doc)

        collection.add(
            ids=[str(idx)],
            documents=[doc],
            embeddings=[embedding]
        )

    print(
        f"Loaded {len(docs)} documents into ChromaDB"
    )

# =====================================================
# Semantic Search
# =====================================================

def retrieve_documents(query, top_k=3):

    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    docs = results["documents"][0]

    return docs

# =====================================================
# LLM WITHOUT Retrieval (Phase 3)
# =====================================================

def llm_only_response(user_query):

    prompt = f"""
You are a Banking Support Assistant.

Answer the user's question.

Question:
{user_query}
"""

    response = client.responses.create(
        model="gpt-5.5",
        input=prompt
    )

    return response.output_text

# =====================================================
# LLM WITH Retrieval (Phase 4)
# =====================================================

def rag_response(user_query):

    retrieved_docs = retrieve_documents(
        user_query
    )

    if not retrieved_docs:

        return (
            "I could not find relevant information "
            "in the banking knowledge base."
        )

    context = "\n\n".join(
        retrieved_docs
    )

    prompt = f"""
You are a Banking Support Assistant.

Use ONLY the provided context.

If the answer is not present in the context,
say that the information is unavailable.

Context:
{context}

Question:
{user_query}
"""

    response = client.responses.create(
        model="gpt-5.5",
        input=prompt
    )

    return response.output_text

# =====================================================
# Main Application
# =====================================================

def main():

    build_vector_store()

    print("=" * 70)
    print("Banking Support Agent - Phase 4 (RAG)")
    print("=" * 70)
    print("Type 'exit' to quit")

    while True:

        user_input = input(
            "\nCustomer: "
        )

        if user_input.lower() == "exit":
            break

        try:

            safe_input = mask_pii(
                user_input
            )

            # -------------------------
            # Without Retrieval
            # -------------------------

            llm_response = (
                llm_only_response(
                    user_input
                )
            )

            # -------------------------
            # With Retrieval
            # -------------------------

            rag_answer = (
                rag_response(
                    user_input
                )
            )

            # -------------------------
            # Logging
            # -------------------------

            logging.info(
                f"""
Customer={safe_input}

WITHOUT RETRIEVAL:
{llm_response}

WITH RETRIEVAL:
{rag_answer}

---------------------------------------------------
"""
            )

            # -------------------------
            # Display Comparison
            # -------------------------

            print("\n" + "=" * 70)
            print("WITHOUT RETRIEVAL (Phase 3)")
            print("=" * 70)

            print(llm_response)

            print("\n" + "=" * 70)
            print("WITH RETRIEVAL (Phase 4)")
            print("=" * 70)

            print(rag_answer)

        except Exception as e:

            print(
                f"\nAgent Error: {e}"
            )

            logging.error(
                f"Error: {e}"
            )

if __name__ == "__main__":
    main()
