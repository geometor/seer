# Standard library imports
import yaml # Keep yaml import if needed elsewhere, otherwise remove
from pathlib import Path
from datetime import datetime
import sys # For exiting on error

# Local application/library specific imports
from geometor.seer import Seer, Tasks
from geometor.seer.config import Config, ConfigError
from geometor.seer.tasks.tasks import get_unsolved_tasks, load_tasks_from_kaggle_json


def run():
    # --- Configuration Loading ---
    # Define the directory containing your index.yaml and other config files
    # Assuming your config files (index.yaml, instructions/, etc.)
    # are in a directory named 'seer_config' relative to this script.
    # Adjust this path as necessary.
    config_dir = Path("./config") # Or Path("path/to/your/config_directory")

    try:
        # Instantiate the Config object, passing the directory path
        config = Config(config_dir)
        print(f"Configuration loaded successfully from: {config_dir}")
    except (FileNotFoundError, ConfigError) as e:
        print(f"FATAL: Failed to load configuration from {config_dir}: {e}")
        sys.exit(1) # Exit if configuration fails to load
    # --- End Configuration Loading ---

    # Seer now expects the Config object directly
    try:
        seer = Seer(config)
    except (ValueError, RuntimeError) as e:
        # Catch errors during Seer initialization (e.g., missing roles, client init failure)
        print(f"FATAL: Failed to initialize Seer: {e}")
        sys.exit(1)

    # --- Task Loading and Execution ---
    output_dir = Path("../sessions_kaggle/")
    # Ensure output directory exists (optional, Session might handle this)
    # output_dir.mkdir(parents=True, exist_ok=True)

    # Define the path to your Kaggle JSON data
    kaggle_json = Path("./arc-agi_training_challenges.json") # Adjust path if needed

    try:
        print(f"Loading tasks from: {kaggle_json}")
        tasks = load_tasks_from_kaggle_json(kaggle_json)
        print(f"Loaded {len(tasks)} tasks.")
    except FileNotFoundError:
        print(f"FATAL: Kaggle JSON file not found at {kaggle_json}")
        sys.exit(1)
    except Exception as e:
        print(f"FATAL: Error loading tasks from {kaggle_json}: {e}")
        sys.exit(1)


    # Optional: Filter for unsolved tasks (uncomment if needed)
    # try:
    #     print(f"Filtering for unsolved tasks based on sessions in: {output_dir}")
    #     tasks = get_unsolved_tasks(output_dir)
    #     print(f"Found {len(tasks)} unsolved tasks.")
    # except Exception as e:
    #     print(f"Warning: Error getting unsolved tasks: {e}. Proceeding with all loaded tasks.")
    #     # Fallback to using all loaded tasks if filtering fails
    #     tasks = load_tasks_from_kaggle_json(kaggle_json)


    # Order tasks (optional, based on your needs)
    tasks = tasks.get_ordered_tasks() # Example: order by default weight
    print("Tasks ordered.")

    # Select a subset of tasks to run (e.g., the first 5)
    tasks_to_run = tasks[0:5]
    if not tasks_to_run:
        print("No tasks selected to run. Exiting.")
        sys.exit(0)

    print(f"Running Seer for {len(tasks_to_run)} tasks...")
    session_description = "kaggle test run" # More descriptive name?
    seer.run(tasks_to_run, output_dir, session_description)

    print("Run completed.")

    # --- Optional: Processing multiple sets (commented out) ---
    # parent_path = Path("../tasks/ConceptARC")
    # for set_dir in parent_path.iterdir():
    #     if set_dir.is_dir():
    #         print(f"\n--- Processing Set: {set_dir.name} ---")
    #         try:
    #             tasks = Tasks(set_dir) # Assumes Tasks can load from a directory structure
    #             tasks = tasks.get_ordered_tasks()
    #             if tasks:
    #                 print(f"Running Seer for {len(tasks)} tasks in set {set_dir.name}...")
    #                 seer.run(tasks, output_dir, f"Set: {set_dir.name}")
    #             else:
    #                 print(f"No tasks found in set {set_dir.name}.")
    #         except Exception as e:
    #             print(f"Error processing set {set_dir.name}: {e}")
    #         print(f"--- Finished Set: {set_dir.name} ---")


if __name__ == "__main__":
    run()
