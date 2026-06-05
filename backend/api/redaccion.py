from fastapi import APIRouter
from backend.modules.redaccion_policial import redactar_reporte

router = APIRouter()


@router.post("/redaccion-policial")
def redaccion_policial(payload: dict):

    texto = payload.get("texto", "")

    if not texto:
        return {
            "error": "Texto vacío"
        }

    resultado = redactar_reporte(texto)

    return {
        "modulo": "redaccion_policial",
        "resultado": resultado
    }