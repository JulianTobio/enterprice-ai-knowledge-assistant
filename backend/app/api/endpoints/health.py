from fastapi import APIRouter, status
from app.core.config import PROJECT_TITLE

router = APIRouter()

@router.get("/health")
async def health_check():
    return {
        "status": status.HTTP_200_OK,
        "service": PROJECT_TITLE
    }