from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.endpoints import health, chat, logs
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(title=settings.PROJECT_NAME)

origins = [
    "http://localhost:5173", 
    "https://chat-bot-frontend-seven-xi.vercel.app/",  # Vite
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутеров
app.include_router(health.router, prefix=settings.API_V1_STR)
app.include_router(chat.router, prefix=settings.API_V1_STR)
app.include_router(logs.router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    return {"message": "Chatbot API is running"}