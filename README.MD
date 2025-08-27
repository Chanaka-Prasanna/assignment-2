# TaskMate Task Tracker

A simple, menu-driven console app to manage tasks with title, description, and due date. Tasks persist between runs via a JSON file.

## Features (as required)
- Add / List / View / Update / Delete tasks
- Sort tasks by due date
- Menu-driven CLI with graceful error handling
- Data persistence to a JSON file (tasks.json)
- Input validation: non-empty title/description, date format YYYY-MM-DD, due date cannot be in the past

## Quick Start
Requirements: Python 3.10+ (no mandatory third-party packages)

Optional (for colored header): install colorama
$ pip install colorama

Run from the project root (where cli/, domain/, services/, infra/, utils/ exist):
macOS/Linux:
$ export PYTHONPATH=.
$ python -m cli.app

Windows (PowerShell):
> $env:PYTHONPATH="."
> python -m cli.app

## Usage
You’ll see the menu:
1) Add  2) List  3) View  4) Update  5) Delete  6) Sort  0) Quit

Add: prompts for Title, Description, Due date (re-prompts until valid)
List: shows all tasks
View: enter a Task ID to see details
Update: shows current values in brackets; press ENTER to keep, or type a new (validated) value
Delete: enter a Task ID to remove it
Sort: prints tasks ordered by due date (soonest first)
Quit: exits the app

## Data & Files
- Tasks are saved to tasks.json in the project root (created automatically).
- To change the path, pass a different filename to JSONTaskRepository in cli/app.py.

## Project Structure (brief)
- cli/app.py                - CLI (menus & prompts)
- domain/models.py          - Task dataclass and enums (core model)
- domain/errors.py          - ValidationError, NotFoundError
- services/task_service.py  - Business logic and validations
- infra/json_repository.py  - JSON file I/O (persistence)
- utils/create_mode_helpers.py - Input helpers for Add flow
- utils/edit_mode_helpers.py   - Input helpers for Update flow
- utils/validation.py          - choose_priority, parse_date, shared validators

## Optional Enhancements (implemented, not required by spec)
- Priority and Status fields with sensible defaults; ENTER to keep on update
- Branded console header (TaskMate Task Tracker) with greeting; optional colors via colorama
- Reusable input helper functions for consistent UX and less duplication

## Troubleshooting
- If borders or box characters look odd on Windows, use Windows Terminal and a UTF-8 font (Consolas/Cascadia), or rely on ASCII borders; installing colorama often helps.
- If imports fail, ensure you run from the project root and set PYTHONPATH as shown above.
