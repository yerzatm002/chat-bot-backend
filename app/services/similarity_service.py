import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(vec1: list[float], vec2: list[float]) -> float:
    a = np.array(vec1).reshape(1, -1)
    b = np.array(vec2).reshape(1, -1)
    return float(cosine_similarity(a, b)[0][0])