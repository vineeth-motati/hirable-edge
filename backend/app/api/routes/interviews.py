from fastapi import APIRouter
router = APIRouter()

@router.get("/")
async def get_interviews():
    return {"message": "Mock interviews endpoint - coming soon"}
