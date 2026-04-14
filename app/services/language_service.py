from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

# специфичные казахские буквы
KAZAKH_CHARS = set("әіңғүұқөһ")


def is_kazakh(text: str) -> bool:
    return any(char in KAZAKH_CHARS for char in text.lower())


def detect_language(text: str) -> str:
    try:
        # 1. проверка на казахский (самая важная)
        if is_kazakh(text):
            return "kz"

        # 2. fallback на langdetect
        lang = detect(text)

        if lang == "ru":
            return "ru"

        # всё остальное считаем казахским (для MVP)
        return "kz"

    except Exception:
        return "ru"