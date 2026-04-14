import json
from app.db.session import SessionLocal
from app.models.category import Category
from app.models.faq_answer import FAQAnswer
from app.models.faq_question import FAQQuestion

db = SessionLocal()


def load_json():
    with open("data/faq.json", "r", encoding="utf-8") as f:
        return json.load(f)


def create_or_get_category(name_ru, name_kz):
    category = db.query(Category).filter_by(name_ru=name_ru).first()

    if category:
        return category.id

    category = Category(name_ru=name_ru, name_kz=name_kz)
    db.add(category)
    db.flush()
    return category.id


def seed():
    data = load_json()

    for category_block in data:
        cat_ru = category_block["category"]["ru"]
        cat_kz = category_block["category"]["kz"]

        category_id = create_or_get_category(cat_ru, cat_kz)

        for faq in category_block["faqs"]:
            answer = FAQAnswer(
                category_id=category_id,
                answer_ru=faq["answer_ru"],
                answer_kz=faq["answer_kz"]
            )

            db.add(answer)
            db.flush()

            # RU вопросы
            for q in faq["questions_ru"]:
                db.add(FAQQuestion(
                    faq_id=answer.id,
                    language="ru",
                    question_text=q
                ))

            # KZ вопросы
            for q in faq["questions_kz"]:
                db.add(FAQQuestion(
                    faq_id=answer.id,
                    language="kz",
                    question_text=q
                ))

    db.commit()
    print("FAQ LOADED SUCCESSFULLY")


if __name__ == "__main__":
    seed()