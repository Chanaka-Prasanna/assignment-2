import json, os, tempfile
from typing import List
from datetime import date
from domain.models import Task, Priority, Status

class JSONTaskRepository:
    def __init__(self, path: str = "../data/tasks.json"):
        self.path = path

    def load(self) -> List[Task]:
        if not os.path.exists(self.path):
            return []
        with open(self.path, "r", encoding="utf-8") as f:
            raw = json.load(f)
        tasks = []
        for r in raw:
            tasks.append(Task(
                id=r["id"],
                title=r["title"],
                description=r.get("description", ""),
                due_date=date.fromisoformat(r["due_date"]),
                priority=Priority(r.get("priority","medium")),
                status=Status(r.get("status","todo")),
                created_on=date.fromisoformat(r.get("created_on", r["due_date"]))
            ))
        return tasks

    def save(self, tasks: List[Task]) -> None:
        data = [dict(
            id=t.id,
            title=t.title,
            description=t.description,
            due_date=t.due_date.isoformat(),
            priority=t.priority.value, status=t.status.value,
            created_on=t.created_on.isoformat()
        ) for t in tasks]
        d = os.path.dirname(self.path) or "."
        fd, tmp = tempfile.mkstemp(dir=d, suffix=".tmp")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        os.replace(tmp, self.path)



