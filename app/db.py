from collections.abc import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from app.config import get_settings
from app.repositories.models import Base


settings = get_settings()

engine = create_engine(settings.database_url, pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def init_db() -> None:
    #if missing
    Base.metadata.create_all(bind=engine)

def get_db() -> Generator[Session, None, None]:
    # opens one db session per request
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
