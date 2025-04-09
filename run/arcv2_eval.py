import yaml
from pathlib import Path
from datetime import datetime

from geometor.seer import Seer, Tasks
from geometor.seer.tasks.tasks import get_unsolved_tasks


def run():
    #  config_file = "thinker.yaml"
    config_file = "config-25.yaml"
    with open(config_file, "r") as f:
        config = yaml.safe_load(f)

    seer = Seer(config)

    output_dir = Path("../sessions_ARCv2_eval/")

    #  tasks = Tasks("../tasks/ARCv2/evaluation")
    #  tasks = tasks.get_ordered_tasks()

    #  seer.run(tasks, output_dir, "ARCv2 EVAL sorted")
    tasks = get_unsolved_tasks(output_dir)
    tasks = tasks.get_ordered_tasks()

    seer.run(tasks, output_dir, "unsolved")





if __name__ == "__main__":
    run()
