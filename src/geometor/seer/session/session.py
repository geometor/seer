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
from rich.markdown import Markdown
from rich.table import Table
from rich.console import Console
from rich import print
import re  
import contextlib
import traceback

from geometor.seer.session.summary import summarize_session, summarize_task
import geometor.seer.verifier as verifier


class TaskStep:
    def __init__(self, session_task: SessionTask, title)
        self.session_task = session_task
        self.title = title
        self.index = f"{len(session_task.steps):03d}"
        self.step_dir = session_task.task_dir / self.index
        self.step_dir.mkdir(parents=True, exist_ok=True)

        self.extracted_file_counts = {"py": 0, "yaml": 0, "json": 0, "txt": 0}

    def add_results(self, response, response_parts, extracted_code_list):
        # TODO: log files
        return

    def log_error(self, e: Exception, context: str = ""):
        error_log_file = self.task_dir / "error_log.txt"  
        print(f"Caught a general exception: {type(e).__name__} - {e}")

        # Capture stack trace for general exceptions too
        stack_trace = traceback.format_exc()
        try:
            with open(error_log_file, "a") as f:
                f.write(f"[{datetime.now().isoformat()}] ERROR: {e}\n")
                if context:
                    if isinstance(context, str):
                        f.write(f"Context: {context}\n")
                    else:
                        f.write(f"Context: {str(context)}\n")
                    f.write("\n")
                if stack_trace:
                    f.write(f"{stack_trace}\n")
                    f.write("\n")
        except (IOError, PermissionError) as e:
            print(f"FATAL: Error writing to error log: {e}")
            print(f"Attempted to log: {e=}, {context=}")

    def log_prompt_image(self, image, description: str):
        """Saves an image and returns its filename."""
        image_filename = f"{description}.png"
        image_path = self.step_dir / image_filename
        image.to_image().save(image_path)
        return image_filename

    def summarize():
        summary_file = self.step_dir / "step_summary.json"
        summary = {}
        try:
            with open(summary_file, "w") as f:
                json.dump(summary, f, indent=2)
        except (IOError, PermissionError) as e:
            print(f"Error writing response JSON to file: {e}")
            self.log_error(f"Error writing response JSON to file: {e}")


    def _format_banner(self, step_index: int, description: str) -> str:
        """Helper function to format the banner."""
        task_folder = self.step_dir.parent.name  
        return f"# {task_folder} • {step_index} • {description}\n"

    def log_prompt(
        self,
        prompt: list,
        instructions: list,
        description: str = "",
    ):
        prompt_file = self.step_dir / f"prompt.md"
        banner = self._format_banner(self.index, description)
        try:
            with open(prompt_file, "w") as f:
                f.write(f"{banner}\n")
                f.write("---\n")
                f.write("\n")
                for i, part in enumerate(prompt):
                    if isinstance(part, str) and part.startswith("![Image]"):
                        f.write(part)
                    else:
                        f.write(str(part))
                f.write("\n")
                for part in instructions:
                    f.write(str(part))
                f.write("\n")
        except (IOError, PermissionError) as e:
            print(f"Error writing prompt to file: {e}")
            self.log_error(f"Error writing prompt to file: {e}")

        self.display_prompt(prompt, instructions, self.index, description)

    def log_total_prompt(
        self,
        total_prompt: list,
        description: str = "",
    ):
        prompt_file = self.step_dir / f"total_prompt.md"
        banner = self._format_banner(self.index, description)
        try:
            with open(prompt_file, "w") as f:
                f.write(f"{banner}\n")
                f.write("---\n")
                for part in total_prompt:
                    f.write(str(part))
                f.write("\n")
        except (IOError, PermissionError) as e:
            print(f"Error writing total prompt to file: {e}")
            self.log_error(f"Error writing total prompt to file: {e}")

    def log_response_json(
        self,
        response,
        response_time,
    ):
        response_file = self.step_dir / f"response.json"
        description = "Response"

        response_data = response.to_dict()
        response_data["response_time"] = response_time
        #  response_data["response_file"] = str(response_file.name)

        try:
            with open(response_file, "w") as f:
                json.dump(response_data, f, indent=2)
        except (IOError, PermissionError) as e:
            print(f"Error writing response JSON to file: {e}")
            self.log_error(f"Error writing response JSON to file: {e}")

    def log_response_md(
        self,
        response,
        response_parts,
        description,
        elapsed_time,
    ):
        response_md_file = self.step_dir / f"response.md"
        banner = self._format_banner(self.index, description)

        try:  
            with open(response_md_file, "w") as f:
                f.write(f"{banner}\n")
                f.write("---\n")
                f.write("\n".join(response_parts))
        except (IOError, PermissionError) as e:  
            print(f"Error writing response Markdown to file: {e}")
            self.log_error(f"Error writing response Markdown to file: {e}")

        self.display_response(
            response_parts, self.index, description, response.to_dict(), elapsed_time
        )


