"""ROOM 13 — FastAPI backend."""

from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from tasks import pick_task_ids, public_task

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"

app = FastAPI(title="ROOM 13 API", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/api/game/new")
def health() -> dict:
    """Pick 4 random tasks. Progress is tracked in the browser."""
    return {"tasks": [public_task(tid, False) for tid in pick_task_ids()]}

# ── Static frontend (mount last so /api routes take priority) ──

app.mount("/", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="frontend")

