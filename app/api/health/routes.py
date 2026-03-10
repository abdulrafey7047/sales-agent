from fastapi import APIRouter, status


router = APIRouter(prefix="/health")

@router.post("/")
async def health():
    return status.HTTP_200_OK
    

@router.get("/success")
async def success():
    return "running"
