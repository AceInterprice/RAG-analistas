from fastapi import APIRouter

from backend.api.redaccion import router as redaccion_router
from backend.api.marco_legal import router as legal_router

router = APIRouter()

router.include_router(redaccion_router)
router.include_router(legal_router)