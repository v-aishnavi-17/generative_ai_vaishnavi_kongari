
def refine_draft(draft_text, issue_to_fix, rounds=3):
    if rounds < 3:
        raise ValueError("The lab requires at least three rounds.")

    if not draft_text.strip() or not issue_to_fix.strip():
        raise ValueError("Draft and issue are required.")

    current_draft = draft_text.strip()

    for round_number in range(1, rounds + 1):
        if issue_to_fix.lower() == "grammar":
            current_draft = current_draft.replace("  ", " ").strip()
            if current_draft:
                current_draft = (
                    current_draft[0].upper() + current_draft[1:]
                )
                if current_draft[-1] not in ".!?":
                    current_draft += "."

        elif issue_to_fix.lower() == "clarity":
            current_draft = " ".join(current_draft.split())

        elif issue_to_fix.lower() == "tone":
            current_draft = current_draft.replace("wanna", "want to")
            current_draft = current_draft.replace("gonna", "going to")
            current_draft = current_draft.replace("yeah", "yes")

        print(f"\n--- Refinement Round {round_number} ---")
        print(current_draft)

    return current_draft


def main():
    print("\n=== Exercise 6: Iterative Content Refiner ===")

    draft = input("Enter draft text: ").strip()
    issue = input(
        "Issue to fix (grammar, clarity, tone): "
    ).strip()

    if not draft or not issue:
        print("Draft and issue are required.")
        return

    try:
        final_draft = refine_draft(draft, issue, rounds=3)

        print("\n=== Final Refined Draft ===")
        print(final_draft)

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
