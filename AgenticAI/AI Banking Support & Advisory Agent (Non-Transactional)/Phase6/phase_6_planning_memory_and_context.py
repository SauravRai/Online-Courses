import os
import re
import json
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
    filename="banking_agent_phase6_logs.txt",
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

ALLOWED_TOOLS = [
    "emi",
    "eligibility"
]

MEMORY_FILE = "memory.json"

conversation_memory = {
    "loan_amount": None,
    "loan_tenure": None,
    "monthly_income": None
}

# =====================================================
# Memory Functions
# =====================================================

def load_memory():
    global conversation_memory

    try:
        with open(MEMORY_FILE, "r") as f:
            conversation_memory = json.load(f)
    except:
        pass


def save_memory():
    with open(MEMORY_FILE, "w") as f:
        json.dump(conversation_memory, f, indent=4)


def reset_memory():
    global conversation_memory

    conversation_memory = {
        "loan_amount": None,
        "loan_tenure": None,
        "monthly_income": None
    }

    save_memory()

    return "Conversation memory has been reset."


def update_memory(user_input):

    text = user_input.lower()

    amount_match = re.search(r"(\d+)\s*lakh", text)

    if amount_match:
        conversation_memory["loan_amount"] = (
            int(amount_match.group(1)) * 100000
        )

    tenure_match = re.search(r"(\d+)\s*years?", text)

    if tenure_match:
        conversation_memory["loan_tenure"] = (
            int(tenure_match.group(1)) * 12
        )

    income_match = re.search(
        r"income.*?(\d+)",
        text
    )

    if income_match:
        conversation_memory["monthly_income"] = int(
            income_match.group(1)
        )

    save_memory()

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
# Embeddings
# =====================================================

def get_embedding(text):

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding

# =====================================================
# Documents
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
# Vector Store
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

    print(f"Loaded {len(docs)} banking documents")

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
# Tool 1 - EMI
# =====================================================

def calculate_emi(
        principal,
        annual_rate,
        tenure_months):

    if principal <= 0:
        return "Invalid loan amount."

    monthly_rate = annual_rate / (12 * 100)

    emi = (
        principal
        * monthly_rate
        * ((1 + monthly_rate) ** tenure_months)
    ) / (
        ((1 + monthly_rate) ** tenure_months) - 1
    )

    return f"Estimated EMI: ₹{round(emi, 2)}"

# =====================================================
# Tool 2 - Eligibility
# =====================================================

def check_eligibility(
        monthly_income,
        existing_emi):

    max_allowed = monthly_income * 0.4

    if existing_emi < max_allowed:
        return "Potentially Eligible"

    return "Requires Manual Review"

# =====================================================
# Planning
# =====================================================

def loan_planner():

    if conversation_memory["loan_amount"] is None:
        return (
            "What loan amount would "
            "you like to borrow?"
        )

    if conversation_memory["loan_tenure"] is None:
        return (
            "What loan tenure "
            "would you prefer?"
        )

    return (
        "I have enough information "
        "to estimate your EMI. "
        "Type 'calculate emi'."
    )

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
        return "Tool usage not permitted."

    if tool_name == "emi":

        if conversation_memory["loan_amount"] is None:
            return (
                "I need the loan amount "
                "before calculating EMI."
            )

        if conversation_memory["loan_tenure"] is None:
            return (
                "I need the loan tenure "
                "before calculating EMI."
            )

        return calculate_emi(
            principal=conversation_memory["loan_amount"],
            annual_rate=8.5,
            tenure_months=conversation_memory["loan_tenure"]
        )

    if tool_name == "eligibility":

        income = (
            conversation_memory["monthly_income"]
            if conversation_memory["monthly_income"]
            else 100000
        )

        return check_eligibility(
            monthly_income=income,
            existing_emi=20000
        )

# =====================================================
# RAG
# =====================================================

def rag_response(query):

    docs = retrieve_documents(query)

    if not docs:
        return "No relevant information was found."

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
# Agent Logic
# =====================================================

def agent_response(query):

    update_memory(query)

    query_lower = query.lower()

    if query_lower in [
        "reset memory",
        "clear memory"
    ]:
        return reset_memory()

    if "transfer" in query_lower:
        return (
            "I cannot perform banking "
            "transactions or money transfers."
        )

    if (
        "home loan" in query_lower
        or "loan application" in query_lower
    ):
        return loan_planner()

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

    return rag_response(query)

# =====================================================
# Failed Tool Demo
# =====================================================

def failed_tool_demo():

    print("\n" + "=" * 60)
    print("FAILED TOOL CALL DEMONSTRATION")
    print("=" * 60)

    print(
        "\nQuery: What documents are required "
        "for a home loan?"
    )

    print("\nIncorrect Tool Selected: EMI Calculator")

    print(
        calculate_emi(
            principal=500000,
            annual_rate=8.5,
            tenure_months=60
        )
    )

    print(
        "\nExplanation: Query required "
        "retrieval but EMI tool was used."
    )

# =====================================================
# Main
# =====================================================

def main():

    load_memory()
    build_vector_store()

    print("=" * 70)
    print("Banking AI Support & Advisory Agent")
    print("Phase 6 - Planning, Memory & Context")
    print("=" * 70)

    failed_tool_demo()

    while True:

        user_input = input("\nCustomer: ")

        if user_input.lower() == "exit":

            print("Agent: Session Ended")
            break

        try:

            response = agent_response(
                user_input
            )

            safe_input = mask_pii(
                user_input
            )

            logging.info(
                f"""
Customer={safe_input}

Memory={conversation_memory}

Agent={response}

-----------------------------------
"""
            )

            print(f"\nAgent:\n{response}")

        except Exception as e:

            print(f"\nAgent Error: {e}")
            logging.error(str(e))

if __name__ == "__main__":
    main()
