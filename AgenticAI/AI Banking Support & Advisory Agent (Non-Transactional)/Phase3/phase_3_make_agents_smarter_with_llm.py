import os
import re
import logging
from openai import OpenAI

# =====================================================
# OpenAI Client
# =====================================================

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)

# =====================================================
# Configuration
# =====================================================

# True  -> Compare V1, V2, V3
# False -> Use selected default prompt only
COMPARE_MODE = True

# Selected default prompt after evaluation
DEFAULT_PROMPT_NAME = "V3"

# =====================================================
# Logging
# =====================================================

logging.basicConfig(
    filename="banking_agent_logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# =====================================================
# PII Masking
# =====================================================

def mask_pii(text):
    """
    Remove potentially sensitive information before logging.
    """

    # Account numbers (8+ digits)
    text = re.sub(
        r"\b\d{8,}\b",
        "[ACCOUNT_MASKED]",
        text
    )

    # Email addresses
    text = re.sub(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        "[EMAIL_MASKED]",
        text
    )

    return text


# =====================================================
# Prompt Version 1
# =====================================================

PROMPT_V1 = """
You are a banking support assistant.

Answer the user's banking question clearly.

User Question:
{query}
"""

# =====================================================
# Prompt Version 2
# =====================================================

PROMPT_V2 = """
You are a Banking Support Assistant.

Rules:
- Answer informational banking questions.
- Do not provide legal advice.
- Do not provide investment advice.
- Do not perform banking transactions.
- Escalate fraud-related complaints.
- If unsure, say you are unsure.

User Question:
{query}
"""

# =====================================================
# Prompt Version 3 (Recommended)
# =====================================================

PROMPT_V3 = """
You are a Banking Support Assistant.

Follow these rules:

1. Answer only informational banking questions.
2. Never invent customer information.
3. Never claim access to customer accounts.
4. Refuse requests involving money transfers.
5. Escalate fraud complaints.
6. If uncertain, explicitly state uncertainty.

Response Format:

Category:
Answer:
Escalation Required:

User Question:
{query}
"""

# Selected prompt after evaluation
DEFAULT_PROMPT = PROMPT_V3

# =====================================================
# LLM Response Generator
# =====================================================

def generate_response(user_query, prompt_template):

    prompt = prompt_template.format(
        query=user_query
    )

    response = client.responses.create(
        model="gpt-5.5",   # replace with model available in your environment
        input=prompt
    )

    return response.output_text


# =====================================================
# Compare Prompt Variants
# =====================================================

def compare_prompts(user_query):

    responses = {
        "V1": generate_response(
            user_query,
            PROMPT_V1
        ),
        "V2": generate_response(
            user_query,
            PROMPT_V2
        ),
        "V3": generate_response(
            user_query,
            PROMPT_V3
        )
    }

    return responses


# =====================================================
# Main Agent
# =====================================================

def main():

    print("=" * 60)
    print("Banking Support Agent (LLM Version)")
    print("=" * 60)

    if COMPARE_MODE:
        print("Mode: Prompt Comparison")
    else:
        print(
            f"Mode: Default Prompt ({DEFAULT_PROMPT_NAME})"
        )

    print("Type 'exit' to quit")
    print("=" * 60)

    while True:

        user_input = input("\nCustomer: ")

        if user_input.lower() == "exit":
            print("Agent: Session Ended")
            break

        try:

            safe_input = mask_pii(user_input)

            # ==================================
            # Prompt Comparison Mode
            # ==================================
            if COMPARE_MODE:

                responses = compare_prompts(
                    user_input
                )

                logging.info(
                    f"""
Customer={safe_input}

PROMPT_V1:
{responses['V1']}

PROMPT_V2:
{responses['V2']}

PROMPT_V3:
{responses['V3']}

----------------------------------------------------
"""
                )

                print("\n" + "=" * 60)
                print("PROMPT V1 RESPONSE")
                print("=" * 60)
                print(responses["V1"])

                print("\n" + "=" * 60)
                print("PROMPT V2 RESPONSE")
                print("=" * 60)
                print(responses["V2"])

                print("\n" + "=" * 60)
                print("PROMPT V3 RESPONSE")
                print("=" * 60)
                print(responses["V3"])

            # ==================================
            # Production Mode
            # ==================================
            else:

                response = generate_response(
                    user_input,
                    DEFAULT_PROMPT
                )

                logging.info(
                    f"""
Customer={safe_input}

Prompt={DEFAULT_PROMPT_NAME}

Response:
{response}

----------------------------------------------------
"""
                )

                print(
                    f"\nUsing Prompt Strategy: {DEFAULT_PROMPT_NAME}"
                )
                print("-" * 60)
                print(response)

        except Exception as e:

            print(
                f"\nAgent Error: {e}"
            )

            logging.error(
                f"Error processing query: {e}"
            )


if __name__ == "__main__":
    main()