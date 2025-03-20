from typing import Dict
from geometor.seer.trials.code_trial import CodeTrial

class StepCodeTrials:
    """
    Manages a collection of CodeTrial instances for a TaskStep.
    """
    def __init__(self):
        self.code_trials: Dict[str, CodeTrial] = {}

    def add_code_trial(self, code_filename: str, code_trial: CodeTrial):
        """Adds a CodeTrial instance to the collection."""
        self.code_trials[code_filename] = code_trial

    def get_code_trial(self, code_filename: str) -> CodeTrial | None:
        """Retrieves a CodeTrial by its filename."""
        return self.code_trials.get(code_filename)

    def get_first_code_trial(self) -> CodeTrial | None:
        """Retrieves the first CodeTrial, if any."""
        if self.code_trials:
            return next(iter(self.code_trials.values()))
        return None

    @property
    def any_train_passed(self) -> bool:
        """Checks if any train trials passed."""
        return any(trial.train_passed for trial in self.code_trials.values())

    @property
    def any_test_passed(self) -> bool:
        """Checks if any test trials passed."""
        return any(trial.test_passed for trial in self.code_trials.values())

    def get_all_trials(self):
        """Returns a list of all CodeTrial objects."""
        return list(self.code_trials.values())
