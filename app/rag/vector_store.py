from langchain_chroma import Chroma
from app.rag.embeddings import get_embedding_model
from app.core.config import settings

def get_vector_store():

    return Chroma(

        persist_directory=settings.CHROMA_PATH,

        embedding_function=get_embedding_model()

    )