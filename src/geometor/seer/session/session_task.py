from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import datetime
from pathlib import Path
import json
import traceback
from PIL import Image

if TYPE_CHECKING:
    from geometor.seer.session import (
        Session,
        TaskStep,
    )

from geometor.seer.tasks.tasks import Task

class SessionTask:
    def __init__(self, session: Session, task: Task):
        self.session = session  # parent
        self.task = task
        self.dir = session.session_dir / task.id
        self.dir.mkdir(parents=True, exist_ok=True)
        self.steps = []
        self.errors = {}

        try:
            task_image = task.to_image()

            image_path = self.dir / "task.png"
            task_image.save(image_path)

            task_json_str = task.nice_json_layout()
            task_json_file = self.dir / "task.json"
            task_json_file.write_text(task_json_str)

        except Exception as e:
            self.log_error(e)

    def log_error(self, e: Exception, context: str = ""):
        # TODO: refactor to generic function
        error_content = {
            "context": context,
            "datetime": datetime.now().isoformat(),
            "stack_trace": traceback.format_exc(),
            "exception": e,
        }
        error_index = len(self.errors) + 1

        error_log_file = self.dir / f"error_{error_index:03d}.json"

        try:
            with open(error_log_file, "w") as f:
                json.dump(error_content, f, indent=2)
        except Exception as e:
            # TODO: print not supported in textual
            print(f"FATAL: Error writing to error log: {e}")
            print(f"Attempted to log: {e=}, {context=}")

        self.errors[error_log_file.name] = error_content

    def add_step(self, history, prompt, instructions):
        task_step = TaskStep(self, history, prompt, instructions)
        self.steps.append(task_step)
        return task_step

    def summarize():
        summary_file = self.dir / "task_summary.json"
        summary = {}
        try:
            with open(summary_file, "w") as f:
                json.dump(summary, f, indent=2)
        except (IOError, PermissionError) as e:
            print(f"Error writing response JSON to file: {e}")
            self.log_error(f"Error writing response JSON to file: {e}")
