import os
import re
import json
import time
import logging
import pysqlite3
import sys

from dotenv import load_dotenv

sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")

import chromadb
from openai import OpenAI

# =====================================================
# Load Environment Variables
# =====================================================

load_dotenv()

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
    filename="banking_agent_phase8_logs.txt",
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

FEEDBACK_FILE = "feedback.json"

conversation_memory = {
    "loan_amount": None,
    "loan_tenure": None,
    "monthly_income": None
}

feedback_data = {
    "helpful": 0,
    "not_helpful": 0
}

# =====================================================
# Memory Functions
# =====================================================

def load_memory():

    global conversation_memory

    try:

        with open(
            MEMORY_FILE,
            "r"
        ) as f:

            conversation_memory = json.load(f)

    except:

        pass


def save_memory():

    with open(
        MEMORY_FILE,
        "w"
    ) as f:

        json.dump(
            conversation_memory,
            f,
            indent=4
        )


def reset_memory():

    global conversation_memory

    conversation_memory = {
        "loan_amount": None,
        "loan_tenure": None,
        "monthly_income": None
    }

    save_memory()

    return (
        "Conversation memory has been reset."
    )


def update_memory(user_input):

    text = user_input.lower()

    amount_match = re.search(
        r"(\d+)\s*lakh",
        text
    )

    if amount_match:

        conversation_memory[
            "loan_amount"
        ] = int(
            amount_match.group(1)
        ) * 100000

    tenure_match = re.search(
        r"(\d+)\s*years?",
        text
    )

    if tenure_match:

        conversation_memory[
            "loan_tenure"
        ] = int(
            tenure_match.group(1)
        ) * 12

    income_match = re.search(
        r"income.*?(\d+)",
        text
    )

    if income_match:

        conversation_memory[
            "monthly_income"
        ] = int(
            income_match.group(1)
        )

    save_memory()

# =====================================================
# Feedback Functions
# =====================================================

def load_feedback():

    global feedback_data

    try:

        with open(
            FEEDBACK_FILE,
            "r"
        ) as f:

            feedback_data = json.load(f)

    except:

        feedback_data = {
            "helpful": 0,
            "not_helpful": 0
        }


def save_feedback():

    with open(
        FEEDBACK_FILE,
        "w"
    ) as f:

        json.dump(
            feedback_data,
            f,
            indent=4
        )


def record_feedback(feedback):

    if feedback == "helpful":

        feedback_data[
            "helpful"
        ] += 1

    elif feedback == "not helpful":

        feedback_data[
            "not_helpful"
        ] += 1

    save_feedback()


def get_response_style():

    negative_feedback = (
        feedback_data[
            "not_helpful"
        ]
    )

    if negative_feedback >= 3:

        return "DETAILED"

    return "NORMAL"

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

    try:

        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )

        return response.data[0].embedding

    except Exception as e:

        logging.error(
            f"Embedding Error: {e}"
        )

        return None

# =====================================================
# Load Documents
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

        if embedding is None:
            continue

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

    if query_embedding is None:

        return []

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    print(
        "[TRACE] Retrieval Used"
    )

    return results["documents"][0]

# =====================================================
# EMI Tool
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

    return (
        f"Estimated EMI: ₹{round(emi, 2)}"
    )

# =====================================================
# Eligibility Tool
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

    if (
        conversation_memory[
            "loan_amount"
        ] is None
    ):

        return (
            "What loan amount would "
            "you like to borrow?"
        )

    if (
        conversation_memory[
            "loan_tenure"
        ] is None
    ):

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

    print(
        f"[TRACE] Tool Selected: {tool_name}"
    )

    if tool_name not in ALLOWED_TOOLS:

        return (
            "Tool usage not permitted."
        )

    if tool_name == "emi":

        if (
            conversation_memory[
                "loan_amount"
            ] is None
        ):

            return (
                "I need the loan amount "
                "before calculating EMI."
            )

        if (
            conversation_memory[
                "loan_tenure"
            ] is None
        ):

            return (
                "I need the loan tenure "
                "before calculating EMI."
            )

        return calculate_emi(
            principal=
            conversation_memory[
                "loan_amount"
            ],
            annual_rate=8.5,
            tenure_months=
            conversation_memory[
                "loan_tenure"
            ]
        )

    if tool_name == "eligibility":

        income = (
            conversation_memory[
                "monthly_income"
            ]
            if conversation_memory[
                "monthly_income"
            ]
            else 100000
        )

        return check_eligibility(
            monthly_income=income,
            existing_emi=20000
        )

