import sys
import json
import os
from datetime import datetime

JSON_FILE = "tasks.json"

# --- Helper Functions ---
def load_tasks():
    if not os.path.exists(JSON_FILE):
        return []
    try:
        with open(JSON_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    with open(JSON_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# --- Feature Implementations ---

def add_task(description):
    tasks = load_tasks()
    new_id = max([t["id"] for t in tasks], default=0) + 1
    now = datetime.now().isoformat()

    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully.")
            return
    print(f"Error: Task with ID {task_id} not found.")

def delete_task(task_id):
    tasks = load_tasks()
    filtered_tasks = [t for t in tasks if t["id"] != task_id]

    if len(filtered_tasks) == len(tasks):
        print(f"Error: Task with ID {task_id} not found.")
    else:
        save_tasks(filtered_tasks)
        print(f"Task {task_id} deleted successfully.")

def change_status(task_id, new_status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {new_status}.")
            return
    print(f"Error: Task with ID {task_id} not found.")

def list_tasks(status_filter=None):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    print(f"\n{'ID':<5} {'Description':<30} {'Status':<15} {'Last Updated':<20}")
    print("-" * 75)

    for t in tasks:
        if status_filter and t["status"] != status_filter:
            continue
        print(f"{t['id']:<5} {t['description']:<30} {t['status']:<15} {t['updatedAt'][:16]}")

# --- CLI Router ---
def main():
    if len(sys.argv) < 2:
        print("Usage: python task_tracker.py [command] [args]")
        return

    # FIXED: Now correctly targeting index 1 for the command name string
    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) < 3: return print("Error: Missing description.")
        add_task(sys.argv[2])

    elif command == "update":
        if len(sys.argv) < 4: return print("Usage: update [id] [new description]")
        update_task(int(sys.argv[2]), sys.argv[3])

    elif command == "delete":
        if len(sys.argv) < 3: return print("Usage: delete [id]")
        delete_task(int(sys.argv[2]))

    elif command == "mark-in-progress":
        if len(sys.argv) < 3: return print("Usage: mark-in-progress [id]")
        change_status(int(sys.argv[2]), "in-progress")

    elif command == "mark-done":
        if len(sys.argv) < 3: return print("Usage: mark-done [id]")
        change_status(int(sys.argv[2]), "done")

    elif command == "list":
        if len(sys.argv) == 3:
            list_tasks(status_filter=sys.argv[2].lower())
        else:
            list_tasks()

    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
