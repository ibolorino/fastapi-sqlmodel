from fastapi import APIRouter


router = APIRouter(prefix="/healthcheck")

@router.get("/")
def health_check():
    return {"status": "OK"}