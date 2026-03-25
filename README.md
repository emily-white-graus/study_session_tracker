# Study session tracker

Project built with fastapi and postgresql for tracking study sessions comfortably and tracking your study progress with stats.🤓☝

## Entity

### Studysession

A study session represents one study activity.

fields:

* `id` --> unique integer id
* `subject` --> subject studied
* `duration_minutes` --> duration of the session in minutes
* `notes` --> optional notes about the session
* `studied_at` --> timestamp of when the session was created

## API endpoints

### Create a study session

`POST /sessions`

example request body:

```json
{
  "subject": "math",
  "duration_minutes": 90,
  "notes": "practiced integrals"
}
```

---

### GET one study session by id

`GET /sessions/{id}`

---

### List all study sessions

`GET /sessions`

---

### GET study statistics

`GET /stats`

returns aggregated data:

* total sessions
* total minutes studied
* minutes per subject
* most studied subject

---

### Generate AI study summary

`GET /summary`

this endpoint uses the openai api to analyze stored study sessions and generate a summary of the user's study activity.

Example response:

```json
{
  "summary": "you studied a total of 5 hours this week, focusing mainly on math and programming. your most productive day was monday."
}
```

## AI feature

The `/summary` endpoint integrates with openai to:

* detect patterns in study habits
* generate human-readable summaries

## Also what is going to be used

* fastapi
* sqlalchemy
* postgresql
* openai api
* google cloud run
* google cloud sql