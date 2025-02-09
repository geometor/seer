import logging
import yaml
from pathlib import Path
from datetime import datetime

from geometor.arcprize.puzzles import PuzzleSet
from geometor.seer.seer import Seer
from geometor.seer.session import Session

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run():
    try:
        # Load configuration
        with open("config.yaml", "r") as f:
            config = yaml.safe_load(f)

        # Initialize PuzzleSet
        puzzle_set = PuzzleSet()
        logging.info(f"Loaded {len(puzzle_set.puzzles)} puzzles")

        # Initialize Session
        timestamp = datetime.now().strftime("%y.%j.%H%M%S") # Generate timestamp
        session = Session(
            output_dir=config["output_dir"],
            puzzle_id=puzzle_set[0].id,  # Assuming you want to solve the first puzzle
            timestamp=timestamp
        )

        # Initialize Seer
        seer = Seer(
            nlp_model=config["nlp_model"],
            code_model=config["code_model"],
            system_context=config["system_context"],
            task_context=config["task_context"],
            session=session
        )

        # Solve the task
        seer.solve_task(puzzle_set[0])

    except FileNotFoundError:
        logging.error("Error: config.yaml not found. Please create a config file.")
    except Exception as e:
        logging.exception("An error occurred during the run:")

if __name__ == "__main__":
    run()
