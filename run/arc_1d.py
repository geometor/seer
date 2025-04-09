import yaml
from pathlib import Path
from datetime import datetime

from geometor.seer import Seer, Tasks
from geometor.seer.config import Config, ConfigError
from geometor.seer.tasks.tasks import get_unsolved_tasks


def run():
    config_dir = Path("./config") 

    try:
        config = Config(config_dir)
        print(f"Configuration loaded successfully from: {config_dir}")
    except (FileNotFoundError, ConfigError) as e:
        print(f"FATAL: Failed to load configuration from {config_dir}: {e}")
        sys.exit(1) 

    try:
        seer = Seer(config)
    except (ValueError, RuntimeError) as e:
        print(f"FATAL: Failed to initialize Seer: {e}")
        sys.exit(1)

    output_dir = Path("../sessions_optorex_1D/")

    #  tasks = Tasks("../tasks/ConceptARC_minimal")
    #  #  tasks = get_unsolved_tasks(Path("../sessions"))
    #  tasks = tasks.get_ordered_tasks()

    #  seer.run(tasks, output_dir, "minimal")

    parent_path = Path("../tasks/optorex_1D")
    for set_dir in parent_path.iterdir():
        if set_dir.is_dir():
            print("SET:", set_dir.name)

            tasks = Tasks(set_dir)
            tasks = tasks.get_ordered_tasks()
            seer.run(tasks, output_dir, set_dir.name)





if __name__ == "__main__":
    run()
