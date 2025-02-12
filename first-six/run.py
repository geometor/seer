import yaml
from pathlib import Path
from datetime import datetime

from geometor.arcprize.puzzles import PuzzleSet
from geometor.seer.seer import Seer
from geometor.seer.session import Session



def run():
    # Load configuration
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    # Initialize PuzzleSet
    tasks = PuzzleSet()

    # Initialize Session
    session = Session(
        config,
        tasks=tasks
    )

    session.run()


if __name__ == "__main__":
    run()
