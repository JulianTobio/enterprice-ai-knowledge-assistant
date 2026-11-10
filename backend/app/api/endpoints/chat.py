from fastapi import APIRouter, status, Depends
from app.dependencies import get_chat_service
from app.services.chat_service import ChatService
from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse

router = APIRouter()

@router.post("/", response_model=ChatResponse, status_code=status.HTTP_200_OK)
async def chat_endpoint(payload: ChatRequest, service: ChatService = Depends(get_chat_service)):

    service_response = await service.chat(prompt=payload.message)
    
    return ChatResponse(
        message=service_response
        )

@router.post("/rag", response_model=ChatResponse, status_code=status.HTTP_200_OK)
async def chat_endpoint(payload: ChatRequest, service: ChatService = Depends(get_chat_service)):

    service_response = await service.chat(prompt=payload.message, rag=True)
    
    return ChatResponse(
        message=service_response
        )