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

    output_dir = Path("../sessions_ARCv2_train/")

    #  tasks = Tasks("../tasks/ARCv2/training")
    tasks = get_unsolved_tasks(output_dir)
    tasks = tasks.get_ordered_tasks()

    #  seer.run(tasks[0:100], output_dir, "ARCv2 training 000:100")
    seer.run(tasks, output_dir, "unsolved")
    





if __name__ == "__main__":
    run()
