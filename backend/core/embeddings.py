from sentence_transformers import SentenceTransformer

from backend.core.config import (
    EMBEDDING_MODEL
)

_model = None


def get_embedding():
    """
    Devuelve el modelo de embeddings
    cargado una sola vez.
    """

    global _model

    if _model is None:

        _model = SentenceTransformer(
            EMBEDDING_MODEL
        )

    return _model


def embed_text(
    text: str
):
    """
    Convierte texto en vector.
    """

    model = get_embedding()

    vector = model.encode(text)

    return vector.tolist()