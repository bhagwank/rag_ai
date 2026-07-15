import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "RAG AI Project"
    APP_VERSION = "1.0.0"
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 100

    LLM_MODEL = os.getenv("LLM_MODEL", "llama3.2:3b")

    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL",
        "nomic-embed-text"
    )

    OLLAMA_BASE_URL = os.getenv(
        "OLLAMA_BASE_URL",
        "http://localhost:11434"
    )

    CHROMA_PATH = os.getenv(
        "CHROMA_PATH",
        "./chroma_db"
    )

    UPLOAD_FOLDER = os.getenv(
        "UPLOAD_FOLDER",
        "./uploads"
    )

    DOCUMENT_FOLDER = os.getenv(
        "DOCUMENT_FOLDER",
        "./documents"
    )

settings = Settings()