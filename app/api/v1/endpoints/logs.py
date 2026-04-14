from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.chat_log import ChatLog

router = APIRouter()


@router.get("/logs")
def get_logs(limit: int = 50, db: Session = Depends(get_db)):
    logs = db.query(ChatLog).order_by(ChatLog.created_at.desc()).limit(limit).all()

    return [
        {
            "message": log.user_message,
            "language": log.detected_language,
            "faq_id": log.matched_faq_id,
            "score": log.similarity_score,
            "fallback": log.is_fallback,
            "response": log.bot_response,
            "time": log.created_at
        }
        for log in logs
    ]