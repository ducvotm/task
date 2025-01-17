from datetime import datetime

def generate_id(tasks):
    if not tasks["tasks"]:
        return 1
    return max(task["id"] for task in tasks["tasks"]) + 1

def get_current_time():
    # Returns the current time in ISO format
    return datetime.now().isoformat()