import mysql.connector

from backend.core.config import (
    MYSQL_HOST,
    MYSQL_PORT,
    MYSQL_USER,
    MYSQL_PASSWORD,
    MYSQL_DB
)


def get_mysql():
    """
    Devuelve conexión a MySQL.
    """

    return mysql.connector.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )


def execute_query(
    query: str,
    params=None
):
    """
    Ejecuta INSERT / UPDATE / DELETE.
    """

    conn = get_mysql()

    cursor = conn.cursor()

    cursor.execute(
        query,
        params or ()
    )

    conn.commit()

    cursor.close()

    conn.close()


def fetch_all(
    query: str,
    params=None
):
    """
    Devuelve lista de resultados.
    """

    conn = get_mysql()

    cursor = conn.cursor(
        dictionary=True
    )

    cursor.execute(
        query,
        params or ()
    )

    rows = cursor.fetchall()

    cursor.close()

    conn.close()

    return rows


def fetch_one(
    query: str,
    params=None
):
    """
    Devuelve un solo registro.
    """

    conn = get_mysql()

    cursor = conn.cursor(
        dictionary=True
    )

    cursor.execute(
        query,
        params or ()
    )

    row = cursor.fetchone()

    cursor.close()

    conn.close()

    return row