import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import TypeVar
from domain.errors import ValidationError, NotFoundError
from services.task_service import TaskService
from infra.json_repository import JSONTaskRepository
from utils.settings import Settings
from utils.create_mode_helpers import ask_new_text,ask_new_date,ask_new_priority
from utils.edit_mode_helpers import ask_edit_text,ask_edit_date,ask_edit_priority,ask_edit_status
from utils.console_helpers import render_home,print_menu_header
T = TypeVar("T")


def main():
    settings = Settings()
    svc = TaskService(JSONTaskRepository())

    if not settings.user_name:
        name = input("Welcome! What's your name? ").strip() or "Friend"
        settings.user_name = name

    # Show welcome splash once
    render_home(svc,settings.user_name)

    while True:
        choice = input("> ").strip()
        try:
            if choice == "1":
                # --- ADD (using your helpers) ---
                title = ask_new_text("Title")
                desc = ask_new_text("Description")
                due = ask_new_date("Due date")
                pr = ask_new_priority(default="medium")

                t = svc.add(title, desc, due, pr)
                print(f"Created {t.id} ✓")
                print_menu_header()  # remind options after action

            elif choice == "2":
                for t in svc.list():
                    print(f"{t.id} | {t.title} | due {t.due_date} | {t.priority.value} | {t.status.value}")
                print_menu_header()

            elif choice == "3":
                tid = input("Task ID: ")
                t = svc.get(tid)
                print(
                    f"\n{t.id}\nTitle: {t.title}\nDesc: {t.description}\nDue: {t.due_date}\n"
                    f"Priority: {t.priority.value}\nStatus: {t.status.value}"
                )
                print_menu_header()

            elif choice == "4":
                tid = input("Task ID: ")
                t = svc.get(tid)

                new_title = ask_edit_text("Title", t.title)

                desc_preview = (t.description if len(t.description) <= 40 else t.description[:40] + "…")
                new_desc = ask_edit_text(f"Description (current: {desc_preview})", t.description)
                new_due = ask_edit_date("Due", t.due_date)
                new_pr = ask_edit_priority(t.priority)
                new_status = ask_edit_status(t.status)

                svc.update(
                    tid,
                    title=new_title,
                    description=new_desc,
                    due_date=new_due,
                    priority=new_pr,
                    status=new_status,
                )
                print("Updated ✓")
                print_menu_header()

            elif choice == "5":
                tid = input("Task ID: ")
                svc.delete(tid)
                print("Deleted ✓")
                print_menu_header()

            elif choice == "6":
                for t in svc.sort_by_due_date():
                    print(f"{t.due_date} | {t.title} ({t.priority.value})")
                print_menu_header()

            elif choice == "7":
                current_name = settings.user_name or "Friend"
                print(f"Current name: {current_name}")
                new_name = input("Enter new name (or press Enter to keep current): ").strip()
                if new_name:
                    settings.user_name = new_name
                    print(f"Name changed to: {new_name} ✓")
                else:
                    print("Name unchanged.")
                print_menu_header()

            elif choice == "0":
                print("Bye!")
                break

            else:
                print("Invalid option. Try 0–7.")
                print_menu_header()

        except (ValidationError, NotFoundError) as e:
            print(f"Error: {e}")
            print_menu_header()


if __name__ == "__main__":
    main()