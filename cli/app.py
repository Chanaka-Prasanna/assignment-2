# cli/app.py
from datetime import date
from domain.errors import ValidationError, NotFoundError
from services.task_service import TaskService
from infra.json_repository import JSONTaskRepository
from utils.validation import choose_priority, parse_date

def main():
    svc = TaskService(JSONTaskRepository())

    while True:
        print("\n1) Add  2) List  3) View  4) Update  5) Delete  6) Sort  0) Quit")
        choice = input("> ").strip()
        try:
            if choice == "1":
                while True:
                    try:
                        title = input("Title: ")
                        if not title.strip():
                            raise ValidationError("Title cannot be empty.")
                        break
                    except ValidationError as e:
                        print(f"Error: {e}")
                while True:
                    try:
                        desc = input("Description: ")
                        if not desc.strip():
                            raise ValidationError("Description cannot be empty.")
                        break
                    except ValidationError as e:
                        print(f"Error: {e}")

                while True:
                    try:
                        due = parse_date(input("Due date (YYYY-MM-DD): "))
                        break
                    except ValidationError as e:
                        print(f"Error: {e}")

                while True:
                    try:
                        pr_input = input("Priority [low(l) | medium(m) | high(h) ] (default=medium): ") or "medium"
                        pr = choose_priority(pr_input)
                        break
                    except ValidationError as e:
                        print(f"Error: {e}")
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
                tid = input("Task ID: ")
                t = svc.get(tid)
                new_title = input(f"Title [{t.title}]: ").strip() or t.title
                new_desc  = input(f"Description [{t.description[:20]}...]: ").strip() or t.description
                raw_due   = input(f"Due [{t.due_date}]: ").strip()
                new_due   = parse_date(raw_due) if raw_due else t.due_date
                raw_pr    = input(f"Priority [{t.priority.value}]: ").strip()
                new_pr    = choose_priority(raw_pr) if raw_pr else t.priority
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
