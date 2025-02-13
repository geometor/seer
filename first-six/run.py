import yaml
from pathlib import Path
from datetime import datetime

from geometor.seer.tasks import Tasks
from geometor.seer.seer import Seer


def run():
    # Load configuration
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    tasks = Tasks()

    seer = Seer(
        config,
        tasks=tasks
    )

    seer.run()


if __name__ == "__main__":
    run()
