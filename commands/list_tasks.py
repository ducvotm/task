from helpers.file_ops import load_tasks

def list_tasks(filter_status=None):
    tasks = load_tasks()
    if "tasks" not in tasks or not isinstance(tasks["tasks"], list):
        print("No tasks found")
        return

    filtered_tasks = [
        task for task in tasks["tasks"]
        if filter_status is None or task["status"] == filter_status
    ]
    if not filtered_tasks:
        print("No tasks found")
        return
    for task in filtered_tasks:
        print(f"[{task['status'].upper()}] {task['id']}: {task['description']} (Created: {task['createdAt']})")

