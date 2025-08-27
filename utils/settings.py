import json
import os
import threading
from typing import Optional, Dict, Any

_DEFAULTS: Dict[str, Any] = {
    "user_name": None,
}

class Settings:
    def __init__(self, path: Optional[str] = None) -> None:
        if path is None:
            # project_root/settings.json (app.py is in cli/, so go up one)
            project_root = os.path.dirname(os.path.dirname(__file__))
            path = os.path.join(project_root, "data", "settings.json")
        self.path = path
        # Use a reentrant lock because set() acquires the lock and then calls save(),
        # which also needs to acquire the same lock. A normal Lock would deadlock.
        self._lock = threading.RLock()
        self._data: Dict[str, Any] = dict(_DEFAULTS)
        self._load()

    def _load(self) -> None:
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    self._data.update(data)
        except FileNotFoundError:
            pass  # first run
        except Exception:
            # If corrupted, ignore and keep defaults
            pass

    def save(self) -> None:
        with self._lock:
            os.makedirs(os.path.dirname(self.path), exist_ok=True)
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(self._data, f, indent=2)

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    def set(self, key: str, value: Any) -> None:
        with self._lock:
            self._data[key] = value
            self.save()

    @property
    def user_name(self) -> Optional[str]:
        return self.get("user_name")

    @user_name.setter
    def user_name(self, value: Optional[str]) -> None:
        self.set("user_name", value)