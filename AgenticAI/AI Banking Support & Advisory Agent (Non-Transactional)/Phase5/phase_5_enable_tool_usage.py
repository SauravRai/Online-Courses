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
    filename="banking_agent_phase5_logs.txt",
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
# Configuration
# =====================================================

MAX_TOOL_CALLS = 3

ALLOWED_TOOLS = [
    "emi",
    "eligibility"
]

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
# Load Banking Documents
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

    if collection.count() > 0:
        return

    docs = load_documents()

    for idx, doc in enumerate(docs):

        embedding = get_embedding(doc)

        collection.add(
            ids=[str(idx)],
            documents=[doc],
            embeddings=[embedding]
        )

    print(
        f"Loaded {len(docs)} banking documents"
    )


# =====================================================
# Retrieval
# =====================================================

def retrieve_documents(query):

    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    return results["documents"][0]


# =====================================================
# Tool 1 - EMI Calculator
# =====================================================

def calculate_emi(
        principal,
        annual_rate,
        tenure_months):

    if principal <= 0:
        return "Invalid loan amount."

    monthly_rate = (
        annual_rate / (12 * 100)
    )

    emi = (
        principal
        * monthly_rate
        * ((1 + monthly_rate) ** tenure_months)
    ) / (
        ((1 + monthly_rate) ** tenure_months) - 1
    )

    return (
        f"Estimated EMI: ₹{round(emi, 2)}"
    )


# =====================================================
# Tool 2 - Eligibility Checker
# =====================================================

def check_eligibility(
        monthly_income,
        existing_emi):

    max_allowed = (
        monthly_income * 0.4
    )

    if existing_emi < max_allowed:
        return "Potentially Eligible"

    return "Requires Manual Review"


# =====================================================
# Tool Routing
# =====================================================

def select_tool(query):

    query = query.lower()

    if "emi" in query:
        return "emi"

    if "eligible" in query:
        return "eligibility"

    return None


# =====================================================
# Execute Tool
# =====================================================

def execute_tool(
        tool_name,
        query):

    if tool_name not in ALLOWED_TOOLS:

        return (
            "Tool usage not permitted."
        )

    if tool_name == "emi":

        # Demo values
        return calculate_emi(
            principal=500000,
            annual_rate=8.5,
            tenure_months=60
        )

    if tool_name == "eligibility":

        # Demo values
        return check_eligibility(
            monthly_income=100000,
            existing_emi=20000
        )

    return None


# =====================================================
# LLM + RAG Response
# =====================================================

def rag_response(query):

    docs = retrieve_documents(query)

    if not docs:

        return (
            "No relevant information "
            "was found."
        )

    context = "\n\n".join(docs)

    prompt = f"""
You are a Banking Support Assistant.

Use ONLY the provided context.

Context:
{context}

Question:
{query}
"""

    response = client.responses.create(
        model="gpt-5.5",
        input=prompt
    )

    return response.output_text


# =====================================================
# Main Agent Logic
# =====================================================

def agent_response(query):

    query_lower = query.lower()

    # --------------------------
    # Guardrail 1
    # --------------------------

    if "transfer" in query_lower:

        return (
            "I cannot perform banking "
            "transactions or money transfers."
        )

    # --------------------------
    # Tool Routing
    # --------------------------

    tool_name = select_tool(query)

    if tool_name:

        result = execute_tool(
            tool_name,
            query
        )

        return (
            f"[TOOL USED: {tool_name}]\n"
            f"{result}"
        )

    # --------------------------
    # Retrieval
    # --------------------------

    return rag_response(query)


# =====================================================
# Demonstration of Failed Tool Call
# =====================================================

def failed_tool_demo():

    print("\n")
    print("=" * 60)
    print("FAILED TOOL CALL DEMONSTRATION")
    print("=" * 60)

    bad_query = (
        "What documents are required "
        "for a home loan?"
    )

    print(
        f"\nQuery: {bad_query}"
    )

    wrong_result = calculate_emi(
        principal=500000,
        annual_rate=8.5,
        tenure_months=60
    )

    print(
        "\nIncorrect Tool Selected:"
    )

    print(
        "EMI Calculator"
    )

    print(
        f"Result: {wrong_result}"
    )

    print(
        "\nExplanation:"
    )

    print(
        "The query required policy retrieval "
        "but the EMI tool was selected."
    )


# =====================================================
# Main
# =====================================================

def main():

    build_vector_store()

    print("=" * 70)
    print("Banking AI Support & Advisory Agent")
    print("Phase 5 - Tool Enabled Agent")
    print("=" * 70)

    failed_tool_demo()

    while True:

        user_input = input(
            "\nCustomer: "
        )

        if user_input.lower() == "exit":

            print(
                "Agent: Session Ended"
            )

            break

        try:

            safe_input = mask_pii(
                user_input
            )

            response = agent_response(
                user_input
            )

            logging.info(
                f"""
Customer={safe_input}

Agent={response}

-----------------------------------------
"""
            )

            print(
                f"\nAgent:\n{response}"
            )

        except Exception as e:

            print(
                f"\nAgent Error: {e}"
            )

            logging.error(
                f"Error={e}"
            )


if __name__ == "__main__":
    main()