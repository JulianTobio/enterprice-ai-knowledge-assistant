from shared.repositories.llm_base import BaseLLMRepository
from shared.repositories.ollama_repo import OllamaRepository

def get_llm_repository() -> BaseLLMRepository:
    """
    Dependency to get the LLM repository instance.
    This can be extended to support different LLM backends in the future.
    """
    return OllamaRepository()