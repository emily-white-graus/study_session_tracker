from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

# validates create request body
class SessionCreateRequest(BaseModel):
    subject: str = Field(min_length=1, max_length=120)
    duration_minutes: int = Field(gt=0, le=720)
    notes: str | None = None

# shapes one session response
class SessionResponse(BaseModel):
    #pydantic read orm objects
    model_config = ConfigDict(from_attributes=True)
    id: int
    subject: str
    duration_minutes: int
    notes: str | None
    studied_at: datetime

# shapes stats response
class StatsResponse(BaseModel):
    total_sessions: int
    total_minutes_studied: int
    minutes_per_subject: dict[str, int]
    most_studied_subject: str | None

# shapes ai summary response
class SummaryResponse(BaseModel):
    summary: str
