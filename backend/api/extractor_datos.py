from fastapi import APIRouter
from pydantic import BaseModel

from backend.modules.extractor_datos import extraer_datos

router = APIRouter()


class Solicitud(BaseModel):
    texto: str


@router.post("/extractor-datos")
def extractor_datos(
    request: Solicitud
):

    resultado = extraer_datos(
        request.texto
    )

    return {
        "resultado": resultado
    }