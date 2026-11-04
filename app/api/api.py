from fastapi import APIRouter
from app.core.config import API_PREFIX
from app.api.endpoints import health
from app.api.endpoints import chat

router = APIRouter()
router.include_router(health.router, tags=["health"])
router.include_router(chat.router, tags=["chat"], prefix=API_PREFIX)