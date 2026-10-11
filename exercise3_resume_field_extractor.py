
import json
import re


def extract_resume_fields(resume_text, fields_to_extract):
    """Extract requested fields and return a JSON-compatible dictionary."""

    if not resume_text.strip():
        raise ValueError("Resume text cannot be empty.")

    if not fields_to_extract:
        raise ValueError("Enter at least one field to extract.")

    text = resume_text.strip()
    result = {}

    for field in fields_to_extract:
        key = field.strip()
        field_lower = key.lower()
        value = None

        if field_lower in ("name", "full name"):
            match = re.search(
                r"(?:name)\s*:\s*([^\n,]+)",
                text,
                re.IGNORECASE
            )
            if match:
                value = match.group(1).strip()

        elif field_lower in ("email", "email address"):
            match = re.search(
                r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
                text
            )
            if match:
                value = match.group(0)

        elif field_lower in ("phone", "phone number", "mobile"):
            match = re.search(
                r"(?:phone|mobile|contact)\s*:\s*([+()\d -]{7,})",
                text,
                re.IGNORECASE
            )
            if match:
                value = match.group(1).strip()

        elif field_lower in ("degree", "education", "qualification"):
            match = re.search(
                r"(?:degree|education|qualification)\s*:\s*([^\n]+)",
                text,
                re.IGNORECASE
            )
            if match:
                value = match.group(1).strip()

        elif field_lower in ("skills", "technical skills"):
            match = re.search(
                r"(?:skills|technical skills)\s*:\s*([^\n]+)",
                text,
                re.IGNORECASE
            )
            if match:
                value = [
                    skill.strip()
                    for skill in match.group(1).split(",")
                    if skill.strip()
                ]

        result[key] = value

    return result


def main():
    print("\n=== Exercise 3: Resume Field Extractor ===")

    resume_text = input("Enter resume text: ").strip()

    fields_input = input(
        "Fields to extract (comma-separated): "
    ).strip()

    fields_to_extract = list(dict.fromkeys(
        field.strip()
        for field in fields_input.split(",")
        if field.strip()
    ))

    try:
        result = extract_resume_fields(
            resume_text,
            fields_to_extract
        )

        print("\n--- Extracted JSON ---")
        print(json.dumps(result, indent=4, ensure_ascii=False))

    except ValueError as error:
        print("ERROR:", error)


if __name__ == "__main__":
    main()
