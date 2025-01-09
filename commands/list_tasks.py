from helpers.file_ops import load_tasks

def list_tasks(filter_status=None):
    tasks = load_tasks()

    # The data structure has a "tasks" key
    # The value stored in "tasks" is actually a list
    if "tasks" not in tasks or not isinstance(tasks["tasks"], list):
        print("No tasks found")
        return


    filtered_tasks = [
        # Take each task dictionary from tasks["tasks"]
        # Temporarily call it task
        # If it passes the filter condition, include it in the new list
        # Move to the next task and repeat
        task for task in tasks["tasks"]
        if filter_status is None or task["status"] == filter_status
    ]

    if not filtered_tasks:
        print("No tasks found")
        return
    for task in filtered_tasks:
        print(f"[{task['status'].upper()}] {task['id']}: {task['description']} (Created: {task['createdAt']})")

