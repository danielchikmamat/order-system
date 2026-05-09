from sqlalchemy import create_engine
from app.core.config import Settings

settings = Settings()

engine = create_engine(
    settings.DATABASE_URL,
    echo=True,  # Set to False in production
    future=True,
)