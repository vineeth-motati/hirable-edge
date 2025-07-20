from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.core.auth import authenticate_user, create_access_token, get_password_hash
from app.core.config import settings
from app.core.database import get_database
from app.models.user import User, UserCreate, UserLogin, UserResponse
from pydantic import BaseModel
from datetime import datetime, timezone

router = APIRouter()

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str = None

@router.post("/register", response_model=UserResponse)
async def register_user(user: UserCreate, db = Depends(get_database)):
    """Register a new user"""
    # Check if user already exists
    existing_user = await db.users.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # Create new user
    hashed_password = get_password_hash(user.password)

    new_user = User(
        email=user.email,
        hashed_password=hashed_password,
        profile={
            "first_name": user.first_name,
            "last_name": user.last_name,
            "university": user.university,
            "major": user.major
        }
    )

    # Insert user into database
    user_dict = new_user.dict(by_alias=True)
    result = await db.users.insert_one(user_dict)

    # Fetch the created user
    created_user = await db.users.find_one({"_id": result.inserted_id})
    return UserResponse(**created_user)

@router.post("/login", response_model=Token)
async def login_user(user: UserLogin, db = Depends(get_database)):
    """Login user and return access token"""
    authenticated_user = await authenticate_user(user.email, user.password, db)

    if not authenticated_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": authenticated_user.email},
        expires_delta=access_token_expires
    )

    # Update last login
    await db.users.update_one(
        {"_id": authenticated_user.id},
        {"$set": {"last_login": datetime.now(timezone.utc)}}
    )

    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db = Depends(get_database)
):
    """OAuth2 compatible token endpoint"""
    authenticated_user = await authenticate_user(form_data.username, form_data.password, db)

    if not authenticated_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": authenticated_user.email},
        expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}
