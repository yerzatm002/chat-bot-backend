from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from app.db.base import Base


class FAQAnswer(Base):
    __tablename__ = "faq_answers"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    answer_ru = Column(Text, nullable=False)
    answer_kz = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())