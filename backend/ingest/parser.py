from backend.utils.pdf_loader import extract_text_from_pdf
from backend.rag.chunking import split_text


def parse_pdf(
    pdf_path: str
) -> list[str]:
    """
    Extrae y divide PDF.
    """

    text = extract_text_from_pdf(
        pdf_path
    )

    chunks = split_text(
        text
    )

    return chunks