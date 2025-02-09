from rich import print
from datetime import datetime
from pathlib import Path
import json
import os

from geometor.arcprize.puzzles import PuzzleSet
from geometor.seer.seer import Seer

def run():
    puzzle_set = PuzzleSet()
    print(f"Loaded {len(puzzle_set.puzzles)} puzzles")

    model_name = "gemini-2.0-flash-thinking-exp-1219"
    #  model_name = "gemini-exp-1206"

    seer = Seer()

    seer.solve_task(puzzle_set[0])

if __name__ == "__main__":
    run()
