# Study session tracker

Project built with fastapi and postgresql for tracking study sessions comfortably and tracking your study progress with stats.🤓☝


## What it does

- create study sessions
- store sessions in PostgreSQL
- list saved sessions
- calculate study statistics
- generate an AI summary with OpenAI
- serve a small web interface from the backend

## Tech stack

- FastAPI
- SQLAlchemy
- PostgreSQL
- OpenAI API
- Docker
- Google Cloud Run
- Google Cloud SQL

## Project structure

```text
app/
  api/
    router.py
    schemas.py
  clients/
    openai_client.py
  repositories/
    models.py
    session_repository.py
  services/
    session_service.py
  static/
    index.html
  config.py
  db.py
  main.py
```

## Main features

### Study session

Each study session has:

- `id`
- `subject`
- `duration_minutes`
- `notes`
- `studied_at`

### API endpoints

- `POST /sessions`
- `GET /sessions`
- `GET /sessions/{session_id}`
- `GET /stats`
- `GET /summary`

## Example request

`POST /sessions`

```json
{
  "subject": "math",
  "duration_minutes": 90,
  "notes": "practiced integrals"
}
```

## Example summary response

```json
{
  "summary": "The student completed 4 study sessions totaling 230 minutes."
}
```

## Run locally

1. create a virtual environment
2. install dependencies
3. add your environment variables
4. start the server

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Open:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/docs`

## Environment variables

Create a `.env` file with:

```env
DATABASE_URL=your_database_url
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-5-mini
```

## Docker

Build and run with:

```bash
docker build -t study-session-tracker .
docker run --env-file .env -p 8080:8080 study-session-tracker
```

## Deployment

This project is deployed on:

- Google Cloud Run
- Google Cloud SQL

## Notes

- the frontend is a static HTML page served by FastAPI
- the backend handles the API, logic, database access, and AI summary
- the `/summary` endpoint depends on a valid OpenAI API key
