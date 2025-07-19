from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import datetime
from enum import Enum
import uuid

class ChallengeDifficulty(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

class ChallengeCategory(str, Enum):
    ALGORITHMS = "algorithms"
    DATA_STRUCTURES = "data_structures"
    DYNAMIC_PROGRAMMING = "dynamic_programming"
    GRAPH_ALGORITHMS = "graph_algorithms"
    STRING_MANIPULATION = "string_manipulation"
    ARRAYS = "arrays"
    TREES = "trees"
    RECURSION = "recursion"

class TestCase(BaseModel):
    input: str
    expected_output: str
    is_hidden: bool = False

class Challenge(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    title: str
    description: str
    category: ChallengeCategory
    difficulty: ChallengeDifficulty
    test_cases: List[TestCase]
    starter_code: Optional[str] = None
    solution_code: Optional[str] = None
    points: int = 100
    time_limit: Optional[int] = 3600  # in seconds, default 1 hour
    memory_limit: Optional[int] = 256  # in MB
    allowed_languages: List[str] = ["python", "javascript", "java", "cpp"]
    tags: List[str] = []
    is_active: bool = True
    created_by: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True

class ChallengeSubmission(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    user_id: str
    challenge_id: str
    code: str
    language: str
    status: str = "pending"  # pending, running, passed, failed, error
    score: Optional[int] = None
    execution_time: Optional[float] = None  # in seconds
    memory_used: Optional[float] = None  # in MB
    test_results: List[Dict] = []
    error_message: Optional[str] = None
    submitted_at: datetime = Field(default_factory=datetime.utcnow)
    evaluated_at: Optional[datetime] = None

    class Config:
        populate_by_name = True

class ChallengeAttempt(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    user_id: str
    challenge_id: str
    submissions: List[str] = []  # submission ids
    best_score: Optional[int] = None
    is_completed: bool = False
    started_at: datetime = Field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = None

    class Config:
        populate_by_name = True

class ChallengeCreate(BaseModel):
    title: str
    description: str
    category: ChallengeCategory
    difficulty: ChallengeDifficulty
    test_cases: List[TestCase]
    starter_code: Optional[str] = None
    solution_code: Optional[str] = None
    points: int = 100
    time_limit: Optional[int] = 3600
    memory_limit: Optional[int] = 256
    allowed_languages: List[str] = ["python", "javascript", "java", "cpp"]
    tags: List[str] = []

class ChallengeUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    test_cases: Optional[List[TestCase]] = None
    starter_code: Optional[str] = None
    solution_code: Optional[str] = None
    points: Optional[int] = None
    time_limit: Optional[int] = None
    memory_limit: Optional[int] = None
    allowed_languages: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    is_active: Optional[bool] = None

class SubmissionCreate(BaseModel):
    challenge_id: str
    code: str
    language: str
