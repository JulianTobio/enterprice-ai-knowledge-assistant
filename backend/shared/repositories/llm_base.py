from abc import ABC, abstractmethod
from typing import Sequence
from app.models.llm_chat_response import LLMChatResponse

class BaseLLMRepository(ABC):
    @abstractmethod
    async def generate(self, prompt: str, system_prompt: str = None, **kwargs) -> LLMChatResponse:
        """Send prompt to LLM provider and return uniform dictionary response."""
        pass

    @abstractmethod
    async def embed(self, input: Sequence[str]) -> Sequence[Sequence[float]]:
        """Send prompt to LLM provider and return uniform dictionary response."""
        pass