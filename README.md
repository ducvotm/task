https://roadmap.sh/projects/task-tracker

# Task CLI

A command-line task management application built with Python that helps you manage your daily tasks efficiently.

## Features

- Add new tasks
- Update existing tasks
- Mark tasks as in-progress or done
- Delete tasks
- List all tasks or filter by status
- Persistent storage using JSON

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ducvotm/task_tracker.git
   cd Task_Tracker
   ```

2. Ensure you have Python 3.x installed
3. Make the CLI executable:
   ```bash
   chmod +x task-cli
   ```

## Usage

Run the CLI using:

Available commands:

- `add`: Add a new task
  ```bash
  ./task-cli add "Complete project documentation"
  ```

- `list`: List all tasks
  ```bash
  ./task-cli list
  ./task-cli list --status done
  ```

- `update`: Update a task
  ```bash
  ./task-cli update 1 --title "Updated task title"
  ```

- `status`: Change task status
  ```bash
  ./task-cli --status 1 in-progress
  ```

- `delete`: Remove a task
  ```bash
  ./task-cli delete 1
  ```

## Configuration

Tasks are stored in `tasks.json` in your home directory. The file is created automatically on first run.

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
# task
# task
# task
