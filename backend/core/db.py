import chromadb

from backend.core.config import (
    CHROMA_PATH,
    CHROMA_COLLECTION
)

# cliente compartido
_client = None


def get_client():
    """
    Devuelve una instancia única
    de ChromaDB.
    """

    global _client

    if _client is None:

        CHROMA_PATH.mkdir(parents=True, exist_ok=True)

        _client = chromadb.PersistentClient(
            path=str(CHROMA_PATH)
        )

    return _client


def get_collection(
    name=CHROMA_COLLECTION
):
    """
    Obtiene o crea colección.
    """

    client = get_client()

    return client.get_or_create_collection(
        name=name
    )