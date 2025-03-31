from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import datetime, timedelta
from pathlib import Path
import json
import traceback
from PIL import Image

if TYPE_CHECKING:
    from geometor.seer.session.session import Session
    from geometor.seer.session.session_task import SessionTask
    from geometor.seer.session.task_step import TaskStep


class Level:
    def __init__(self, parent: Level | None, name: str):
        self.parent = parent
        self.name = name
        self.dir = self._get_dir()
        self.dir.mkdir(parents=True, exist_ok=True)
        self.errors = {}
        self.start_time = datetime.now()  # Store start time
        self.end_time = None  # Initialize end_time
        self.duration_seconds = None  # Initialize
        # self.duration = None # REMOVE

    def _get_dir(self) -> Path:
        if self.parent:
            return self.parent.dir / self.name
        else:  # Special case for Session, which has no parent
            return Path(self.name)

    def log_error(self, e: Exception, context: str = ""):
        error_content = {
            "context": context,
            "datetime": datetime.now().isoformat(),
            "stack_trace": traceback.format_exc(),
            "exception": str(e),
        }
        error_index = len(self.errors) + 1

        error_log_file = f"error_{error_index:03d}.json"

        txt_content = f"""
ERROR

{ context }
{ str(e) }
{ error_content["stack_trace"] }
"""
        #  print(txt_content)

        self._write_to_json(error_log_file, error_content)

        self.errors[error_log_file] = error_content


        error_log_file = f"error_{error_index:03d}.txt"
        self._write_to_file(error_log_file, txt_content)


    def _write_to_file(self, file_name: str, content: str, mode: str = "w"):
        """Writes content to a file in the task directory."""
        file_path = self.dir / file_name
        try:
            # Use the provided mode when opening the file
            with open(file_path, mode) as f:
                f.write(content)
        except Exception as e:
            # Use repr(e) for potentially more detailed error info during logging
            self.log_error(e, f"Error writing to file: {file_path} with mode '{mode}'. Exception: {repr(e)}")

    def _write_to_json(self, file_name: str, content: object):
        """Writes content to a file in the task directory."""
        file_path = self.dir / file_name
        try:
            with open(file_path, "w") as f:
                json.dump(content, f, indent=2)
        except Exception as e:
            # Use repr(e) for potentially more detailed error info during logging
            self.log_error(e, f"Error writing to json: {file_path}. Exception: {repr(e)}")

    def log_markdown(
        self,
        name: str,
        content: list,
    ):
        markdown_file = self.dir / f"{name}.md"
        try:
            with open(markdown_file, "w") as f:
                for i, part in enumerate(content):
                    if isinstance(part, Image.Image):
                        image_filename = f"{name}_{i:03d}.png"
                        image_path = self.dir / image_filename
                        part.save(image_path)
                        f.write(f"!\\[image {i}]({image_filename})\n")
                    else:
                        f.write(str(part))
        except Exception as e:
            print(f"Error writing prompt to file: {e}")
            # Use repr(e) for potentially more detailed error info during logging
            self.log_error(e, f"Error writing markdown to file: {markdown_file}. Exception: {repr(e)}")

    @staticmethod
    def _format_duration(seconds: float | None) -> str:
        """Formats duration in HH:MM:SS format."""
        if seconds is None or seconds < 0:
            return "-"
        delta = timedelta(seconds=int(seconds)) # Convert to int for timedelta
        total_seconds = int(delta.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        # Format as HH:MM:SS
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def summarize(self):
        # Base implementation.  Subclasses should override and call super().summarize()
        self.end_time = datetime.now()  # Store end time
        self.duration_seconds = (
            (self.end_time - self.start_time).total_seconds()
            if self.start_time
            else None
        )
        # self.duration = (
        #     self._format_duration(self.duration_seconds)
        #     if self.duration_seconds is not None
        #     else None
        # )

        summary = {
            "errors": {},
            "duration_seconds": self.duration_seconds,  # Add duration in seconds
            # "duration": self.duration,  # Add formatted duration # REMOVE
        }
        summary["errors"]["count"] = len(self.errors)
        summary["errors"]["types"] = list(self.errors.keys())
        return summary
