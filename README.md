# Aevyra DRF Backend

Django REST Framework backend for the Aevyra wellness platform.

## Features

- Public lead submission endpoint
- Staff-protected admin lead listing, detail, and patch endpoints
- Filtering, search, and ordering for leads
- SQLite by default for local development
- CORS enabled for the Next.js frontend

## API Endpoints

- `GET /api/leads/`
- `POST /api/leads/`
- `GET /api/leads/<uuid:id>/`
- `PATCH /api/leads/<uuid:id>/`

## Setup

```bash
cd /Users/bibhasingh/workspace/platform/django/aevyra_backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Frontend Connection

Set this in the frontend environment:

```bash
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000/api
```

## Notes

- `POST /api/leads/` is public
- `GET` and `PATCH` lead endpoints are staff-only
- Token auth is enabled for future admin API use
