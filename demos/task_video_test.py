from os import wait
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

    task = tasks[0]
    task.train[0].get_video()


if __name__ == "__main__":
    run()
