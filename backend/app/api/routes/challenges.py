from fastapi import APIRouter
router = APIRouter()

@router.get("/")
async def get_challenges():
    return {"message": "Challenges endpoint - coming soon"}
