from fastapi import APIRouter
from backend.modules.redaccion_policial import redactar_reporte

router = APIRouter()


@router.post("/redaccion-policial")
def redaccion_policial(payload: dict):

    texto = payload.get("texto", "")
    estado_caso = payload.get("estado_caso", "")

    if not texto:
        return {
            "error": "Texto vacío"
        }

    if not estado_caso:
        return {
            "error": "Debe proporcionar el estado del caso"
        }

    resultado = redactar_reporte(
        solicitud=texto,
        estado_caso=estado_caso
    )

    return {
        "modulo": "redaccion_policial",
        "estado_caso": estado_caso,
        "resultado": resultado
    }