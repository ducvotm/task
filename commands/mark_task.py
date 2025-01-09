from helpers.file_ops import load_tasks, save_tasks
from helpers.task_utils import get_current_time

def mark_task(task_id, status):
    if status not in ["in-progress", "done"]:
        print("Invalid status. Use 'in-progress' or 'done'")
        return

    tasks = load_tasks()
    for task in tasks["tasks"]:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = get_current_time()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}")
            return
    print(f"Task with ID {task_id} not found")
