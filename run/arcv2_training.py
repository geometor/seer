import yaml
from pathlib import Path
from datetime import datetime

from geometor.seer import Seer, Tasks
from geometor.seer.config import Config, ConfigError
from geometor.seer.tasks.tasks import get_unsolved_tasks


def run():
    config_dir = Path("./config")

    config = Config(config_dir)
    seer = Seer(config)

    output_dir = Path("../../seer_sessions/sessions_ARCv2_train/")

    # read tasks from json files in folder
    tasks = Tasks("../tasks/ARCv2/training")
    # sort the tasks by "weight" - total pixels in train
    tasks = tasks.get_ordered_tasks()

    seer.run(tasks[0:100], output_dir, "ARCv2 training 000:100")

    #  tasks = get_unsolved_tasks(output_dir)
    #  seer.run(tasks, output_dir, "unsolved")


if __name__ == "__main__":
    run()
