from __future__ import annotations
from typing import TYPE_CHECKING

from geometor.seer.session.level import Level
import json # Added for reading step summary
from datetime import datetime # Keep for log_warning

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
        # Get base summary (errors, duration)
        summary = super().summarize()
        # Check if any errors were logged at this level
        has_errors = bool(self.errors)

        # --- Analyze Step Summaries ---
        step_summaries = []
        for step in self.steps:
            # Ensure step summary exists (it should have been created by step.summarize())
            step_summary_path = step.dir / "index.json"
            if step_summary_path.exists():
                try:
                    with open(step_summary_path, "r") as f:
                        step_summary = json.load(f)
                        step_summaries.append(step_summary)
                        # Aggregate step errors into task errors
                        if step_summary.get("has_errors"):
                             has_errors = True # Mark task as having errors if any step has errors
                except (json.JSONDecodeError, TypeError, Exception) as e:
                    self.log_error(e, f"Error reading step summary for task aggregation: {step.dir.name}")
            else:
                self.log_warning(f"Step summary file not found for task aggregation: {step_summary_path}", "SessionTask Summarize")

        # Call the static analysis method
        analysis_results = SessionTask.analyze_step_summaries(step_summaries)

        # --- Update Task Summary ---
        summary["has_errors"] = has_errors # Set based on own errors + step errors
        summary["steps"] = analysis_results["steps"]
        summary["train_passed"] = analysis_results["train_passed"]
        summary["test_passed"] = analysis_results["test_passed"]
        summary["tokens"] = analysis_results["tokens"]

        # Conditionally add best_score
        if analysis_results["best_score"] is not None:
            summary["best_score"] = analysis_results["best_score"]

        # Remove detailed errors dict and trials dict as per step refactor
        if "errors" in summary:
             del summary["errors"]
        # summary["trials"] = {} # Removed trials summary

        self._write_to_json("index.json", summary)

    def _summarize_trial_results(self, results):
        """Helper function to summarize trial results."""
        num_trials = len(results)
        num_passed = sum(1 for r in results if r.match)
        num_failed = num_trials - num_passed

        summary = {
            "total": num_trials,
            "passed": num_passed,
            "failed": num_failed,
        }
        return summary

    # Add model_name parameter with a default value for backward compatibility if needed
    def add_step(self, title: str, history: list, content: list, instructions: list, model_name: str | None = None):
        """Adds a new step to the task."""
        from geometor.seer.session import TaskStep # Keep local import

        # Pass model_name to TaskStep constructor
        task_step = TaskStep(title, history, content, instructions, self, model_name)
        self.steps.append(task_step)
        return task_step

    @staticmethod
    def analyze_step_summaries(step_summary_list: List[Dict]) -> Dict:
        """
        Analyzes a list of step summary dictionaries and returns aggregated task-level metrics.

        Args:
            step_summary_list: A list of dictionaries, where each dictionary is a
                               TaskStep summary (loaded from index.json or generated).

        Returns:
            A dictionary containing aggregated task-level results:
            - train_passed: True if any step passed training, else False.
            - test_passed: True if any step passed testing, else False.
            - best_score: The lowest best_score found across all steps (float or None).
            - tokens: Dictionary containing aggregated token counts.
            - steps: The total number of steps analyzed.
        """
        results = {
            "train_passed": False,
            "test_passed": False,
            "best_score": None,
            "tokens": {
                "prompt_tokens": 0,
                "candidates_tokens": 0,
                "total_tokens": 0,
            },
            "steps": len(step_summary_list),
        }

        best_score = float('inf')
        found_valid_score = False

        for step_summary in step_summary_list:
            # Aggregate tokens
            tokens = step_summary.get("response", {})
            prompt_tokens = tokens.get("prompt_tokens")
            candidates_tokens = tokens.get("candidates_tokens")
            total_tokens = tokens.get("total_tokens")

            if prompt_tokens is not None:
                results["tokens"]["prompt_tokens"] += prompt_tokens
            if candidates_tokens is not None:
                results["tokens"]["candidates_tokens"] += candidates_tokens
            if total_tokens is not None:
                results["tokens"]["total_tokens"] += total_tokens

            # Aggregate passed status
            if step_summary.get("train_passed") is True:
                results["train_passed"] = True
            if step_summary.get("test_passed") is True:
                results["test_passed"] = True

            # Find overall best score
            step_best_score = step_summary.get("best_score")
            if step_best_score is not None and step_best_score < best_score:
                best_score = step_best_score
                found_valid_score = True

        results["best_score"] = best_score if found_valid_score else None
        return results


    @property
    def train_passed(self):
        return any(step.train_passed is True for step in self.steps)  # Check for True

    @property
    def test_passed(self):
        return any(step.test_passed is True for step in self.steps)  # Check for True


    def log_warning(self, message: str, context: str = ""):
        """Logs a warning message to the task's warnings.txt."""
        # This method is useful here, but could be moved to Level if needed more broadly
        # For now, keeping it here as requested by the context of the change.
        timestamp = datetime.now().isoformat()
        log_entry = f"[{timestamp}]"
        if context:
            log_entry += f" Context: {context}"
        log_entry += f"\nWarning: {message}\n---\n"

        try:
            # Append warning to the file in the task directory
            warnings_file = self.dir / "warnings.txt"
            with open(warnings_file, "a") as f:
                f.write(log_entry)
            # Also print the warning for immediate visibility
            print(f"    WARNING ({self.name}): {message}" + (f" (Context: {context})" if context else ""))
        except Exception as e:
            # Fallback if logging fails
            print(f"    CRITICAL ({self.name}): Failed to log warning: {message}. Error: {e}")
    # --- End of added method ---
