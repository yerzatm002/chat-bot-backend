from sentence_transformers import SentenceTransformer


class EmbeddingService:
    _model = None

    @classmethod
    def get_model(cls):
        if cls._model is None:
            print("Loading model...")  # лог для Render
            cls._model = SentenceTransformer(
                "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
            )
        return cls._model

    def encode(self, text: str):
        model = self.get_model()
        return model.encode(text).tolist()