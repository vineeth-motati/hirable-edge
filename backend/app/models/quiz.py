from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import datetime
from enum import Enum
import uuid

class QuizCategory(str, Enum):
    TECHNICAL = "technical"
    BEHAVIORAL = "behavioral"
    APTITUDE = "aptitude"
    DOMAIN_SPECIFIC = "domain_specific"

class QuizDifficulty(str, Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

class QuestionType(str, Enum):
    MULTIPLE_CHOICE = "multiple_choice"
    TRUE_FALSE = "true_false"
    SINGLE_CHOICE = "single_choice"

class QuizQuestion(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    question_text: str
    question_type: QuestionType
    options: List[str] = []
    correct_answer: str
    explanation: Optional[str] = None
    points: int = 1
    time_limit: Optional[int] = 60  # seconds

class Quiz(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    title: str
    description: str
    category: QuizCategory
    difficulty: QuizDifficulty
    questions: List[QuizQuestion]
    total_points: int
    time_limit: int = 1800  # 30 minutes default
    passing_score: int = 70  # percentage
    tags: List[str] = []
    is_active: bool = True
    created_by: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True

class QuizAttempt(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    user_id: str
    quiz_id: str
    answers: Dict[str, str] = {}  # question_id -> answer
    score: Optional[int] = None
    percentage: Optional[float] = None
    is_completed: bool = False
    is_passed: bool = False
    time_taken: Optional[int] = None  # seconds
    started_at: datetime = Field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = None

    class Config:
        populate_by_name = True

class QuizCreate(BaseModel):
    title: str
    description: str
    category: QuizCategory
    difficulty: QuizDifficulty
    questions: List[QuizQuestion]
    time_limit: int = 1800
    passing_score: int = 70
    tags: List[str] = []

class QuizUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    questions: Optional[List[QuizQuestion]] = None
    time_limit: Optional[int] = None
    passing_score: Optional[int] = None
    tags: Optional[List[str]] = None
    is_active: Optional[bool] = None

class QuizSubmission(BaseModel):
    quiz_id: str
    answers: Dict[str, str]

class QuizResponse(BaseModel):
    id: str = Field(alias="_id")
    title: str
    description: str
    category: QuizCategory
    difficulty: QuizDifficulty
    questions: List[QuizQuestion]
    total_points: int
    time_limit: int
    passing_score: int
    tags: List[str]
    is_active: bool
    created_at: datetime

    class Config:
        populate_by_name = True
