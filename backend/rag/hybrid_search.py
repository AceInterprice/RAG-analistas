from backend.rag.retriever import buscar_contexto


def hybrid_search(
    query: str
) -> list[str]:
    """
    Recupera leyes y reportes relevantes
    eliminando duplicados.
    """

    leyes = buscar_contexto(
        query,
        tipo="case"
    )

    reportes = buscar_contexto(
        query,
        tipo="report"
    )

    print("\n===== LEYES RECUPERADAS =====\n")

    for i, chunk in enumerate(leyes, start=1):

        print(f"\n--- LEY {i} ---\n")

        print(chunk)

    print("\n===== REPORTES RECUPERADOS =====\n")

    for i, chunk in enumerate(reportes, start=1):

        print(f"\n--- REPORTE {i} ---\n")

        print(chunk)

    combined = []

    for chunk in leyes:

        if chunk and chunk not in combined:

            combined.append(
                chunk
            )

    for chunk in reportes:

        if chunk and chunk not in combined:

            combined.append(
                chunk
            )

    return combined