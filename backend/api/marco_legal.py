from fastapi import APIRouter
from backend.modules.marco_legal import consultar_marco_legal

router = APIRouter()


@router.post("/marco-legal")
def marco_legal(payload: dict):

    texto = payload.get("texto", "")

    if not texto:
        return {
            "error": "Texto vacío"
        }

    resultado = consultar_marco_legal(texto)

    return {
        "modulo": "marco_legal",
        "resultado": resultado
    }