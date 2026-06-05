from fastapi import FastAPI

from backend.ingest.runner import ingest_all

from backend.api.redaccion import router as redaccion_router
from backend.api.marco_legal import router as legal_router
from backend.api.extractor_datos import router as extractor_router
from backend.api.redaccion_audio import router as redaccion_audio_router

app = FastAPI(
    title="RAG Analistas API",
    version="1.0.0",
    description="API para asistencia de análisis policial con RAG + LLM"
)


@app.on_event("startup")
def startup_event():

    print("\n=== INICIANDO INDEXACIÓN ===\n")

    try:
        ingest_all()

        print("\n=== INDEXACIÓN FINALIZADA ===\n")

    except Exception as e:

        print(
            f"\n=== ERROR EN INDEXACIÓN: {e} ===\n"
        )


@app.get("/")
def root():

    return {
        "status": "ok",
        "message": "RAG Analistas API funcionando"
    }


app.include_router(
    redaccion_router,
    prefix="/api",
    tags=["Redacción Policial"]
)

app.include_router(
    legal_router,
    prefix="/api",
    tags=["Marco Legal"]
)

app.include_router(
    extractor_router,
    prefix="/api",
    tags=["Extractor de Datos"]
)

app.include_router(
    redaccion_audio_router,
    prefix="/api",
    tags=["Redacción Policial con Audio"]
)

