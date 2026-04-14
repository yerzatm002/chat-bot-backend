from app.db.base import Base
from app.db.session import engine

# ВАЖНО: импортируем модели через init_db
import app.db.init_db  # ← ключевой момент

Base.metadata.create_all(bind=engine)

print("Tables created successfully")