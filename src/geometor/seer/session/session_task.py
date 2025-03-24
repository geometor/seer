from __future__ import annotations
from typing import TYPE_CHECKING

from geometor.seer.session.level import Level

if TYPE_CHECKING:
    from geometor.seer.session import Session
    from geometor.seer.tasks.tasks import Task


class SessionTask(Level):
    def __init__(self, session: Session, task: Task):
        super().__init__(session, task.id)
        self.session = session  # parent
        self.task = task
        self.steps = []
        self.trials = {}

        try:
            task_image = task.to_image()
            image_path = self.dir / "task.png"
            task_image.save(image_path)

            task_json_str = task.nice_json_layout()
            self._write_to_file("task.json", task_json_str)

        except Exception as e:
            self.log_error(e)

        print(f"    {task.id}")

    def summarize(self):
        summary = super().summarize()

        # Aggregate trial results from all steps
        all_train_results = []
        all_test_results = []
        for step in self.steps:
            # Access step_code_trials directly
            for code_trial in step.step_code_trials.get_all_trials():
                if code_trial.train_results:
                    all_train_results.extend(code_trial.train_results.get("trials", []))
                if code_trial.test_results:
                    all_test_results.extend(code_trial.test_results.get("trials", []))

        # Calculate best_score across all steps
        # Only calculate if there are steps
        if self.steps:
            best_score = None
            for step in self.steps:
                step_best_score = step.step_code_trials.best_score  # Access directly
                if step_best_score is not None:
                    if best_score is None or step_best_score < best_score:
                        best_score = step_best_score


        # Correct train_passed and test_passed logic using any() and explicit True check
        train_passed = any(step.train_passed is True for step in self.steps)
        test_passed = any(step.test_passed is True for step in self.steps)


        summary.update(
            {
                "steps": len(self.steps),
                "matches": None,  # Filled in by TaskStep
                "train_passed": train_passed,  # Use calculated values
                "test_passed": test_passed,  # Use calculated values
            }
        )

        # Conditionally add best_score
        if self.steps and any(step.step_code_trials.best_score is not None for step in self.steps):
            summary["best_score"] = best_score

        # Conditionally add trials
        if all_train_results or all_test_results:
            self.trials = {}  # Initialize here if needed
            if all_train_results:
                self.trials["train"] = self._summarize_trial_results(all_train_results)
            if all_test_results:
                self.trials["test"] = self._summarize_trial_results(all_test_results)
            summary["trials"] = self.trials

        self._write_to_json("index.json", summary)

    def _summarize_trial_results(self, results):
        """Helper function to summarize trial results (moved from TaskStep)."""
        num_trials = len(results)
        num_passed = sum(1 for r in results if r.get("match", False))
        num_failed = num_trials - num_passed

        summary = {
            "total": num_trials,
            "passed": num_passed,
            "failed": num_failed,
        }
        return summary

    def add_step(self, title, history, prompt, instructions):
        from geometor.seer.session import TaskStep

        task_step = TaskStep(title, history, prompt, instructions, self)
        self.steps.append(task_step)
        return task_step

    @property
    def train_passed(self):
        return any(step.train_passed is True for step in self.steps)  # Check for True

    @property
    def test_passed(self):
        return any(step.test_passed is True for step in self.steps)  # Check for True
