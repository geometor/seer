"""Subpackage defining task (Task, TaskPair) and grid (Grid) structures."""
# Explicitly list public API elements
from .tasks import (
    Task,
    Tasks,
    TaskPair,
    load_tasks_from_kaggle_json,
    get_unsolved_tasks,
    get_partially_solved_tasks, # Add the new function here
)
from .grid import Grid, string_to_grid

__all__ = [
    "Task",
    "Tasks",
    "TaskPair",
    "Grid",
    "string_to_grid",
    "load_tasks_from_kaggle_json",
    "get_unsolved_tasks",
    "get_partially_solved_tasks", # And here
]
