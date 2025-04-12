import yaml
from pathlib import Path
from datetime import datetime

from geometor.seer import Seer, Tasks
from geometor.seer.tasks.tasks import get_unsolved_tasks, get_partially_solved_tasks


def run():
    #  config_file = "thinker.yaml"
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

    output_dir = Path("../sessions_ARCv2_eval/")

    #  tasks = Tasks("../tasks/ARCv2/evaluation")
    #  tasks = tasks.get_ordered_tasks()

    #  seer.run(tasks, output_dir, "ARCv2 EVAL sorted")
    #  tasks = get_unsolved_tasks(output_dir)
    tasks = get_partially_solved_tasks(output_dir)
    #  tasks = tasks.get_ordered_tasks()

    seer.run(tasks[0:1], output_dir, "previous partial solve")





if __name__ == "__main__":
    run()
