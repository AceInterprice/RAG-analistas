from backend.ingest.ingest_leyes import ingest_leyes
from backend.ingest.ingest_reportes import ingest_reportes


def ingest_all():
    """
    Indexa todas las leyes y reportes disponibles.
    """

    ingest_leyes()
    ingest_reportes()
