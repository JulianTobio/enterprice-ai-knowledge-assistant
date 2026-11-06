from fastapi import Depends
from app.core.config import LLM_MODEL_NAME
from app.repositories.llm_base import BaseLLMRepository
from app.repositories.ollama_repo import OllamaRepository
from app.services.chat_service import ChatService
from app.services.file_service import FileService
from app.services.queue_service import QueueService
from app.repositories.metadata_base import MetadataBase
from app.repositories.metadata_repo import MetadataRepository
from app.db.database import get_db
from app.db.redis import get_queue
from sqlalchemy.orm import Session
from rq import Queue

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

def get_metadata_repository(session: Session = Depends(get_db)) -> MetadataBase:
    """
    Dependency to get the metadata repository instance.
    This can be extended to support different db backends in the future.
    It depends on the database session
    """
    return MetadataRepository(db_session=session)

def get_queue_service(db_queue: Queue = Depends(get_queue)) -> QueueService:
    return QueueService(queue=db_queue)

def get_file_service(metadata_repo: MetadataBase = Depends(get_metadata_repository)) -> "FileService":
    """
    Dependency to get the FileService instance.
    It depends on the Metadata repository
    """
    return FileService(metadata_repository=metadata_repo)