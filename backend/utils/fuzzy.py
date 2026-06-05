from rapidfuzz import fuzz


def similar(
    a: str,
    b: str
) -> int:
    """
    similitud 0-100
    """

    return fuzz.ratio(a, b)


def is_similar(
    a: str,
    b: str,
    threshold=85
) -> bool:
    """
    valida coincidencia.
    """

    score = similar(a, b)

    return score >= threshold