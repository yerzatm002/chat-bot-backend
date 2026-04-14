from sentence_transformers import SentenceTransformer


class EmbeddingService:
    def __init__(self):
        self.model = SentenceTransformer(
            "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        )

    def encode(self, text: str) -> list[float]:
        vector = self.model.encode(text)
        return vector.tolist()