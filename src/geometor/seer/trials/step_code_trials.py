import ast
import contextlib
import io
import multiprocessing
from typing import Dict

import numpy as np

from geometor.seer.trials.code_trial import CodeTrial
from geometor.seer.trials.task_pair_trial import TaskPairTrial
from geometor.seer.tasks.grid import Grid


class StepCodeTrials:
    """
    Manages a collection of CodeTrial instances for a TaskStep.
    """

    def __init__(self, task_step):
        self.task_step = task_step  # parent
        self.code_trials: Dict[str, CodeTrial] = {}

    def run_trials(self):
        task = self.task_step.session_task.task
        for code_filename, code in self.task_step.get_python.items():
            code_trial = CodeTrial(self.task_step, code_filename, code, task)
            self.code_trials[code_filename] = code_trial

    def get_code_trial(self, code_filename: str) -> CodeTrial | None:
        return self.code_trials.get(code_filename)

    def get_first_code_trial(self) -> CodeTrial | None:
        """Retrieves the first CodeTrial, if any."""
        if self.code_trials:
            return next(iter(self.code_trials.values()))
        return None

    @property
    def any_train_passed(self) -> bool | None:
        """Checks if any train trials passed."""
        if not self.code_trials:
            return None  # No CodeTrials, return None
        for trial in self.code_trials.values():
            if trial.train_passed is True:
                return True  # Found at least one True
        return False  # No True found, but CodeTrials exist

    @property
    def any_test_passed(self) -> bool | None:
        """Checks if any test trials passed."""
        if not self.code_trials:
            return None  # No CodeTrials, return None
        for trial in self.code_trials.values():
            if trial.test_passed is True:
                return True  # Found at least one True
        return False  # No True found, but CodeTrials exist

    @property
    def count_trials(self) -> int:
        """Checks if any test trials passed."""
        return len(self.code_trials)

    def get_all_trials(self):
        """Returns a list of all CodeTrial objects."""
        return list(self.code_trials.values())


    def execute_trials(self, task):
        """Executes trials for all available code."""

            #  code_trial.execute_and_save_results()

    def get_best_trial(self):
        """Returns the CodeTrial with the lowest total score."""
        best_trial = None
        best_score = float('inf')  # Initialize with a high score

        for trial in self.code_trials.values():
            # Use total_score and handle None values
            if trial.total_score is not None and trial.total_score < best_score:
                best_score = trial.total_score
                best_trial = trial
        return best_trial

    @property
    def best_score(self):
        best_trial = self.get_best_trial()
        # Return total_score of the best trial
        return best_trial.total_score if best_trial else None
