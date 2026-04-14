from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService
from app.api.deps import get_db
from app.models.chat_log import ChatLog

router = APIRouter()
chat_service = ChatService()


@router.post("/chat/message", response_model=ChatResponse)
def chat_message(request: ChatRequest, db: Session = Depends(get_db)):

    result = chat_service.find_best_match(request.message, db)

    # логирование
    chat_log = ChatLog(
        user_message=request.message,
        detected_language=result["detected_language"],
        matched_faq_id=result["matched_faq_id"],
        similarity_score=result["similarity_score"],
        bot_response=result["bot_response"],
        is_fallback=result["is_fallback"]
    )

    db.add(chat_log)
    db.commit()

    return ChatResponse(
        response=result["bot_response"],
        language=result["detected_language"],
        matched_faq_id=result["matched_faq_id"],
        similarity_score=result["similarity_score"],
        is_fallback=result["is_fallback"]
    )