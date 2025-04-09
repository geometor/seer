from pathlib import Path
from geometor.seer.tasks.tasks import Tasks
from geometor.seer.navigator import GridApp

# --- Configuration ---
TASKS_DIR = Path("tasks/ARC/training")  

def main():
    """
    Loads tasks from the specified directory and runs the GridApp to display them.
    """
    # 1. Load tasks
    if not TASKS_DIR.exists():
        print(f"Error: Tasks directory '{TASKS_DIR}' not found.")
        print("Please create a 'tasks' directory and place your JSON task files in it.")
        return

    try:
        tasks = Tasks(TASKS_DIR)
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return

    if not tasks:
        print("No tasks found in the 'tasks' directory.")
        return

    # 2. Create and run the GridApp
    app = GridApp(tasks)
    app.run()

if __name__ == "__main__":
    main()
