from fastapi import APIRouter
from app.db.session import SessionLocal

router = APIRouter()


@router.get("/health")
def health_check():
    db = SessionLocal()
    try:
        db.execute("SELECT 1")
        return {"status": "ok", "db": "connected"}
    except Exception:
        return {"status": "error", "db": "failed"}
    finally:
        db.close()