class SessionTask:
    def __init__(self, session, task):
        self.session = session
        self.task = task
        self.task_dir = session.session_dir / task.id
        self.task_dir.mkdir(parents=True, exist_ok=True)
        self.steps = []

        try:
            task_image = task.to_image()

            image_path = self.task_dir / "task.png"
            task_image.save(image_path)

            task_json_str = task.nice_json_layout()
            task_json_file = self.task_dir / "task.json"
            task_json_file.write_text(task_json_str)

        except Exception as e:
            self.session.log_error(e)

    def log_error(self, e: Exception, context: str = ""):
        error_log_file = self.task_dir / "error_log.txt"  
        print(f"Caught a general exception: {type(e).__name__} - {e}")

        # Capture stack trace for general exceptions too
        stack_trace = traceback.format_exc()
        try:
            with open(error_log_file, "a") as f:
                f.write(f"[{datetime.now().isoformat()}] ERROR: {e}\n")
                if context:
                    if isinstance(context, str):
                        f.write(f"Context: {context}\n")
                    else:
                        f.write(f"Context: {str(context)}\n")
                    f.write("\n")
                if stack_trace:
                    f.write(f"{stack_trace}\n")
                    f.write("\n")
        except (IOError, PermissionError) as e:
            print(f"FATAL: Error writing to error log: {e}")
            print(f"Attempted to log: {e=}, {context=}")

    def add_step(self, history, prompt, instructions):
        task_step = TaskStep(self, history, prompt, instructions)
        self.steps.append(task_step)
        return task_step


    def summarize():
        summary_file = self.task_dir / "task_summary.json"
        summary = {}
        try:
            with open(summary_file, "w") as f:
                json.dump(summary, f, indent=2)
        except (IOError, PermissionError) as e:
            print(f"Error writing response JSON to file: {e}")
            self.log_error(f"Error writing response JSON to file: {e}")


