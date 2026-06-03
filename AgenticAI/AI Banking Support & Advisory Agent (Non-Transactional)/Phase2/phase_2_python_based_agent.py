import logging
import re

# Configure logging
logging.basicConfig(
    filename="banking_agent_logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# ---------------------------------
# PII Masking
# ---------------------------------
def mask_pii(text):
    """
    Mask sensitive information before logging.
    """

    # Mask long numbers (account numbers)
    text = re.sub(r"\b\d{8,}\b", "[ACCOUNT_MASKED]", text)

    # Mask email addresses
    text = re.sub(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        "[EMAIL_MASKED]",
        text
    )

    return text


# ---------------------------------
# Response Generator
# ---------------------------------
def generate_response(user_input):
    """
    Generate rule-based banking responses.
    """

    query = user_input.lower()

    # Home Loan Documents
    if "home loan" in query and "document" in query:
        return (
            "Typical home loan documents include "
            "identity proof, address proof, income proof, "
            "bank statements, and property documents."
        )

    # Travel Reward Credit Card
    elif "travel reward" in query or "travel card" in query:
        return (
            "Travel reward credit cards generally offer "
            "air miles, reward points, and airport lounge access."
        )

    # EMI Query
    elif "emi" in query:
        return (
            "EMI support is available, but this baseline version "
            "cannot perform EMI calculations yet."
        )

    # Fraud or Double Charge
    elif "charged twice" in query or "fraud" in query:
        return (
            "This issue requires human review. "
            "Please contact customer support immediately. "
            "Escalation Recommended."
        )

    # Money Transfer Request
    elif "transfer" in query:
        return (
            "I cannot perform banking transactions. "
            "Please use official banking channels."
        )

    # Balance Inquiry
    elif "balance" in query:
        return (
            "I cannot access customer-specific account information."
        )

    # Default Response
    else:
        return (
            "I am unable to answer that request. "
            "Please contact customer support."
        )


# ---------------------------------
# Main Agent Loop
# ---------------------------------
def main():

    print("=" * 50)
    print("Banking Support Agent")
    print("Type 'exit' to quit")
    print("=" * 50)

    while True:

        user_input = input("\nCustomer: ")

        if user_input.lower() == "exit":
            print("Agent: Session Ended")
            break

        response = generate_response(user_input)

        # Mask sensitive information before logging
        safe_input = mask_pii(user_input)

        logging.info(
            f"Customer={safe_input} | Agent={response}"
        )

        print(f"Agent: {response}")


if __name__ == "__main__":
    main()