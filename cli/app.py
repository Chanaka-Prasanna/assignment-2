from typing import TypeVar
from domain.errors import ValidationError, NotFoundError
from services.task_service import TaskService
from infra.json_repository import JSONTaskRepository
from utils.create_mode_helpers import ask_new_text,ask_new_date,ask_new_priority
from utils.edit_mode_helpers import ask_edit_text,ask_edit_date,ask_edit_priority

T = TypeVar("T")


def main():
    svc = TaskService(JSONTaskRepository())

    while True:
        print("\n1) Add  2) List  3) View  4) Update  5) Delete  6) Sort  0) Quit")
        choice = input("> ").strip()
        try:
            if choice == "1":
                # --- ADD (now using same helpers as update) ---
                title = ask_new_text("Title")
                desc  = ask_new_text("Description")
                due   = ask_new_date("Due date")
                pr    = ask_new_priority(default="medium")

                t = svc.add(title, desc, due, pr)
                print(f"Created {t.id} ✓")

            elif choice == "2":
                for t in svc.list():
                    print(f"{t.id[:8]} | {t.title} | due {t.due_date} | {t.priority.value} | {t.status.value}")

            elif choice == "3":
                tid = input("Task ID: ")
                t = svc.get(tid)
                print(f"\n{t.id}\nTitle: {t.title}\nDesc: {t.description}\nDue: {t.due_date}\nPriority: {t.priority.value}\nStatus: {t.status.value}")

            elif choice == "4":
                # --- UPDATE (validated edit flow) ---
                tid = input("Task ID: ")
                t = svc.get(tid)

                new_title = ask_edit_text("Title", t.title)

                desc_preview = (t.description if len(t.description) <= 40 else t.description[:40] + "…")
                new_desc  = ask_edit_text(f"Description (current: {desc_preview})", t.description)

                new_due   = ask_edit_date("Due", t.due_date)
                new_pr    = ask_edit_priority(t.priority)

                svc.update(tid, title=new_title, description=new_desc, due_date=new_due, priority=new_pr)
                print("Updated ✓")

            elif choice == "5":
                tid = input("Task ID: ")
                svc.delete(tid)
                print("Deleted ✓")

            elif choice == "6":
                for t in svc.sort_by_due_date():
                    print(f"{t.due_date} | {t.title} ({t.priority.value})")

            elif choice == "0":
                print("Bye!")
                break
            else:
                print("Invalid option. Try 0–6.")
        except (ValidationError, NotFoundError) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
