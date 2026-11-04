from fastapi import Depends
from app.core.config import LLM_MODEL_NAME
from app.repositories.llm_base import BaseLLMRepository
from app.repositories.ollama_repo import OllamaRepository
from app.services.chat_service import ChatService
from app.services.file_service import FileService

def get_llm_repository() -> BaseLLMRepository:
    """
    Dependency to get the LLM repository instance.
    This can be extended to support different LLM backends in the future.
    """
    return OllamaRepository(model=LLM_MODEL_NAME)

def get_chat_service(llm_repo: BaseLLMRepository = Depends(get_llm_repository)) -> ChatService:
    """
    Dependency to get the ChatService instance.
    It depends on the LLM repository.
    """
    return ChatService(llm_repository=llm_repo)

def get_file_service() -> "FileService":
    """
    Dependency to get the FileService instance.
    """
    return FileService()