class Session:
    def __init__(self, config: dict):
        self.config = config
        self.tasks = {}

        self.output_dir = Path(config["output_dir"])
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.timestamp = datetime.now().strftime("%y.%j.%H%M")  

        self.session_dir = self.output_dir / self.timestamp
        self.session_dir.mkdir(parents=True, exist_ok=True)

        self._write_context_files()

        self.display_config()  

    def add_task(self, task):
        session_task = SessionTask(self.session, task)
        self.tasks[task.id] = session_task
        return session_task

    def _write_context_files(self):
        """Writes system context files for each role and the task context."""
        try:
            for role_name, role_config in self.config["roles"].items():
                system_context_file = role_config["system_context_file"]
                with open(system_context_file, "r") as f:
                    system_context = f.read().strip()
                (self.session_dir / f"{role_name}_system_context.md").write_text(
                    system_context
                )
        except (FileNotFoundError, IOError, PermissionError) as e:
            print(f"Error writing context files: {e}")
            self.log_error(f"Error writing context files: {e}")

        try:
            with open(self.session_dir / "config.json", "w") as f:
                json.dump(self.config, f, indent=2)
        except (IOError, PermissionError) as e:
            print(f"Error writing config file: {e}")
            self.log_error(f"Error writing config file: {e}")

        with open(self.config["task_context_file"], "r") as f:
            task_context = f.read().strip()
        (self.session_dir / "task_context.md").write_text(task_context)

    def summarize():
        summary_file = self.session_dir / "session_summary.json"
        summary = {}
        try:
            with open(summary_file, "w") as f:
                json.dump(summary, f, indent=2)
        except (IOError, PermissionError) as e:
            print(f"Error writing response JSON to file: {e}")
            self.log_error(f"Error writing response JSON to file: {e}")

    def log_error(self, e: Exception, context: str = ""):
        error_log_file = self.task_dir / "error_log.txt"  
        print(f"Caught a general exception: {type(e).__name__} - {e}")

        # Capture stack trace for general exceptions too
        stack_trace = traceback.format_exc()
        try:
            with open(error_log_file, "a") as f:
                f.write(f"[{datetime.now().isoformat()}] ERROR: {e}\n")
                if context:
                    if isinstance(context, str):
                        f.write(f"Context: {context}\n")
                    else:
                        f.write(f"Context: {str(context)}\n")
                    f.write("\n")
                if stack_trace:
                    f.write(f"{stack_trace}\n")
                    f.write("\n")
        except (IOError, PermissionError) as e:
            print(f"FATAL: Error writing to error log: {e}")
            print(f"Attempted to log: {e=}, {context=}")

    def display_prompt(
        self, prompt: list, instructions: list, prompt_count: int, description: str
    ):
        """Displays the prompt and instructions using rich.markdown.Markdown."""
        banner = self._format_banner(prompt_count, description)  
        markdown_text = f"\n{banner}\n\n"  
        for part in prompt:
            markdown_text += str(part) + "\n"

        for part in instructions:
            markdown_text += str(part) + "\n"

        markdown = Markdown(markdown_text)
        print()
        print(markdown)

    def display_response(
        self,
        response_parts: list,
        prompt_count: int,
        description: str,
        respdict: dict,
        elapsed_time: float,
    ):
        """Displays the response using rich.markdown.Markdown."""
        banner = self._format_banner(prompt_count, description)  
        markdown_text = f"\n## RESPONSE\n\n"  

        for part in response_parts:
            markdown_text += str(part) + "\n"

        usage = respdict.get("usage_metadata", {})
        if usage:
            markdown_text += "\n---\n\n**Usage Meta**\n\n```json\n"
            markdown_text += json.dumps(usage, indent=2)
            markdown_text += "\n```\n"

        timing = respdict.get("timing", {})
        if timing:
            markdown_text += "\n**Timing Meta**\n\n```json\n"
            markdown_text += json.dumps(timing, indent=2)
            markdown_text += "\n```\n"
        markdown_text += f"\n**Total Elapsed Time:** {elapsed_time:.4f} seconds\n"

        markdown = Markdown(markdown_text)
        print()
        print(markdown)

    def display_config(self):
        """Displays the configuration information using rich.markdown.Markdown."""
        markdown_text = f"# {self.timestamp}\n\n"
        markdown_text += f"```yaml\n{json.dumps(self.config, indent=2)}\n```\n"
        markdown = Markdown(markdown_text)
        print()
        print(markdown)

    def display_test_results(self, test_results_str: str, prompt_count: int):
        """
        Displays the test results.
        """
        description = "Test Results"
        banner = self._format_banner(prompt_count, description)
        markdown_text = f"\n{banner}\n\n"
        markdown_text += test_results_str

        markdown = Markdown(markdown_text)
        print()
        print(markdown)

    #  def _write_extracted_content(  # REMOVE
        #  self,
        #  text,
        #  prompt_count,
        #  extracted_file_counts,
        #  task,
    #  ):  # REMOVE
        #  """Extracts content enclosed in triple backticks and writes it to files."""  # REMOVE
        #  matches = re.findall(r"```(\w+)?\n(.*?)\n```", text, re.DOTALL)  # REMOVE
        #  for file_type, content in matches:  # REMOVE
            #  file_type = file_type.lower() if file_type else "txt"  # REMOVE
            #  if file_type == "python":  # REMOVE
                #  file_type = "py"  # Correct extension # REMOVE
            #  if file_type not in extracted_file_counts:  # REMOVE
                #  file_type = "txt"  # REMOVE

            #  extracted_file_counts[file_type] += 1  # REMOVE
            #  count = extracted_file_counts[file_type]  # REMOVE
            #  file_name = (
                #  f"{prompt_count:03d}-{file_type}_{count:02d}.{file_type}"  # REMOVE
            #  )
            #  file_path = self.task_dir / file_name  # REMOVE

            #  self._write_to_file(file_name, content)  # REMOVE

            #  # If it's a Python file, also run tests # REMOVE
            #  if file_type == "py":  # REMOVE
                #  test_results = test_code(content, file_path, task)  # Pass task # REMOVE
                #  # Write test results to file # REMOVE
                #  test_results_file = Path(f"{file_path.stem()}.md")  # REMOVE
                #  self._write_to_file(test_results_file, "".join(test_results))  # REMOVE

                #  # TODO: review the test results - # REMOVE

    def _write_code_text(  
        self,
        extracted_code,
        prompt_count,
        extracted_file_counts,
    ):  
        """Writes extracted code blocks to files and runs tests on Python files."""  
        for file_type, content in extracted_code:  
            if file_type not in extracted_file_counts:  
                file_type = "txt"  # Default to txt for unknown types 

            extracted_file_counts[file_type] += 1  
            count = extracted_file_counts[file_type]  
            file_name = f"{prompt_count:03d}-{file_type}_{count:02d}.{file_type}"  
            file_path = self.task_dir / file_name  

            self._write_to_file(file_name, content)  

            return file_path

    def _write_to_file(self, file_name, content):
        """Writes content to a file in the task directory."""
        file_path = self.task_dir / file_name  # Always use task_dir
        try:
            with open(file_path, "w") as f:
                f.write(content)
        except (IOError, PermissionError) as e:
            print(f"Error writing to file {file_name}: {e}")
            self.log_error(f"Error writing to file {file_name}: {e}")

    def run_task(self, task):
        """Runs a single task."""
        print(f"Running task: {task.id}")
        self.task_dir = self.session_dir / task.id
        self.task_dir.mkdir(parents=True, exist_ok=True)
        self.seer.solve(task, self)
        summarize_task(self.task_dir, self.log_error)  # Summarize after each task

    def run_all_tasks(self):
        """Runs all tasks in the session."""
        for task in self.tasks:
            self.run_task(task)
        summarize_session(self.session_dir, self.log_error, self.display_response)
