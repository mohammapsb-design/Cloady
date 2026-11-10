# My First Cloud API

A tiny Python API built with FastAPI.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://127.0.0.1:8000

## Endpoints

- `/` — welcome message
- `/time` — current UTC time
- `/health` — health status

## Deploy

For Cloady, connect this GitHub repository. Leave Build Command blank.
Set the Start Command to:

```bash
uvicorn main:app --host 0.0.0.0 --port ${PORT:-3000}
```
