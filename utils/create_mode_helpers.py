from datetime import date
from typing import TypeVar
from utils.validation import choose_priority, parse_date
from utils.input_helpers import ask_until_valid,non_empty_factory

T = TypeVar("T")

def ask_new_text(label: str) -> str:
    return ask_until_valid(f"{label}: ", non_empty_factory(label))

def ask_new_date(label: str) -> date:
    # parse_date already checks format and not-in-the-past
    return ask_until_valid(f"{label} (YYYY-MM-DD): ", parse_date)

def ask_new_priority(default: str = "medium"):
    def _p(s: str):
        s = (s or default).strip()
        return choose_priority(s)
    return ask_until_valid(
        f"Priority [low(l) | medium(m) | high(h)] (default={default}): ", _p
    )