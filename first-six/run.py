import yaml
from pathlib import Path
from datetime import datetime

from geometor.arcprize.puzzles import PuzzleSet
from geometor.seer.seer import Seer
from geometor.seer.session import Session  # Session is still imported, but not used directly here


def run():
    # Load configuration
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    # Initialize PuzzleSet
    tasks = PuzzleSet()

    # Initialize Seer (Session is created internally by Seer)
    seer = Seer(
        config,
        tasks=tasks
    )

    seer.run()


if __name__ == "__main__":
    run()
