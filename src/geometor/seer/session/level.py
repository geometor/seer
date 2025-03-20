from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import datetime
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

        print("ERROR")
        print(context)
        print(str(e))
        print(error_content["stack_trace"])

        self._write_to_json(error_log_file, error_content)

        self.errors[error_log_file] = error_content

    def _write_to_file(self, file_name: str, content: str):
        """Writes content to a file in the task directory."""
        file_path = self.dir / file_name
        try:
            with open(file_path, "w") as f:
                f.write(content)
        except Exception as e:
            self.log_error(e, f"Error writing to file: {file_path}")

    def _write_to_json(self, file_name: str, content: object):
        """Writes content to a file in the task directory."""
        file_path = self.dir / file_name
        try:
            with open(file_path, "w") as f:
                json.dump(content, f, indent=2)
        except Exception as e:
            self.log_error(e, f"Error writing to json: {file_path}")

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
            self.log_error(f"Error writing prompt to file: {e}")

    def summarize(self):
        # Base implementation.  Subclasses should override and call super().summarize()
        summary = {
            "errors": {},
        }
        summary["errors"]["count"] = len(self.errors)
        summary["errors"]["types"] = list(self.errors.keys())
        return summary
