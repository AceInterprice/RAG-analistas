import os

# Ruta absoluta al ffmpeg del proyecto
BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)

FFMPEG_PATH = os.path.join(
    BASE_DIR,
    "ffmpeg",
    "bin"
)

os.environ["PATH"] += os.pathsep + FFMPEG_PATH

import whisper

model = whisper.load_model(
    "base"
)


def transcribir_audio(
    ruta_audio: str
) -> str:

    resultado = model.transcribe(
        ruta_audio,
        language="es"
    )

    return resultado["text"]