from fastapi import FastAPI
from app.core.config import PROJECT_TITLE
from app.api.api import router as api_router
from app.dependencies import get_chat_service

app = FastAPI(
    title=PROJECT_TITLE,
    version="0.1.0",
)

app.include_router(api_router)