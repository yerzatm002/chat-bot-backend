from sqlalchemy import Column, Integer, Text, Float, ForeignKey, String, TIMESTAMP
from sqlalchemy.sql import func
from app.db.base import Base
from sqlalchemy import Boolean

class ChatLog(Base):
    __tablename__ = "chat_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_message = Column(Text, nullable=False)
    detected_language = Column(String(2))
    matched_faq_id = Column(Integer, ForeignKey("faq_answers.id"))
    similarity_score = Column(Float)
    bot_response = Column(Text, nullable=False)
    is_fallback = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=func.now())