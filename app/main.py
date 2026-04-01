from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.api.router import router
from app.db import init_db

#builds app
app = FastAPI(title="Study Session Tracker")

#api routes
app.include_router(router)
# serves frontend files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.on_event("startup")
def startup() -> None:
    # creates tables on startup
    init_db()

@app.get("/", include_in_schema=False)
def index():
    # serves main frontend page
    return FileResponse("app/static/index.html")

@app.get("/health")
def health() -> dict[str, str]:
    # status
    return {"status": "ok"}
