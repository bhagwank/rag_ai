from langchain_ollama import ChatOllama
from app.core.config import settings

# Only LLM initialization
def get_llm():
    return ChatOllama(
        model = settings.LLM_MODEL,
        base_url = settings.OLLAMA_BASE_URL
    )