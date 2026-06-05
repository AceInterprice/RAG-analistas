from pathlib import Path
import fitz

from backend.utils.cleaner import clean_text


def extract_text_from_pdf(
    pdf_path: str
):
    """
    Extrae texto desde PDF.
    """

    pdf_path = Path(pdf_path)

    doc = fitz.open(pdf_path)

    pages = []

    for page in doc:

        text = page.get_text()

        if text.strip():

            pages.append(text)

    doc.close()

    full_text = "\n".join(pages)

    return clean_text(full_text)