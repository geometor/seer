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

    #  tasks = Tasks("../../_ARC-AGI-2/data/training")
    #  tasks = Tasks("../../_ConceptARC/corpus/Copy")
    #  tasks = Tasks("tasks/ARC/evaluation")
    #  tasks = Tasks("tasks/ARC/training").get_ordered_by_train_count()
    #  tasks = list(reversed(tasks))

    tasks = get_unsolved_tasks(Path("../sessions"))

    tasks = tasks.get_ordered_tasks()

    seer = Seer(config)

    seer.run(tasks[50:100], "unsolved sorted 050:100")
    #  seer.run(tasks)


if __name__ == "__main__":
    run()
