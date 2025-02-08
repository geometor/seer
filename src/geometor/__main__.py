from geometor.arcprize.puzzles import Puzzle, PuzzleSet, Grid
from rich import print
from datetime import datetime
from pathlib import Path
import json
import os
from .gemini_solver import PuzzleSolver

def solve_all_puzzles(puzzle_set):
    timestamp = datetime.now().strftime("%y.%j.%H%M%S")
    for puzzle in puzzle_set.puzzles:

        solver = PuzzleSolver(puzzle, timestamp=timestamp, output_dir="../docsrc")
        solver.solve()

def run():
    puzzle_set = PuzzleSet()
    print(f"Loaded {len(puzzle_set.puzzles)} puzzles")

    solve_all_puzzles(puzzle_set)

    #  timestamp = datetime.now().strftime("%y.%j.%H%M%S")
    #  solver = PuzzleSolver(puzzle_set.puzzles[0], timestamp=timestamp, output_dir="../docsrc")
    #  solver.solve()


if __name__ == "__main__":
    run()

