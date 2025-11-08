# Backend (Flask)

This folder contains a minimal Flask backend used for local development.

Quick start (macOS / zsh):

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Endpoints:

- `GET /` — health check, returns JSON {"message": "Hello from backend (Flask)"}
- `POST /echo` — echoes the JSON body back as {"received": <body>} for easy testing

Notes:

- This is a development server. Use a production WSGI server (e.g. gunicorn) and proper configuration for deployments.
