from __future__ import annotations

from pathlib import Path
import json
from datetime import datetime

from geometor.seer.session.level import Level


class Session(Level):
    def __init__(self, config: dict, description: str): # ADD description parameter
        self.config = config
        self.description = description # STORE description
        self.tasks = {}

        output_dir = Path(config["output_dir"])
        output_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%y.%j.%H%M")
        super().__init__(None, str(output_dir / timestamp))

        self._write_context_files()

        print(timestamp)

    def summarize(self):
        summary = super().summarize()
        summary["description"] = self.description # ADD description to summary
        summary["count"] = len(self.tasks)
        summary["train_passed"] = self.train_passed_count  # Use count property
        summary["test_passed"] = self.test_passed_count    # Use count property

        # Aggregate trial counts and tokens from each SessionTask
        task_trials = {}
        total_steps = 0  # Initialize total steps
        # --- START ADDED TOKEN COUNTERS ---
        total_prompt_tokens = 0
        total_candidates_tokens = 0
        total_tokens_all_tasks = 0
        # --- END ADDED TOKEN COUNTERS ---
        total_error_count = summary["errors"]["count"] # Start with session's own errors

        for task_id, session_task in self.tasks.items():
            # Access summary information directly from session_task
            total_steps += len(session_task.steps)  # Use len(steps)
            task_trials[task_id] = {
                "train": session_task.trials.get("train", {}).get("total", 0),
                "test": session_task.trials.get("test", {}).get("total", 0),
            }

            # --- START ADDED TOKEN AGGREGATION ---
            # Read from the task's index.json for robustness
            task_summary_path = session_task.dir / "index.json"
            try:
                # Ensure the task summary exists before trying to read it
                # This assumes task.summarize() is called before session.summarize()
                if task_summary_path.exists():
                    with open(task_summary_path, "r") as f:
                        task_summary = json.load(f)

                    tokens_data = task_summary.get("tokens", {}) # Get tokens dict
                    prompt_tokens = tokens_data.get("prompt_tokens")
                    candidates_tokens = tokens_data.get("candidates_tokens")
                    total_tokens = tokens_data.get("total_tokens")

                    if prompt_tokens is not None:
                        total_prompt_tokens += prompt_tokens
                    if candidates_tokens is not None:
                        total_candidates_tokens += candidates_tokens
                    if total_tokens is not None:
                        total_tokens_all_tasks += total_tokens
                else:
                    # Log a warning if the task summary is missing
                    # TODO: Implement self.log_warning or use a proper logger
                    print(f"    WARNING (Session {self.name}): Task summary file not found for token aggregation: {task_summary_path}")

                # --- START ADDED ERROR AGGREGATION ---
                task_errors_data = task_summary.get("errors", {}) # Get errors dict, default empty
                total_error_count += task_errors_data.get("count", 0) # Add task's error count
                # --- END ADDED ERROR AGGREGATION ---

            except (json.JSONDecodeError, TypeError) as e:
                 # Log or handle error if task summary isn't valid JSON or structure is wrong
                 # TODO: Implement self.log_error or use a proper logger
                 print(f"    ERROR (Session {self.name}): Error reading task summary for token aggregation: {session_task.name} - {e}")
            except Exception as e:
                 # Catch any other unexpected errors during file reading
                 # TODO: Implement self.log_error or use a proper logger
                 print(f"    ERROR (Session {self.name}): Unexpected error reading task summary for token aggregation: {session_task.name} - {e}")
            # --- END ADDED TOKEN AGGREGATION ---


        summary["task_trials"] = task_trials
        summary["total_steps"] = total_steps  # Add total_steps to the summary

        # --- START ADDED TOKENS TO SUMMARY ---
        summary["tokens"] = {
            "prompt_tokens": total_prompt_tokens,
            "candidates_tokens": total_candidates_tokens,
            "total_tokens": total_tokens_all_tasks,
        }
        # --- END ADDED TOKENS TO SUMMARY ---
        summary["errors"]["count"] = total_error_count # Update with aggregated count

        self._write_to_json("index.json", summary)

    def add_task(self, task):
        from geometor.seer.session.session_task import SessionTask

        session_task = SessionTask(self, task)
        self.tasks[task.id] = session_task
        return session_task

    def _write_context_files(self):
        """Writes system context files for each role and the task context."""
        try:
            for role_name, role_config in self.config["roles"].items():
                system_context_file = role_config["system_context_file"]
                with open(system_context_file, "r") as f:
                    system_context = f.read().strip()
                (self.dir / f"{role_name}_system_context.md").write_text(
                    system_context
                )
        except (FileNotFoundError, IOError, PermissionError) as e:
            print(f"Error writing context files: {e}")
            self.log_error(f"Error writing context files: {e}")

        try:
            with open(self.dir / "config.json", "w") as f:
                json.dump(self.config, f, indent=2)
        except (IOError, PermissionError) as e:
            print(f"Error writing config file: {e}")
            self.log_error(f"Error writing config file: {e}")

        with open(self.config["task_context_file"], "r") as f:
            task_context = f.read().strip()
        (self.dir / "task_context.md").write_text(task_context)

    @property
    def train_passed(self):
        return any(task.train_passed for task in self.tasks.values())

    @property
    def test_passed(self):
        return any(task.test_passed for task in self.tasks.values())

    @property
    def train_passed_count(self):
        return sum(1 for task in self.tasks.values() if task.train_passed)

    @property
    def test_passed_count(self):
        return sum(1 for task in self.tasks.values() if task.test_passed)
