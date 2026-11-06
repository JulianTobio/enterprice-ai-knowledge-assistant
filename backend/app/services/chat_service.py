from app.repositories.llm_base import BaseLLMRepository

class ChatService:
    def __init__(self, llm_repository: BaseLLMRepository):
        self.llm_repository = llm_repository

    async def chat(self, prompt: str) -> str:
        
        # Define a system prompt to guide the LLM's behavior
        system_prompt = "Eres un asistente de IA que responde a las preguntas de los usuarios de manera clara y concisa."
        
        # Use the LLM repository to generate a response based on the prompt
        response = await self.llm_repository.generate(prompt, system_prompt=system_prompt)
        return response.message_content