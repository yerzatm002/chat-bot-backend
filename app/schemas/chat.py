from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str
    language: str
    matched_faq_id: int | None
    similarity_score: float
    is_fallback: bool