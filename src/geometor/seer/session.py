"""
Manages a session for interacting with the Seer, handling logging, and task execution.

The Session class encapsulates a single run of the Seer, including configuration,
task management, output directory handling, and interaction with the Seer instance.
It also provides methods for saving images, logging prompts and responses, and
handling errors.
"""

from pathlib import Path
from datetime import datetime
import json

from geometor.seer.seer import Seer
from geometor.seer.logger import Logger


class Session:
    def __init__(self, config: dict, tasks: list):
        self.config = config
        self.tasks = tasks

        self.output_dir = Path(config["output_dir"])
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.timestamp = datetime.now().strftime("%y.%j.%H%M%S")  # Generate timestamp

        self.session_dir = self.output_dir / self.timestamp
        self.session_dir.mkdir(parents=True, exist_ok=True)

        # Write system and task context to files
        self._write_context_files(config["system_context_file"], config["task_context_file"])

        # Initialize Logger
        self.logger = Logger(self.session_dir)

        self.seer = Seer(
            config=config,
            session=self,
        )

        # Log the configuration
        with open(self.session_dir / "config.json", "w") as f:
            json.dump(config, f, indent=2)

    def _write_context_files(self, system_context_file: str, task_context_file: str):
        with open(system_context_file, "r") as f:
            system_context = f.read().strip()
        with open(task_context_file, "r") as f:
            task_context = f.read().strip()

        (self.session_dir / "system_context.md").write_text(system_context)
        (self.session_dir / "task_context.md").write_text(task_context)

    def run(self):
        for task in self.tasks.puzzles:
            self.task_dir = self.session_dir / task.id
            self.task_dir.mkdir(parents=True, exist_ok=True)
            self.seer.solve(task) # Call generalized solve
