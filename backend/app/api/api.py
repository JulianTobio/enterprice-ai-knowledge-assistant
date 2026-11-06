from fastapi import APIRouter
from app.core.config import API_PREFIX
from app.api.endpoints import health
from app.api.endpoints import chat
from app.api.endpoints import files

router = APIRouter()
router.include_router(health.router, tags=["health"])
router.include_router(chat.router, tags=["chat"], prefix=f"{API_PREFIX}/chat")
router.include_router(files.router, tags=["files"], prefix=f"{API_PREFIX}/files")