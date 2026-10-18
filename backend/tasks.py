import json
import random
from pathlib import Path 
from typing import Dict, List

TASKS_FILE = Path(__file__).resolve().parent / "tasks.json"
TASKS_PER_GAME = 4
REQUIRED_FIELDS = ("id", "icon", "label", "question", "answers", "hint", "explanation")

def _load_tasks() -> Dict[str, dict]:
    with TASKS_FILE.open(encoding="utf-8") as f:
        raw = json.load(f)

    tasks: Dict[str, dict] = {}
    for task in raw:
        missing = [k for k in REQUIRED_FIELDS if not task.get(k)]
        if missing:
            raise ValueError(f"Task {task.get('id', '?')} is missing {missing}")
        if task["id"] in tasks:
            raise ValueError(f"Duplicate task id {task['id']}")
        tasks[task["id"]] = task

    if len(tasks) < TASKS_PER_GAME:
        raise ValueError(f"Need at least {TASKS_PER_GAME} tasks, found {len(tasks)}")
    return tasks


TASKS = _load_tasks()


def pick_task_ids() -> List[str]:
    return random.sample(list(TASKS), TASKS_PER_GAME)


def public_task(task_id: str, solved: bool) -> dict:
    task = TASKS[task_id]
    return {
        "id": task_id,
        "icon": task["icon"],
        "label": task["label"],
        "question": task["question"],
        "solved": solved,
        "solution": {"answer": task["answers"][0], "explanation": task["explanation"]} if solved else None,
    }


