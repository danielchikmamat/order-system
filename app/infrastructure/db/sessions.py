from sqlalchemy.orm import sessionmaker
from app.infrastructure.db.engine import engine

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

def get_db():
    """Dependency injection for database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Initialize database tables"""
    from app.infrastructure.db.base import Base
    Base.metadata.create_all(bind=engine)