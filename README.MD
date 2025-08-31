# TaskMate Task Tracker

A simple, menu-driven console app to manage tasks (title, description, due date, priority, status) with JSON persistence.

## Project Description

TaskMate Task Tracker is a comprehensive command-line task management application designed to help users organize and track their tasks efficiently. The application provides a user-friendly interface with robust features for task management.

### What the Application Does

- **Task Management**: Create, view, update, and delete tasks with detailed information
- **Smart Organization**: Sort tasks by due date to prioritize upcoming deadlines
- **User Personalization**: Customize the interface with your name for a personalized experience
- **Data Persistence**: All tasks and settings are automatically saved to JSON files
- **Input Validation**: Ensures data integrity with comprehensive validation rules

### Technologies Used

- **Python 3.10+**: Core programming language for robust performance and modern features
- **JSON**: Lightweight data storage format for easy data management
- **Colorama**: Enhanced terminal interface with colors for better user experience
- **Object-Oriented Design**: Clean architecture with separation of concerns

### Key Features Implemented

- **Quit Operations**: Press 'q' at any time to cancel current operations
- **Colorful UI**: Enhanced terminal interface with colors (requires colorama)
- **Task Counter**: Real-time display of loaded tasks in the header
- **Input Validation**: Comprehensive validation for dates, priorities, and required fields
- **Persistent Settings**: User preferences are saved between sessions

### Future Enhancements

- Database integration for better scalability
- Task categories and tags
- Export functionality (CSV, PDF)
- Reminder notifications
- Multi-user support

## Table of Contents

- [Project Description](#project-description)
- [Installation and Setup](#installation-and-setup)
- [How to Use](#how-to-use)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Installation and Setup

### Prerequisites

- Python 3.10+
- Optional: color output via the colorama package

### Step-by-Step Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Chanaka-Prasanna/assignment-2.git
   ```

2. **Install Dependencies (optional but recommended)**

   ```bash
   # Install colorama for enhanced UI
   pip install colorama
   ```

3. **Run the Application**

   ```bash
   # Run from the project root (where cli/, domain/, ... exist)
   python -m cli.app

   # Or navigate to cli folder and run:
   cd cli
   python app.py
   ```

## How to Use

### Getting Started

When you first run the application, you'll be prompted to enter your name. This will be used for personalized greetings in future sessions.

### Main Interface

You'll see a colorful menu-driven interface. Example session:

```text
╔══════════════════════════════════════════════════════════════════════════════╗
║                           TaskMate Task Tracker                             ║
║                    Good afternoon Chanaka! 3 tasks loaded                   ║
╚══════════════════════════════════════════════════════════════════════════════╝

────────────────────────────────────────────────────────────────────────────────
                1) Add  2) List  3) View  4) Update  5) Delete  6) Sort 7) Change name  0) Quit
────────────────────────────────────────────────────────────────────────────────
What would you like to do? (Choose 0-7): 1
Press 'q' at any time to cancel this operation.
Title: Plan sprint
Description: Prepare sprint backlog
Due date (YYYY-MM-DD): 2025-09-05
Priority [low(l) | medium(m) | high(h)] (default=medium): high
Created 6b3a... ✓

────────────────────────────────────────────────────────────────────────────────
                1) Add  2) List  3) View  4) Update  5) Delete  6) Sort 7) Change name  0) Quit
────────────────────────────────────────────────────────────────────────────────
What would you like to do? (Choose 0-7): 2
6b3a... | Plan sprint | due 2025-09-05 | high | todo

────────────────────────────────────────────────────────────────────────────────
                1) Add  2) List  3) View  4) Update  5) Delete  6) Sort 7) Change name  0) Quit
────────────────────────────────────────────────────────────────────────────────
What would you like to do? (Choose 0-7): 0
Bye!
```

### Available Commands

- **1 Add**: Create a new task with validated Title, Description, Due date, and Priority
- **2 List**: Display all tasks in a concise format
- **3 View**: Enter a Task ID to see detailed information
- **4 Update**: Modify existing tasks (press Enter to keep current values)
- **5 Delete**: Remove tasks by entering their Task ID
- **6 Sort**: Display tasks ordered by due date (earliest first)
- **7 Change name**: Update your personalized greeting name
- **0 Quit**: Exit the application

### Tips for Better Usage

- **Press 'q'** at any time during input operations to cancel and return to the main menu
- **Date Format**: Use YYYY-MM-DD format for due dates (e.g., 2025-09-05)
- **Priority Options**: Choose from low, medium, or high (or use l, m, h shortcuts)
- **Task IDs**: Use the first few characters of the task ID for quick reference

## Project Structure

```
taskmate-task-tracker/
├── cli/                    # CLI entry point and main application loop
│   └── app.py
├── data/                   # Application data storage
│   ├── settings.json       # User preferences and settings
│   └── tasks.json          # Task data (auto-created if missing)
├── domain/                 # Core business logic and models
│   ├── errors.py           # Custom exception classes
│   └── models.py           # Task and data models
├── infra/                  # Data persistence layer
│   └── json_repository.py  # JSON-based data storage implementation
├── services/               # Business logic services
│   └── task_service.py     # Task management business logic
├── utils/                  # Utility functions and helpers
│   ├── console_helpers.py  # UI rendering and display functions
│   ├── create_mode_helpers.py  # Task creation input helpers
│   ├── edit_mode_helpers.py    # Task editing input helpers
│   ├── input_helpers.py    # Input validation and processing
│   ├── io.py              # Input/output utilities
│   ├── settings.py        # Settings management
│   └── validation.py      # Data validation functions
└── README.md
```

## Troubleshooting

### Common Issues and Solutions

**Box/Border Characters Display Incorrectly**

- **Solution**: Use Windows Terminal with a UTF-8 font (Consolas/Cascadia)
- **Alternative**: Install colorama package for better compatibility

**Import Errors**

- **Cause**: Running from wrong directory
- **Solution**: Ensure you run from the project root directory
- **Windows PowerShell**: Use `py -m cli.app` for better compatibility

**Data File Issues**

- **Cause**: Incorrect file paths or permissions
- **Solution**: Run the app from the project root to keep data files in the `data/` folder
- **Note**: The app automatically creates data files if they don't exist

### Performance Tips

- Install colorama for enhanced visual experience
- Use Windows Terminal for better Unicode support
- Keep the application updated for latest features and bug fixes

**TaskMate Task Tracker** - Making task management simple and efficient!
