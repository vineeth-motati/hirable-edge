from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
from app.api.routes import auth, users, quizzes, challenges, interviews, resume, roadmap, tutor, achievements
from app.core.database import connect_to_mongo, close_mongo_connection
from app.core.auth import get_current_user

security = HTTPBearer()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await connect_to_mongo()
    yield
    # Shutdown
    await close_mongo_connection()

app = FastAPI(
    title="HirableEdge API",
    description="A comprehensive platform to help students improve their job hirability",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],  # Frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(quizzes.router, prefix="/api/quizzes", tags=["Quizzes"])
app.include_router(challenges.router, prefix="/api/challenges", tags=["Coding Challenges"])
app.include_router(interviews.router, prefix="/api/interviews", tags=["Mock Interviews"])
app.include_router(resume.router, prefix="/api/resume", tags=["Resume Builder"])
app.include_router(roadmap.router, prefix="/api/roadmap", tags=["Career Roadmap"])
app.include_router(tutor.router, prefix="/api/tutor", tags=["AI Tutor"])
app.include_router(achievements.router, prefix="/api/achievements", tags=["Achievements"])

@app.get("/")
async def root():
    return {"message": "Welcome to HirableEdge API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
