from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(title="My First Cloud API")


@app.get("/")
def home():
    return {"message": "Hello from my server!"}


@app.get("/time")
def get_time():
    return {"utc_time": datetime.now(timezone.utc).isoformat()}


@app.get("/health")
def health():
    return {"status": "ok"}
