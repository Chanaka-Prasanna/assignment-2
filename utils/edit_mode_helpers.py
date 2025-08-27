from datetime import date
from typing import Callable, TypeVar
from domain.errors import ValidationError
from utils.validation import choose_priority, parse_date
from utils.input_helpers import non_empty_factory

T = TypeVar("T")

def ask_edit(label: str, current, transform: Callable[[str], T]) -> T:
    while True:
        raw = input(f"{label} [{current}]: ")
        if raw.strip() == "":
            return current
        try:
            return transform(raw)
        except ValidationError as e:
            print(f"Error: {e}")

def ask_edit_text(label: str, current: str) -> str:
    return ask_edit(label, current, non_empty_factory(label))

def ask_edit_date(label: str, current: date) -> date:
    return ask_edit(f"{label} (YYYY-MM-DD)", current, parse_date)

def ask_edit_priority(current) -> "Priority":
    while True:
        raw = input(f"Priority [{current.value}] (low|medium|high or l/m/h): ").strip()
        if raw == "":
            return current
        try:
            return choose_priority(raw)
        except ValidationError as e:
            print(f"Error: {e}")