from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime
from enum import Enum
import uuid

class UserRole(str, Enum):
    STUDENT = "student"
    ADMIN = "admin"

class UserProfile(BaseModel):
    first_name: str
    last_name: str
    phone: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    university: Optional[str] = None
    major: Optional[str] = None
    graduation_year: Optional[int] = None
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    portfolio_url: Optional[str] = None

class UserSkills(BaseModel):
    technical_skills: List[str] = []
    soft_skills: List[str] = []
    languages: List[str] = []
    certifications: List[str] = []

class UserGoals(BaseModel):
    target_roles: List[str] = []
    target_companies: List[str] = []
    career_level: Optional[str] = None
    preferred_locations: List[str] = []
    salary_expectation: Optional[str] = None

class UserProgress(BaseModel):
    total_quizzes_taken: int = 0
    total_challenges_completed: int = 0
    total_interviews_completed: int = 0
    badges_earned: List[str] = []
    total_points: int = 0
    level: int = 1

class User(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    email: EmailStr
    hashed_password: str
    role: UserRole = UserRole.STUDENT
    is_active: bool = True
    is_verified: bool = False
    profile: UserProfile
    skills: UserSkills = Field(default_factory=UserSkills)
    goals: UserGoals = Field(default_factory=UserGoals)
    progress: UserProgress = Field(default_factory=UserProgress)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    last_login: Optional[datetime] = None

    class Config:
        populate_by_name = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    university: Optional[str] = None
    major: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: str = Field(alias="_id")
    email: EmailStr
    role: UserRole
    is_active: bool
    is_verified: bool
    profile: UserProfile
    skills: UserSkills
    goals: UserGoals
    progress: UserProgress
    created_at: datetime
    updated_at: datetime
    last_login: Optional[datetime] = None

    class Config:
        populate_by_name = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class UserUpdate(BaseModel):
    profile: Optional[UserProfile] = None
    skills: Optional[UserSkills] = None
    goals: Optional[UserGoals] = None
