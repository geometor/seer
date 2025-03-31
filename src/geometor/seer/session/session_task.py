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
        summary = super().summarize()

        # Aggregate trial results from all steps
        all_train_results = []
        all_test_results = []
        # --- START ADDED TOKEN COUNTERS ---
        total_prompt_tokens = 0
        total_candidates_tokens = 0
        total_tokens_all_steps = 0
        # --- END ADDED TOKEN COUNTERS ---

        for step in self.steps:
            # Access step_code_trials directly
            for code_trial in step.step_code_trials.get_all_trials():
                if code_trial.train_results:
                    all_train_results.extend(code_trial.train_results.get("trials", []))
                if code_trial.test_results:
                    all_test_results.extend(code_trial.test_results.get("trials", []))

            # --- START ADDED TOKEN AGGREGATION ---
            # Ensure step summary is generated first if needed, or read directly
            # Let's read from the step's index.json for robustness
            step_summary_path = step.dir / "index.json"
            try:
                # Ensure the step summary exists before trying to read it
                # This assumes step.summarize() is called before task.summarize()
                if step_summary_path.exists():
                    with open(step_summary_path, "r") as f:
                        step_summary = json.load(f)

                    prompt_tokens = step_summary.get("response", {}).get("prompt_tokens")
                    candidates_tokens = step_summary.get("response", {}).get("candidates_tokens")
                    total_tokens = step_summary.get("response", {}).get("total_tokens")

                    if prompt_tokens is not None:
                        total_prompt_tokens += prompt_tokens
                    if candidates_tokens is not None:
                        total_candidates_tokens += candidates_tokens
                    if total_tokens is not None:
                        total_tokens_all_steps += total_tokens
                else:
                    # Log a warning if the step summary is missing
                    self.log_warning(f"Step summary file not found for token aggregation: {step_summary_path}", "SessionTask Summarize")

            except (json.JSONDecodeError, TypeError) as e:
                 # Log or handle error if step summary isn't valid JSON or structure is wrong
                 self.log_error(e, f"Error reading step summary for token aggregation: {step.dir.name}")
            except Exception as e:
                 # Catch any other unexpected errors during file reading
                 self.log_error(e, f"Unexpected error reading step summary for token aggregation: {step.dir.name}")
            # --- END ADDED TOKEN AGGREGATION ---


        # Calculate best_score across all steps
        # Only calculate if there are steps
        best_score = None # Initialize outside the loop
        if self.steps:
            valid_scores = [
                step.step_code_trials.best_score
                for step in self.steps
                if step.step_code_trials.best_score is not None
            ]
            if valid_scores:
                best_score = min(valid_scores)


        # Correct train_passed and test_passed logic using any() and explicit True check
        train_passed = any(step.train_passed is True for step in self.steps)
        test_passed = any(step.test_passed is True for step in self.steps)


        summary.update(
            {
                "steps": len(self.steps),
                "matches": None,  # Filled in by TaskStep
                "train_passed": train_passed,  # Use calculated values
                "test_passed": test_passed,  # Use calculated values
                # --- START ADDED TOKENS TO SUMMARY ---
                "tokens": {
                    "prompt_tokens": total_prompt_tokens,
                    "candidates_tokens": total_candidates_tokens,
                    "total_tokens": total_tokens_all_steps,
                }
                # --- END ADDED TOKENS TO SUMMARY ---
            }
        )

        # Conditionally add best_score
        if best_score is not None: # Check if best_score was calculated
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
        num_passed = sum(1 for r in results if r.match)
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

    # --- Start of added method ---
    def log_warning(self, message: str, context: str = ""):
        """Logs a warning message to the task's warnings.txt."""
        # This method might be better placed in the Level class if needed elsewhere
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
