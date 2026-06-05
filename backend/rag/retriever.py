from backend.core.db import get_collection
from backend.core.embeddings import embed_text
from backend.core.config import TOP_K_RESULTS


def buscar_contexto(
    query: str,
    tipo: str | None = None
) -> list[str]:

    collection = get_collection()

    embedding = embed_text(query)

    where = None

    if tipo:

        where = {
            "type": tipo
        }

    results = collection.query(
        query_embeddings=[embedding],
        n_results=TOP_K_RESULTS,
        where=where
    )

    documents = results.get(
        "documents",
        []
    )

    if not documents:

        return []

    return documents[0]