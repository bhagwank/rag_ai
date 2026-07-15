from fastapi import APIRouter

router = APIRouter(
    prefix="/debug",
    tags=["Debug"]
)

@router.get("/")
def debug():
    return {
        "status": "OK"
    }