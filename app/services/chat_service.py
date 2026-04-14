import json
from app.models import faq_answer
from sqlalchemy.orm import Session

from app.models.faq_question import FAQQuestion
from app.models.faq_answer import FAQAnswer
from app.utils.text_processing import normalize_text
from app.services.language_service import detect_language
from app.services.embedding_service import EmbeddingService
from app.services.similarity_service import calculate_similarity


THRESHOLD = 0.65


class ChatService:
    def __init__(self):
        self.embedding_service = EmbeddingService()

    def find_best_match(self, user_message: str, db: Session) -> dict:
        normalized = normalize_text(user_message)
        detected_language = detect_language(normalized)
        user_embedding = self.embedding_service.encode(normalized)

        #faq_questions = db.query(FAQQuestion).all()
        faq_questions = db.query(FAQQuestion).filter(
            FAQQuestion.language == detected_language
            ).all()

        best_question = None
        best_score = -1.0

        for faq_question in faq_questions:
            if not faq_question.embedding:
                continue

            stored_embedding = json.loads(faq_question.embedding)
            score = calculate_similarity(user_embedding, stored_embedding)

            if score > best_score:
                best_score = score
                best_question = faq_question

        if not best_question or best_score < THRESHOLD:
            return {
                "detected_language": detected_language,
                "matched_faq_id": None,
                "similarity_score": best_score,
                "bot_response": self.get_fallback_message(detected_language),
                "is_fallback": True
            }

        faq_answer = db.query(FAQAnswer).filter(
            FAQAnswer.id == best_question.faq_id
        ).first()

        if detected_language == "kz":
            response_text = faq_answer.answer_kz or faq_answer.answer_ru
        else:
            response_text = faq_answer.answer_ru or faq_answer.answer_kz
        #response_text = faq_answer.answer_ru if detected_language == "ru" else faq_answer.answer_kz

        return {
            "detected_language": detected_language,
            "matched_faq_id": faq_answer.id,
            "similarity_score": best_score,
            "bot_response": response_text,
            "is_fallback": False
        }

    def get_fallback_message(self, language: str) -> str:
        if language == "kz":
            return (
                "Кешіріңіз, жүйе сіздің сұрағыңызға дәл сәйкес жауапты анықтай алмады. "
                "Сұрағыңызды қысқа әрі нақты етіп қайта жазыңыз."
            )

        return (
            "Извините, система не смогла точно определить подходящий ответ на ваш запрос. "
            "Попробуйте сформулировать вопрос короче и конкретнее."
        )