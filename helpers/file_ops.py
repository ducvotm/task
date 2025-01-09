import json
from pathlib import Path

TASKS_FILE = Path("tasks.json")

# Ensure the JSON file exists
if not TASKS_FILE.exists():
    with open(TASKS_FILE, "w") as file:
        json.dump({"tasks": []}, file) # Writes the Python dictionary {"tasks": []} to the file in JSON format.

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return {"tasks": []} # Default empty tasks structure

# Tasks is a dictionary with a "tasks" key
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)