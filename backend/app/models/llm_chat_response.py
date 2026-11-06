from pydantic import BaseModel

class LLMChatResponse(BaseModel):
    message_content: str
    message_role: str
    model: str