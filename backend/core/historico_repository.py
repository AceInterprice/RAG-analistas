from backend.core.mysql import execute_query


def guardar_reporte(
    modulo: str,
    narrativa: str,
    reporte: str,
    estado_caso: str = "ABIERTO"
):

    query = """
    INSERT INTO historico_reportes
    (
        modulo,
        narrativa,
        reporte,
        estado_caso
    )
    VALUES
    (
        %s,
        %s,
        %s,
        %s
    )
    """

    execute_query(
        query,
        (
            modulo,
            narrativa,
            reporte,
            estado_caso
        )
    )