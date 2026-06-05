import re


def clean_text(
    text: str
) -> str:
    """
    Limpieza básica.
    """

    if not text:

        return ""

    text = text.replace(
        "\xa0",
        " "
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    text = text.strip()

    return text