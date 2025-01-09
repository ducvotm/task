from helpers.file_ops import load_tasks, save_tasks
from helpers.task_utils import get_current_time

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks["tasks"]:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updateAt"] = get_current_time()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully")
            return
    print(f"Task with ID {task_id} not found")