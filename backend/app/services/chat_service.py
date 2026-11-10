from shared.repositories.llm_base import BaseLLMRepository
from chromadb import Collection

class ChatService:
    def __init__(self, llm_repository: BaseLLMRepository, chroma_collection: Collection):
        self.llm_repository = llm_repository
        self.vector_collection = chroma_collection

    async def chat(self, prompt: str, rag: bool = False) -> str:
        
        # Define a system prompt to guide the LLM's behavior
        system_prompt = "Eres un asistente de IA que responde a las preguntas de los usuarios de manera clara y concisa."
        
        if (rag):

            # Embed user prompt
            prompt_embedding = await self.llm_repository.embed(input=[prompt])

            # Search ChromaDB for the closest vector matches
            vector_results = self.vector_collection.query(query_embeddings=[prompt_embedding][0], n_results=3)

            # Create contexts from the matching documents
            context_text = ""

            for idx, doc in enumerate(vector_results["documents"][0]):
                context_text += f"Documento {idx + 1} (fuente: {vector_results['metadatas'][0][idx]['source']}, pagina: {vector_results['metadatas'][0][idx]['page']}): [{doc}]\n" 

            # Add context to system prompt
            system_prompt = f"{system_prompt} Responde utilizando la información en el contexto.\n\n<contexto>\n{context_text}\n</contexto>"
        
        # Use the LLM repository to generate a response based on the prompt
        response = await self.llm_repository.generate(prompt, system_prompt=system_prompt)
        return response.message_content