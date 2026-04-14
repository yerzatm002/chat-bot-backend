from app.db.session import SessionLocal
from app.services.chat_service import ChatService


def main():
    db = SessionLocal()
    service = ChatService()

    result = service.find_best_match("Как зарегистрироваться на платформе?", db)
    print(result)

    db.close()


if __name__ == "__main__":
    main()