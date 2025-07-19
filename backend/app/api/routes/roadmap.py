from fastapi import APIRouter
router = APIRouter()

@router.get("/")
async def get_roadmap():
    return {"message": "Career roadmap endpoint - coming soon"}
