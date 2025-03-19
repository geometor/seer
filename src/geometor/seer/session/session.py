"""
Manages a session for interacting with the Seer, handling logging, and task execution.

The Session class encapsulates a single run of the Seer, including configuration,
task management, output directory handling, and interaction with the Seer instance.
It also provides methods for saving images, logging prompts and responses, and
handling errors.
"""

from __future__ import annotations

from pathlib import Path
from datetime import datetime
import json
import re  
import contextlib
import traceback

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from geometor.seer.session.session_task import SessionTask

import geometor.seer.verifier as verifier


class Session:
    def __init__(self, config: dict):
        self.config = config
        self.tasks = {}

        self.output_dir = Path(config["output_dir"])
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.timestamp = datetime.now().strftime("%y.%j.%H%M")  

        self.dir = self.output_dir / self.timestamp
        self.dir.mkdir(parents=True, exist_ok=True)

        self._write_context_files()

        #  self.display_config()  

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

    def summarize(self):
        summary_file = self.dir / "session_summary.json"
        summary = {}
        try:
            with open(summary_file, "w") as f:
                json.dump(summary, f, indent=2)
        except (IOError, PermissionError) as e:
            print(f"Error writing response JSON to file: {e}")
            self.log_error(f"Error writing response JSON to file: {e}")

    def log_error(self, e: Exception, context: str = ""):
        # TODO: refactor to generic function
        error_content = {
                "context": context,
                "datetime": datetime.now().isoformat(),
                "stack_trace": traceback.format_exc(),
                "exception": str(e),
                }
        error_index = len(self.errors) + 1

        error_log_file = self.dir / f"error_{error_index:03d}.json"

        print("ERROR")
        print(context)
        print(str(e))
        print(error_content["stack_trace"])

        try:
            with open(error_log_file, "w") as f:
                json.dump(error_content, f, indent=2)
        except Exception as e:
            # TODO: print not supported in textual
            print(f"FATAL: Error writing to error log: {e}")
            print(f"Attempted to log: {e=}, {context=}")

        self.errors[error_log_file.name] = error_content

