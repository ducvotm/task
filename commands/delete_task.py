from helpers.file_ops import load_tasks, save_tasks

def delete_task(task_id):
    tasks = load_tasks()
    tasks["tasks"] = [task for task in tasks["tasks"] if task["id"] != task_id]  # Fixed line
    save_tasks(tasks)
    print(f"Task {task_id} deleted successfully")
