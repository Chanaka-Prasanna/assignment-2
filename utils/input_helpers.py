from typing import Callable, TypeVar
from domain.errors import ValidationError

T = TypeVar("T")

def ask_until_valid(prompt: str, transform: Callable[[str], T]) -> T:
    """Keep asking until transform(value) succeeds (no ValidationError)."""
    while True:
        try:
            return transform(input(prompt))
        except ValidationError as e:
            print(f"Error: {e}")

def non_empty_factory(field_name: str) -> Callable[[str], str]:
    """Validator factory for required non-empty text."""
    def _v(s: str) -> str:
        s = (s or "").strip()
        if not s:
            raise ValidationError(f"{field_name} cannot be empty.")
        return s
    return _v