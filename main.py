#!/usr/bin/env python3

import sys
from commands.add_task import add_task
from commands.update_task import update_task
from commands.delete_task import delete_task
from commands.mark_task import mark_task
from commands.list_tasks import list_tasks

def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        return
    
    command = sys.argv[1]
    try:
        if command == "add" and len(sys.argv) == 3:
            add_task(sys.argv[2])
        elif command == "update" and len(sys.argv) == 4:
            update_task(int(sys.argv[2]), sys.argv[3])
        elif command == "delete" and len(sys.argv) == 3:
            delete_task(int(sys.argv[2]))
        elif command == "mark-in-progress" and len(sys.argv) == 3:
            mark_task(int(sys.argv[2]), "in-progress")
        elif command == "mark-done" and len(sys.argv) == 3:
            mark_task(int(sys.argv[2]), "done")
        elif command == "list" and len(sys.argv) == 2:
            list_tasks()
        elif command == "list" and len(sys.argv) == 3:
            if sys.argv[2] in ["todo", "in-progress", "done"]:
                list_tasks(sys.argv[2])
            else:
                print("Invalid status. Use 'todo', 'in-progress', 'done'")
        else:
            print("Invalid command or arguments")
    except ValueError:
        print("Invalid task ID")
        
if __name__ == "__main__":
    main()