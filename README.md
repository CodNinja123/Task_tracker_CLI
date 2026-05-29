Project URL:https://roadmap.sh/projects/task-tracker
# Task Tracker CLI

A zero-dependency command-line interface application to track tasks and manage to-do lists, built with Python.

## How to Run

### Add a new task
```bash
python task_tracker.py add "Visit Grandma"
```

### List all tasks
```bash
python task_tracker.py list
```

### List tasks by status
```bash
python task_tracker.py list todo
python task_tracker.py list in-progress
python task_tracker.py list done
```

### Update a task
```bash
python task_tracker.py update 1 "Buy organic groceries"
```

### Delete a task
```bash
python task_tracker.py delete 1
```

### Mark task status
```bash
python task_tracker.py mark-in-progress 1
python task_tracker.py mark-done 1
```
