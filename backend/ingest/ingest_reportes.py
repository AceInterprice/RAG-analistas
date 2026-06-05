import shutil
import uuid
from pathlib import Path

from backend.core.db import get_collection
from backend.core.embeddings import embed_text
from backend.ingest.parser import parse_pdf


REPORTES_PATH = Path(
    "data/reportes_pdf"
)

PROCESADOS_PATH = Path(
    "data/procesados"
)


def ingest_reportes():
    """
    Indexa reportes.
    """

    collection = get_collection()

    pdfs = list(
        REPORTES_PATH.rglob("*.pdf")
    )

    PROCESADOS_PATH.mkdir(
        exist_ok=True
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
                    "type": "report",
                    "source": pdf.name
                }]
            )

        destino = (
            PROCESADOS_PATH
            / pdf.name
        )

        shutil.move(
            str(pdf),
            str(destino)
        )

        print(
            f"Procesado: {pdf.name}"
        )