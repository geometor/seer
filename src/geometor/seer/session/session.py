from __future__ import annotations

from pathlib import Path
import json
from datetime import datetime

from geometor.seer.session.level import Level


class Session(Level):
    def __init__(self, config: dict):
        self.config = config
        self.tasks = {}

        output_dir = Path(config["output_dir"])
        output_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%y.%j.%H%M")
        super().__init__(None, str(output_dir / timestamp))

        self._write_context_files()

        print(timestamp)

    def summarize(self):
        summary = super().summarize()
        summary["count"] = len(self.tasks)
        summary["train_passed"] = self.train_passed_count  # Use count property
        summary["test_passed"] = self.test_passed_count    # Use count property

        # Aggregate trial counts from each SessionTask
        task_trials = {}
        total_steps = 0  # Initialize total steps
        for task_id, session_task in self.tasks.items():
            task_summary = session_task.summarize() # Get the latest summary
            if task_summary is None:  # Handle None
                self.log_error(Exception("Task summarize returned None"), f"Task: {task_id}")
                continue # Skip this task

            total_steps += task_summary.get("steps", 0) # Accumulate steps
            trials = task_summary.get("trials", {})  # Get trials safely with a default
            task_trials[task_id] = {
                "train": trials.get("train", {}).get("total", 0),
                "test": trials.get("test", {}).get("total", 0),
            }


        summary["task_trials"] = task_trials
        summary["total_steps"] = total_steps  # Add total_steps to the summary

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
