from app.clients.openai_client import StudySummaryClient
from app.repositories.session_repository import SessionRepository

class SessionService:
    def __init__(self, repo: SessionRepository, summary_client: StudySummaryClient | None = None) -> None:
        self.repo = repo
        self.summary_client = summary_client

    def create_session(self, subject: str, duration_minutes: int, notes: str | None):
        subject = subject.strip().title()
        if not subject:
            raise ValueError("Subject cannot be empty.")
        if duration_minutes <= 0:
            raise ValueError("Duration must be greater than 0.")
        return self.repo.create(subject, duration_minutes, notes)

    def get_session(self, session_id: int):
        session = self.repo.get_by_id(session_id)
        if session is None:
            raise LookupError("Session not found.")
        return session

    def list_sessions(self):
        return self.repo.list_all()

    def get_stats(self) -> dict:
        sessions = self.repo.list_all()
        minutes_per_subject: dict[str, int] = {}
        for session in sessions:
            minutes_per_subject[session.subject] = minutes_per_subject.get(session.subject, 0) + session.duration_minutes

        return {
            "total_sessions": len(sessions),
            "total_minutes_studied": sum(session.duration_minutes for session in sessions),
            "minutes_per_subject": minutes_per_subject,
            "most_studied_subject": max(minutes_per_subject, key=minutes_per_subject.get) if minutes_per_subject else None,
        }

    def get_summary(self) -> str:
        if self.summary_client is None:
            raise RuntimeError("OPENAI_API_KEY is not configured.")
        sessions = self.repo.list_all()
        if not sessions:
            return "No study sessions have been recorded yet."

        stats = self.get_stats()
        lines = [f"Subject: {s.subject}, minutes: {s.duration_minutes}, notes: {s.notes or 'none'}" for s in sessions]
        prompt = (
            "Summarize this student's study history in 3 to 5 simple sentences.\n"
            f"Stats: {stats}\n"
            "Sessions:\n" + "\n".join(lines)
        )
        return self.summary_client.generate_summary(prompt)
