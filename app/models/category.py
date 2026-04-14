from sqlalchemy import Column, Integer, Text
from app.db.base import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name_ru = Column(Text, nullable=False)
    name_kz = Column(Text, nullable=False)