from helpers.file_ops import load_tasks, save_tasks
from helpers.task_utils import generate_id, get_current_time

def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": generate_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": get_current_time(),
        "updatedAt": get_current_time(),
    }
    tasks["tasks"].append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")
