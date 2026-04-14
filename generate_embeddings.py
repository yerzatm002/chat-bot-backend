import json

from app.db.session import SessionLocal
import app.db.init_db  

from app.models.faq_question import FAQQuestion
from app.services.embedding_service import EmbeddingService
from app.utils.text_processing import normalize_text


def main():
    db = SessionLocal()
    embedding_service = EmbeddingService()

    faq_questions = db.query(FAQQuestion).all()

    for item in faq_questions:
        normalized_text = normalize_text(item.question_text)
        vector = embedding_service.encode(normalized_text)
        item.embedding = json.dumps(vector)

    db.commit()
    db.close()

    print("Embeddings generated successfully")


if __name__ == "__main__":
    main()