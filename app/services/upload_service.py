import os
import shutil

from fastapi import UploadFile

from app.core.config import settings
from app.core.logger import logger


def save_uploaded_file(file: UploadFile):

    os.makedirs(settings.UPLOAD_FOLDER, exist_ok=True)

    file_path = os.path.join(
        settings.UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    logger.info(f"Saved {file.filename}")

    return file_path


from app.rag.ingest import ingest_pdf

def upload_document(file: UploadFile):

    path = save_uploaded_file(file)

    ingest_pdf(path)

    return {

        "message": "Document uploaded successfully",

        "filename": file.filename

    }