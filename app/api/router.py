from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.schemas import SessionCreateRequest, SessionResponse, StatsResponse, SummaryResponse
from app.clients.openai_client import StudySummaryClient
from app.config import get_settings
from app.db import get_db
from app.repositories.session_repository import SessionRepository
from app.services.session_service import SessionService

router = APIRouter()

def get_service(db: Session = Depends(get_db)) -> SessionService:
    settings = get_settings()
    summary_client = StudySummaryClient(settings.openai_api_key, settings.openai_model) if settings.openai_api_key else None
    return SessionService(SessionRepository(db), summary_client)

@router.post("/sessions", response_model=SessionResponse, status_code=status.HTTP_201_CREATED)
def create_session(payload: SessionCreateRequest, service: SessionService = Depends(get_service)):
    try:
        return service.create_session(payload.subject, payload.duration_minutes, payload.notes)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

@router.get("/sessions/{session_id}", response_model=SessionResponse)
def get_session(session_id: int, service: SessionService = Depends(get_service)):
    try:
        return service.get_session(session_id)
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc

@router.get("/sessions", response_model=list[SessionResponse])
def list_sessions(service: SessionService = Depends(get_service)):
    return service.list_sessions()

@router.get("/stats", response_model=StatsResponse)
def get_stats(service: SessionService = Depends(get_service)):
    return service.get_stats()

@router.get("/summary", response_model=SummaryResponse)
def get_summary(service: SessionService = Depends(get_service)):
    try:
        return {"summary": service.get_summary()}
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
