import re
from datetime import date
from domain.models import Priority
from domain.errors import ValidationError

def choose_priority(s: str) -> Priority:
    s = s.lower().strip()
    mapping = {"l":"low","m":"medium","h":"high"}
    s = mapping.get(s, s)
    try: return Priority(s)
    except ValueError: raise ValidationError("Priority must be low|medium|high.")


def parse_date(s: str) -> date:
    s = (s or "").strip()
    if not s:
        raise ValidationError("Date is required in the form YYYY-MM-DD.")

    # Normalize separators to a dash
    normalized = re.sub(r"[/.]", "-", s)

    # Allow 1–2 digit months/days
    m = re.fullmatch(r"(\d{4})-(\d{1,2})-(\d{1,2})", normalized)
    if not m:
        raise ValidationError("Use date format YYYY-MM-DD, e.g., 2025-06-08.")

    y, mth, d = map(int, m.groups())

    # Range checks
    if not (1 <= mth <= 12):
        raise ValidationError("Month must be between 1 and 12.")
    if not (1 <= d <= 31):
        raise ValidationError("Day must be between 1 and 31.")

    # Validate real calendar date
    try:
        dt = date(y, mth, d)
    except ValueError:
        raise ValidationError("Invalid calendar date for the given month/year.")

    if dt < date.today():
        raise ValidationError("Due date cannot be earlier than today.")

    return dt
