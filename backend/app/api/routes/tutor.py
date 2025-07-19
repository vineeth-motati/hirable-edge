from fastapi import APIRouter
router = APIRouter()

@router.get("/")
async def get_tutor():
    return {"message": "AI Tutor endpoint - coming soon"}
