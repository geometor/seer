import yaml
from pathlib import Path
from datetime import datetime

from geometor.seer import Seer, Tasks


def run():
    #  config_file = "thinker.yaml"
    config_file = "config.yaml"
    with open(config_file, "r") as f:
        config = yaml.safe_load(f)

    #  tasks = Tasks("one")
    #  tasks = Tasks("first-six")
    #  tasks = Tasks("44").get_ordered_tasks()
    tasks = Tasks("ARC-800-tasks/training").get_ordered_tasks()
    tasks = reversed(tasks)
    #  tasks = Tasks("other-six")

    seer = Seer(
        config,
    )

    seer.run(tasks) 


if __name__ == "__main__":
    run()
