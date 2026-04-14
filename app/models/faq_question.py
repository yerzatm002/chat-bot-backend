from sqlalchemy import Column, Integer, Text, ForeignKey, String, TIMESTAMP
from sqlalchemy.sql import func
from app.db.base import Base


class FAQQuestion(Base):
    __tablename__ = "faq_questions"

    id = Column(Integer, primary_key=True, index=True)
    faq_id = Column(Integer, ForeignKey("faq_answers.id", ondelete="CASCADE"))
    language = Column(String(2), nullable=False)
    question_text = Column(Text, nullable=False)
    embedding = Column(Text)  # пока TEXT (потом можно JSON)
    created_at = Column(TIMESTAMP, server_default=func.now())