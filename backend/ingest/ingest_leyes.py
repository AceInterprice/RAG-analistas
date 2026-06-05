import uuid
from pathlib import Path

from backend.core.db import get_collection
from backend.core.embeddings import embed_text
from backend.ingest.parser import parse_pdf


PDF_PATH = Path(
    "data/leyes"
)


def ingest_leyes():
    """
    Indexa leyes.
    """

    collection = get_collection()

    pdfs = list(
        PDF_PATH.rglob("*.pdf")
    )

    for pdf in pdfs:

        chunks = parse_pdf(
            str(pdf)
        )

        for chunk in chunks:

            collection.add(
                ids=[
                    str(uuid.uuid4())
                ],
                documents=[
                    chunk
                ],
                embeddings=[
                    embed_text(chunk)
                ],
                metadatas=[{
                    "type": "case",
                    "source": pdf.name
                }]
            )

        print(
            f"Indexado: {pdf.name}"
        )