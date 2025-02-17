import yaml
from pathlib import Path
from datetime import datetime

from geometor.seer.tasks import Tasks
from geometor.seer.seer import Seer


def run():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    tasks = Tasks("one")

    seer = Seer(
        config,
    )

    seer.run(tasks) 


if __name__ == "__main__":
    run()
