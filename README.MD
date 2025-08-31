# TaskMate Task Tracker

A simple, menu-driven console app to manage tasks (title, description, due date, priority, status) with JSON persistence.

## Table of Contents

- Quick start
- Features
- Usage (with examples)
- Data and configuration
- Project structure
- Troubleshooting

## Quick start

Prerequisites

- Python 3.10+
- Optional: color output via the colorama package

Set up (Windows PowerShell)

```powershell

# (optional) install color for the header
pip install colorama

# run from the project root (where cli/, domain/, ... exist)
python -m cli.app
```

## Features

- Add, list, view, update, and delete tasks
- Sort tasks by due date (soonest first)
- Menu-driven CLI with validation and friendly errors
- JSON persistence on disk
- Input validation: non-empty title/description, YYYY-MM-DD dates, no past due dates

## Usage

You’ll see a menu and can type an option number. Example session:

```text
============================
 TaskMate Task Tracker
============================
Hi, Friend! What would you like to do?

[1] Add  [2] List  [3] View  [4] Update  [5] Delete  [6] Sort  [7] Name  [0] Quit
> 1
Title: Plan sprint
Description: Prepare sprint backlog
Due date (YYYY-MM-DD): 2025-09-05
Priority [low|medium|high] (default: medium): high
Created 6b3a... ✓

[1] Add  [2] List  [3] View  [4] Update  [5] Delete  [6] Sort  [7] Name  [0] Quit
> 2
6b3a... | Plan sprint | due 2025-09-05 | high | todo

[1] Add  [2] List  [3] View  [4] Update  [5] Delete  [6] Sort  [7] Name  [0] Quit
> 0
Bye!
```

Commands at a glance

- 1 Add: prompts for validated Title, Description, Due date, Priority
- 2 List: shows all tasks in brief form
- 3 View: enter a Task ID to see details
- 4 Update: press Enter to keep current values or provide new ones
- 5 Delete: enter a Task ID to remove it
- 6 Sort: prints tasks ordered by due date
- 7 Name: change the saved greeting name
- 0 Quit: exit the app

## Data and configuration

- Settings file: `data/settings.json` (stores the friendly greeting name)
- Tasks file: `data/tasks.json` (created automatically if missing)
- The storage path is defined in `infra/json_repository.py` via `JSONTaskRepository(path=...)`. You can customize it if you want to store tasks elsewhere.

Note: Run the app from the project root to keep data files under the `data/` folder.

## Project structure

```text
cli/                # CLI entry point and loop
	app.py
data/               # App data (persisted settings & tasks)
	settings.json
	tasks.json
domain/             # Core models and domain errors
	errors.py
	models.py
infra/              # Persistence implementation (JSON repository)
	json_repository.py
services/           # Business logic
	task_service.py
utils/              # Console + input helpers, validation, settings loader
	console_helpers.py
	create_mode_helpers.py
	edit_mode_helpers.py
	input_helpers.py
	io.py
	settings.py
	validation.py
README.MD
```

## Troubleshooting

- If box/border characters look odd on Windows, try Windows Terminal and a UTF‑8 font (Consolas/Cascadia). Installing colorama can also help.
- If imports fail, ensure you run from the project root. On Windows PowerShell, prefer `py -m cli.app`.
