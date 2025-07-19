from fastapi import APIRouter, Depends, HTTPException, status
from app.core.auth import get_current_user
from app.core.database import get_database
from app.models.user import User, UserResponse, UserUpdate
from typing import List

router = APIRouter()

@router.get("/me", response_model=UserResponse)
async def get_current_user_profile(current_user: User = Depends(get_current_user)):
    """Get current user profile"""
    return current_user

@router.put("/me", response_model=UserResponse)
async def update_current_user_profile(
    user_update: UserUpdate,
    current_user: User = Depends(get_current_user),
    db = Depends(get_database)
):
    """Update current user profile"""
    update_data = user_update.dict(exclude_unset=True)

    if update_data:
        await db.users.update_one(
            {"_id": current_user.id},
            {"$set": update_data}
        )

    # Fetch updated user
    updated_user = await db.users.find_one({"_id": current_user.id})
    return UserResponse(**updated_user)

@router.get("/leaderboard", response_model=List[dict])
async def get_leaderboard(
    limit: int = 10,
    db = Depends(get_database)
):
    """Get user leaderboard based on points"""
    pipeline = [
        {"$match": {"is_active": True}},
        {"$sort": {"progress.total_points": -1}},
        {"$limit": limit},
        {"$project": {
            "id": "$_id",
            "name": {"$concat": ["$profile.first_name", " ", "$profile.last_name"]},
            "university": "$profile.university",
            "total_points": "$progress.total_points",
            "level": "$progress.level",
            "badges_count": {"$size": "$progress.badges_earned"}
        }}
    ]

    cursor = db.users.aggregate(pipeline)
    leaderboard = []
    async for user in cursor:
        leaderboard.append(user)

    return leaderboard

@router.get("/stats", response_model=dict)
async def get_user_stats(
    current_user: User = Depends(get_current_user),
    db = Depends(get_database)
):
    """Get user statistics"""
    # Get quiz stats
    quiz_stats = await db.quiz_attempts.aggregate([
        {"$match": {"user_id": current_user.id, "is_completed": True}},
        {"$group": {
            "_id": None,
            "total_quizzes": {"$sum": 1},
            "average_score": {"$avg": "$percentage"}
        }}
    ]).to_list(1)

    # Get challenge stats
    challenge_stats = await db.challenge_attempts.aggregate([
        {"$match": {"user_id": current_user.id, "is_completed": True}},
        {"$group": {
            "_id": None,
            "total_challenges": {"$sum": 1},
            "average_score": {"$avg": "$best_score"}
        }}
    ]).to_list(1)

    return {
        "quiz_stats": quiz_stats[0] if quiz_stats else {"total_quizzes": 0, "average_score": 0},
        "challenge_stats": challenge_stats[0] if challenge_stats else {"total_challenges": 0, "average_score": 0},
        "total_points": current_user.progress.total_points,
        "level": current_user.progress.level,
        "badges_earned": len(current_user.progress.badges_earned)
    }
