import re


def generate_slug(text: str) -> str:

    text = text.lower()

    text = text.strip()

    text = re.sub(r"\s+", "-", text)

    text = re.sub(
        r"[^a-z0-9\-]",
        "",
        text,
    )

    return text
