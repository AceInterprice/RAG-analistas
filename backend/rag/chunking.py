from backend.utils.cleaner import clean_text


def split_text(
    text: str,
    chunk_size: int = 1200,
    overlap: int = 200
) -> list[str]:
    """
    Divide texto en chunks optimizados para RAG legal/policial.
    """

    if overlap >= chunk_size:
        raise ValueError("overlap debe ser menor que chunk_size")

    text = clean_text(text)

    if not text:
        return []

    chunks = []

    start = 0
    text_length = len(text)

    while start < text_length:

        end = start + chunk_size

        chunk = text[start:end]

        chunk = clean_text(chunk)

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks