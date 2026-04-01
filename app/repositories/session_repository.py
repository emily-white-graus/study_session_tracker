from sqlalchemy import select
from sqlalchemy.orm import Session
from app.repositories.models import StudySessionORM

class SessionRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, subject: str, duration_minutes: int, notes: str | None) -> StudySessionORM:
        session = StudySessionORM(subject=subject, duration_minutes=duration_minutes, notes=notes)
        self.db.add(session)
        self.db.commit()
        self.db.refresh(session)
        return session

    def get_by_id(self, session_id: int) -> StudySessionORM | None:
        return self.db.get(StudySessionORM, session_id)

    def list_all(self) -> list[StudySessionORM]:
        stmt = select(StudySessionORM).order_by(StudySessionORM.studied_at.desc())
        return list(self.db.scalars(stmt))
