from typing import List, Optional
from uuid import uuid4
from datetime import date
from domain.models import Task, Priority, Status
from domain.errors import ValidationError, NotFoundError

class TaskService:
    def __init__(self, repo):
        self.repo = repo
        self._cache = repo.load()

    def list(self) -> List[Task]:
        return self._cache.copy()

    def get(self, task_id: str) -> Task:
        for t in self._cache:
            if t.id == task_id: return t
        raise NotFoundError(f"No task with id {task_id}")

    def add(self, title: str, description: str, due_date: date,
            priority: Priority = Priority.MEDIUM) -> Task:
        title = title.strip()
        if not title:
            raise ValidationError("Title cannot be empty.")
        if due_date < date.today():
            raise ValidationError("Due date cannot be in the past.")
        task = Task(id=str(uuid4()), title=title,
                    description=description.strip(), due_date=due_date,
                    priority=priority)
        self._cache.append(task)
        self.repo.save(self._cache)
        return task

    def update(self, task_id: str, **fields) -> Task:
        t = self.get(task_id)
        if "title" in fields and not fields["title"].strip():
            raise ValidationError("Title cannot be empty.")
        if "due_date" in fields and fields["due_date"] < date.today():
            raise ValidationError("Due date cannot be in the past.")
        updated = t.with_updates(**fields)
        self._cache = [updated if x.id == task_id else x for x in self._cache]
        self.repo.save(self._cache)
        return updated

    def delete(self, task_id: str) -> None:
        _ = self.get(task_id)
        self._cache = [x for x in self._cache if x.id != task_id]
        self.repo.save(self._cache)

    def sort_by_due_date(self) -> List[Task]:
        return sorted(self._cache, key=lambda t: t.due_date)
