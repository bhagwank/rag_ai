from fastapi import APIRouter
from app.services.ask_service import ask_question
from app.models.models import Question
router = APIRouter(
    prefix="/ask",
    tags=["RAG"]
)

@router.post("/")
def ask(request: Question):

    return ask_question(request.question)