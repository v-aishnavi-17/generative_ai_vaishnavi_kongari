

CATEGORIES = {"POSITIVE", "NEGATIVE", "MIXED", "NEUTRAL", "UNCLEAR"}


def classify_review(review_text):
    review = review_text.lower()

    positive_words = [
        "good", "great", "excellent", "amazing",
        "love", "satisfied", "wonderful", "perfect",
        "happy", "helpful", "fast"
    ]

    negative_words = [
        "bad", "poor", "terrible", "awful",
        "hate", "disappointed", "worst", "broken",
        "slow", "damaged", "unhappy"
    ]

    positive_count = sum(word in review for word in positive_words)
    negative_count = sum(word in review for word in negative_words)

    if not review.strip():
        return "UNCLEAR"

    if positive_count > 0 and negative_count > 0:
        return "MIXED"
    elif positive_count > 0:
        return "POSITIVE"
    elif negative_count > 0:
        return "NEGATIVE"
    elif any(char.isalpha() for char in review):
        return "NEUTRAL"
    else:
        return "UNCLEAR"


def main():
    print("\n=== Exercise 2: Review Classifier ===")

    review = input("Enter customer review: ").strip()

    if not review:
        print("Review cannot be empty.")
        return

    category = classify_review(review)
    print("\nCategory:", category)


if __name__ == "__main__":
    main()
