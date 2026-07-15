from fastapi import APIRouter
from fastapi import UploadFile,File

from app.services.upload_service import upload_document

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

@router.post("/")
def upload(file: UploadFile = File(...)):

    return upload_document(file)