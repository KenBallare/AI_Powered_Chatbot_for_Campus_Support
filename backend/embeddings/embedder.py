from sentence_transformers import SentenceTransformer
from backend.config.config import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)

def get_embedding(text: str):
    return model.encode(text).tolist()

#This is the core of the MVP intelligence layer