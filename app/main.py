from fastapi import FastAPI
from app.api import (
    upload,
    ask,
    search,
    documents,
    debug
)
from app.core.config import settings
from app.core.logger import logger

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

#The routers contain endpoint definitions, while main.py simply assembles the application.
app.include_router(upload.router)
app.include_router(ask.router)
app.include_router(search.router)
app.include_router(documents.router)
app.include_router(debug.router)

@app.get("/")
def home():
    logger.info("Health check called")
    return {
        "RAG AI PROJECT IS RUNNING"
    }