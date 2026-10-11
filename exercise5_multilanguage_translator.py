
VALID_FORMALITY = {"formal", "neutral", "informal"}

TRANSLATIONS = {
    "hello": {
        "hindi": {
            "formal": "नमस्कार।",
            "neutral": "नमस्ते।",
            "informal": "हाय!"
        },
        "marathi": {
            "formal": "नमस्कार.",
            "neutral": "नमस्कार.",
            "informal": "हाय!"
        },
        "spanish": {
            "formal": "Hola.",
            "neutral": "Hola.",
            "informal": "¡Hola!"
        }
    },
    "thank you": {
        "hindi": {
            "formal": "आपका धन्यवाद।",
            "neutral": "धन्यवाद।",
            "informal": "शुक्रिया!"
        },
        "marathi": {
            "formal": "आपले आभार.",
            "neutral": "धन्यवाद.",
            "informal": "थँक्स!"
        },
        "spanish": {
            "formal": "Muchas gracias.",
            "neutral": "Gracias.",
            "informal": "¡Gracias!"
        }
    }
}


def translate_sentence(sentence, target_language, formality):
    formality = formality.strip().lower()
    language = target_language.strip().lower()

    if formality not in VALID_FORMALITY:
        raise ValueError("Choose formal, neutral, or informal.")

    if not sentence.strip() or not language:
        raise ValueError("Sentence and target language are required.")

    sentence_key = sentence.strip().lower().rstrip(".!?")

    if sentence_key not in TRANSLATIONS:
        return (
            "Translation unavailable for this sentence in the demo. "
            "Try 'Hello' or 'Thank you'."
        )

    if language not in TRANSLATIONS[sentence_key]:
        return (
            f"Translation unavailable for {target_language}. "
            "This demo supports Hindi, Marathi, and Spanish."
        )

    return TRANSLATIONS[sentence_key][language][formality]


def main():
    print("\n=== Exercise 5: Multi-language Translator ===")

    sentence = input("Sentence: ").strip()
    language = input("Target language: ").strip()

    print("Formality options: formal, neutral, informal")
    formality = input("Formality: ").strip()

    try:
        translation = translate_sentence(
            sentence, language, formality
        )
        print("\n--- Translation ---")
        print(translation)

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