# =====================================================
# Adaptive RAG
# =====================================================

def rag_response(query):

    docs = retrieve_documents(query)

    if not docs:

        return (
            "No relevant information "
            "was found."
        )

    context = "\n\n".join(docs)

    response_style = get_response_style()

    # --------------------------------
    # NORMAL MODE
    # --------------------------------

    if response_style == "NORMAL":

        prompt = f"""
You are a Banking Support Assistant.

Provide a concise answer.

Use ONLY the provided context.

Context:
{context}

Question:
{query}
"""

    # --------------------------------
    # DETAILED MODE
    # --------------------------------

    else:

        prompt = f"""
You are a Banking Support Assistant.

Provide a detailed answer with:
- explanations
- bullet points
- additional clarification

Use ONLY the provided context.

Context:
{context}

Question:
{query}
"""

    try:

        response = client.responses.create(
            model="gpt-5.5",
            input=prompt
        )

        return response.output_text

    except Exception as e:

        logging.error(
            f"LLM Error: {e}"
        )

        return (
            "The AI service is temporarily unavailable. "
            "Please try again later."
        )

# =====================================================
# Agent Logic
# =====================================================

def agent_response(query):

    update_memory(query)

    query_lower = query.lower()

    # --------------------------------
    # Feedback Commands
    # --------------------------------

    if query_lower.startswith(
        "feedback "
    ):

        feedback = query_lower.replace(
            "feedback ",
            ""
        )

        record_feedback(
            feedback
        )

        return (
            "Thank you for your feedback. "
            "Future responses may adapt "
            "based on this feedback."
        )

    # --------------------------------
    # Reset Memory
    # --------------------------------

    if query_lower in [
        "reset memory",
        "clear memory"
    ]:

        return reset_memory()

    # --------------------------------
    # Guardrail
    # --------------------------------

    if "transfer" in query_lower:

        return (
            "I cannot perform banking "
            "transactions or money transfers."
        )

    # --------------------------------
    # Planning
    # --------------------------------

    if (
        "home loan" in query_lower
        or "loan application" in query_lower
    ):

        return loan_planner()

    # --------------------------------
    # Tool Routing
    # --------------------------------

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

    # --------------------------------
    # Retrieval
    # --------------------------------

    return rag_response(query)

# =====================================================
# Main
# =====================================================

def main():

    load_memory()

    load_feedback()

    build_vector_store()

    print("=" * 70)
    print("Banking AI Support & Advisory Agent")
    print("Phase 8 - Deployment Readiness")
    print("=" * 70)

    print(
        f"Current Response Style: "
        f"{get_response_style()}"
    )

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

            start_time = time.time()

            response = agent_response(
                user_input
            )

            end_time = time.time()

            latency = round(
                end_time - start_time,
                2
            )

            safe_input = mask_pii(
                user_input
            )

            logging.info(
                f"""
Customer={safe_input}

Memory={conversation_memory}

Feedback={feedback_data}

ResponseStyle={get_response_style()}

Latency={latency} seconds

Agent={response}

-----------------------------------
"""
            )

            print(
                f"\nAgent:\n{response}"
            )

            print(
                f"\n[TRACE] Latency: "
                f"{latency} seconds"
            )

        except Exception as e:

            print(
                "\nAgent: The system encountered "
                "an unexpected error. "
                "Please try again later."
            )

            logging.error(
                f"Runtime Error: {e}"
            )

if __name__ == "__main__":
    main()