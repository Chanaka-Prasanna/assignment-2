from dataclasses import dataclass, field
from enum import Enum
from datetime import date
from uuid import uuid4


class Priority(Enum):
    LOW    = "low"
    MEDIUM = "medium"
    HIGH   = "high"

class Status(Enum):
    TODO  = "todo"
    DOING = "doing"
    DONE  = "done"

@dataclass(frozen=True)
class Task:
    id: str
    title: str
    description: str
    due_date: date
    priority: Priority = Priority.MEDIUM
    status: Status = Status.TODO
    created_on: date = field(default_factory=date.today)

    def with_updates(self, **changes) -> "Task":
        return dataclass_replace(self, **changes)

from dataclasses import replace as dataclass_replace

