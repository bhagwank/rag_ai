from langchain_chroma import Chroma

from app.rag.embeddings import get_embedding_model
from app.core.config import settings


_vector_store = None


def get_vector_store():
    global _vector_store

    if _vector_store is None:
        _vector_store = Chroma(
            persist_directory=settings.CHROMA_PATH,
            embedding_function=get_embedding_model()
        )

    return _vector_store