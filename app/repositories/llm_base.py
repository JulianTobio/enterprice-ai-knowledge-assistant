from abc import ABC, abstractmethod
from app.models.llm_chat_response import LLMChatResponse

class BaseLLMRepository(ABC):
    @abstractmethod
    async def generate(self, prompt: str, system_prompt: str = None, **kwargs) -> LLMChatResponse:
        """Send prompt to LLM provider and return uniform dictionary response."""
        pass