from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    # Database settings
    mongodb_url: str = "mongodb://localhost:27017"
    database_name: str = "hirableedge"

    # JWT settings
    secret_key: str = "your-secret-key-change-this-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # OpenAI API settings
    openai_api_key: Optional[str] = None

    # App settings
    app_name: str = "HirableEdge"
    debug: bool = True

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
