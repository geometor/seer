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
            step_summary = step.summarize()  # Get step summary
            train_trials = step_summary.get("trials", {}).get("train", {})
            test_trials = step_summary.get("trials", {}).get("test", {})

            # Extend with individual trial results from each step
            if train_trials:
                all_train_results.extend(
                    [
                        {"match": i < train_trials.get("passed", 0)}
                        for i in range(train_trials.get("total", 0))
                    ]
                )
            if test_trials:
                all_test_results.extend(
                    [
                        {"match": i < test_trials.get("passed", 0)}
                        for i in range(test_trials.get("total", 0))
                    ]
                )

        # Calculate best_score across all steps
        best_score = None
        for step in self.steps:
            step_best_score = step.step_code_trials.best_score
            if step_best_score is not None:
                if best_score is None or step_best_score < best_score:
                    best_score = step_best_score

        summary.update(
            {
                "steps": len(self.steps),
                "trials": {  # Include aggregated trials
                    "train": self._summarize_trial_results(all_train_results)
                    if all_train_results
                    else {},
                    "test": self._summarize_trial_results(all_test_results)
                    if all_test_results
                    else {},
                },
                "matches": None,  # Filled in by TaskStep
                "train_passed": self.train_passed,
                "test_passed": self.test_passed,
                "best_score": best_score,  # Add best_score
            }
        )
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
        return any(step.train_passed for step in self.steps)

    @property
    def test_passed(self):
        return any(step.test_passed for step in self.steps)

