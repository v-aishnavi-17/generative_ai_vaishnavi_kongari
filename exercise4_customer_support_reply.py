

def count_words(text):
    return len(text.split())


def generate_support_reply(customer_message, company_name, max_words):
    if max_words < 1:
        raise ValueError("Maximum words must be at least 1.")

    message = customer_message.lower()

    if any(word in message for word in ["damaged", "broken", "defective"]):
        reply = (
            f"We're sorry the product arrived damaged. "
            f"Please share your order number so {company_name} "
            "can help with the next steps."
        )

    elif any(word in message for word in ["late", "delayed", "not arrived"]):
        reply = (
            f"We're sorry your delivery is delayed. "
            f"Please share your order number so {company_name} "
            "can check the details."
        )

    elif any(word in message for word in ["refund", "money back"]):
        reply = (
            f"Thank you for contacting {company_name}. "
            "Please share your order number so we can review "
            "your refund request."
        )

    elif any(word in message for word in ["cancel", "cancellation"]):
        reply = (
            f"We understand you'd like to cancel your order. "
            f"Please share your order number so {company_name} "
            "can help you with the request."
        )

    else:
        reply = (
            f"Thank you for contacting {company_name}. "
            "Could you please share more details so we can help?"
        )

    # Enforce the maximum word limit.
    words = reply.split()

    if len(words) > max_words:
        reply = " ".join(words[:max_words])

    return reply


def main():
    print("\n=== Exercise 4: Customer Support Reply ===")

    company = input("Company name: ").strip()
    message = input("Customer message: ").strip()

    try:
        max_words = int(input("Maximum words: ").strip())
    except ValueError:
        print("Enter a valid whole number.")
        return

    if not company or not message:
        print("Company name and customer message are required.")
        return

    try:
        reply = generate_support_reply(message, company, max_words)

        print("\n--- Support Reply ---")
        print(reply)
        print(f"\nWord count: {count_words(reply)}/{max_words}")

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
