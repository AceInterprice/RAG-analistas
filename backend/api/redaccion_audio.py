from fastapi import APIRouter, UploadFile, File
import tempfile
import os

from backend.speech.whisper_service import transcribir_audio
from backend.modules.redaccion_policial import redactar_reporte

router = APIRouter()


@router.post("/redaccion-policial-audio")
async def redaccion_policial_audio(
    archivo: UploadFile = File(...)
):

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    ) as temp:

        contenido = await archivo.read()
        temp.write(contenido)

        ruta_audio = temp.name

    try:

        texto = transcribir_audio(
            ruta_audio
        )

        informe = redactar_reporte(
            texto
        )

        return {
            "transcripcion": texto,
            "resultado": informe
        }

    finally:

        if os.path.exists(ruta_audio):
            os.remove(ruta_audio)