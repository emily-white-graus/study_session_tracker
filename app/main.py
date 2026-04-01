from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.api.router import router
from app.db import init_db

app = FastAPI(title="Study Session Tracker")

app.include_router(router)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.on_event("startup")
def startup() -> None:
    init_db()

@app.get("/", include_in_schema=False)
def index():
    return FileResponse("app/static/index.html")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
