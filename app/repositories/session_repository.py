from sqlalchemy import select
from sqlalchemy.orm import Session
from app.repositories.models import StudySessionORM

# handles db queries
class SessionRepository:
    def __init__(self, db: Session) -> None:
        #stores active db session
        self.db = db

    def create(self, subject: str, duration_minutes: int, notes: str | None) -> StudySessionORM:
        #inserts new session row
        session = StudySessionORM(subject=subject, duration_minutes=duration_minutes, notes=notes)
        self.db.add(session)
        self.db.commit()
        self.db.refresh(session)
        return session

    def get_by_id(self, session_id: int) -> StudySessionORM | None:
        # fetches one session
        return self.db.get(StudySessionORM, session_id)

    def list_all(self) -> list[StudySessionORM]:
        # fetches all sessions newest first
        stmt = select(StudySessionORM).order_by(StudySessionORM.studied_at.desc())
        return list(self.db.scalars(stmt))
