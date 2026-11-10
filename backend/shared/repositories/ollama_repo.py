from typing import Sequence
from shared.repositories.llm_base import BaseLLMRepository
from ollama import Client
from app.models.llm_chat_response import LLMChatResponse
from app.core.config import OLLAMA_BASE_URL, LLM_MODEL_NAME, EMBED_MODEL_NAME

class OllamaRepository(BaseLLMRepository):
    def __init__(self):
        self.llm_model = LLM_MODEL_NAME
        self.embed_model = EMBED_MODEL_NAME
        self.client = Client(host=OLLAMA_BASE_URL)

    async def generate(self, prompt: str, system_prompt: str = None, **kwargs) -> LLMChatResponse:
        # Prepare messages for the Ollama chat
        messages = []
        
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        # Generate a response from the Ollama model
        response = self.client.chat(
            model=self.llm_model,
            messages=messages,
            options={"temperature": kwargs.get("temperature", 0.7)}
            )
        
        return LLMChatResponse(
            message_content=response['message']['content'],
            message_role=response['message']['role'],
            model=self.llm_model
            )

    async def embed(self, input: Sequence[str]) -> Sequence[Sequence[float]]:
            
            response = self.client.embed(
                model=self.embed_model,
                input=input
                )
            
            return response["embeddings"]