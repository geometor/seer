# src/geometor/seer/session/session.py
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
import re  # Import the 're' module

from geometor.seer.session.summary import summarize_session, summarize_task


class Session:
    def __init__(self, config: dict, tasks: list):
        self.config = config
        self.tasks = tasks

        self.output_dir = Path(config["output_dir"])
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.timestamp = datetime.now().strftime("%y.%j.%H%M")  # Generate timestamp

        self.session_dir = self.output_dir / self.timestamp
        self.session_dir.mkdir(parents=True, exist_ok=True)

        # Initialize task_dir to session_dir for initial context display
        self.task_dir = self.session_dir

        #  Write system and task context to files
        try:
            self._write_context_files()
            #  self._write_context_files(
            #      config["roles"]["dreamer"]["system_context_file"],
            #      config["roles"]["coder"]["system_context_file"],
            #      config["task_context_file"],
            #  )
        except (FileNotFoundError, IOError, PermissionError) as e:
            print(f"Error writing context files: {e}")
            self.log_error(f"Error writing context files: {e}")

        try:
            with open(self.session_dir / "config.json", "w") as f:
                json.dump(config, f, indent=2)
        except (IOError, PermissionError) as e:
            print(f"Error writing config file: {e}")
            self.log_error(f"Error writing config file: {e}")

        self.display_config()  # display config at start of session

    #  def _write_context_files(
    #      self,
    #      dreamer_system_context_file: str,
    #      coder_system_context_file: str,
    #      task_context_file: str,
    #  ):
    def _write_context_files(self):
        """Writes system context files for each role and the task context."""
        for role_name, role_config in self.config["roles"].items():
            system_context_file = role_config["system_context_file"]
            with open(system_context_file, "r") as f:
                system_context = f.read().strip()
            (self.session_dir / f"{role_name}_system_context.md").write_text(
                system_context
            )

        with open(self.config["task_context_file"], "r") as f:
            task_context = f.read().strip()
        (self.session_dir / "task_context.md").write_text(task_context)

        #  with open(dreamer_system_context_file, "r") as f:
        #      dreamer_system_context = f.read().strip()
        #  with open(coder_system_context_file, "r") as f:
        #      coder_system_context = f.read().strip()
        #  with open(task_context_file, "r") as f:
        #      task_context = f.read().strip()

        #  (self.session_dir / "dreamer_system_context.md").write_text(
        #      dreamer_system_context
        #  )
        #  (self.session_dir / "builder_system_context.md").write_text(
        #      coder_system_context
        #  )
        #  (self.session_dir / "task_context.md").write_text(task_context)

    def _format_banner(self, prompt_count: int, description: str) -> str:
        """Helper function to format the banner."""
        session_folder = self.task_dir.parent.name  # Get the session folder name
        task_folder = self.task_dir.name  # Get the task folder name
        return f"# {task_folder} • {prompt_count:03d} • {description}\n"

    def log_prompt_image(self, image, prompt_count: int, description: str):
        """Saves an image and returns its filename."""
        image_filename = f"{prompt_count:03d}-{description}.png"
        image_path = self.task_dir / image_filename
        image.to_image().save(image_path)
        return image_filename

    def log_prompt(
        self,
        prompt: list,
        instructions: list,
        prompt_count: int,
        description: str = "",
    ):
        prompt_file = self.task_dir / f"{prompt_count:03d}-prompt.md"
        banner = self._format_banner(prompt_count, description)
        image_count = 0  # Keep track of images within the prompt
        try:
            with open(prompt_file, "w") as f:
                f.write(f"{banner}\n")
                f.write("---\n")
                f.write("\n")
                for i, part in enumerate(prompt):  # Use enumerate to get index
                    #  if hasattr(part, "save"):  # Check if it's an image # REMOVE
                    if isinstance(part, str) and part.startswith("![Image]"): # NEW
                        # Assume it's already an image filename string
                        f.write(part) # NEW
                    #  if hasattr(part, "save"):  # Check if it's an image # REMOVE
                    #      image_count += 1 # REMOVE

                    #      image_filename = ( # REMOVE
                    #          f"{prompt_count:03d}-{description}-{image_count}.png" # REMOVE
                    #      ) # REMOVE
                    #      image_path = self.task_dir / image_filename # REMOVE
                    #      part.save(image_path) # REMOVE
                    #      f.write(f"![Image]({image_filename})\n") # REMOVE
                    else: # NEW
                        f.write(str(part)) # NEW
                #  for i, part in enumerate(prompt):  # Use enumerate to get index # REMOVE
                #      if hasattr(part, "save"):  # Check if it's an image # REMOVE
                #          image_count += 1 # REMOVE

                #          image_filename = ( # REMOVE
                #              f"{prompt_count:03d}-{description}-{image_count}.png" # REMOVE
                #          ) # REMOVE
                #          image_path = self.task_dir / image_filename # REMOVE
                #          part.save(image_path) # REMOVE
                #          f.write(f"![Image]({image_filename})\n") # REMOVE
                #      else: # REMOVE
                #          f.write(str(part)) # REMOVE
                f.write("\n")
                for part in instructions:
                    f.write(str(part))
                f.write("\n")
        except (IOError, PermissionError) as e:
            print(f"Error writing prompt to file: {e}")
            self.log_error(f"Error writing prompt to file: {e}")

        # Call display_prompt here
        self.display_prompt(prompt, instructions, prompt_count, description)

    def log_total_prompt(
        self,
        total_prompt: list,
        prompt_count: int,
        description: str = "",
    ):
        prompt_file = self.task_dir / f"{prompt_count:03d}-total_prompt.md"
        banner = self._format_banner(prompt_count, description)
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
        prompt_count,
        response_time,
    ):
        response_start = datetime.now()
        response_file = self.task_dir / f"{prompt_count:03d}-response.json"
        description = "Response"

        # Get token counts and update totals (passed in)
        metadata = response.to_dict().get("usage_metadata", {})
        #  token_counts["prompt"] += metadata.get("prompt_token_count", 0)
        #  token_counts["candidates"] += metadata.get("candidates_token_count", 0)
        #  token_counts["total"] += metadata.get("total_token_count", 0)
        #  token_counts["cached"] += metadata.get("cached_content_token_count", 0)

        #  response_end = datetime.now()
        #  response_time = (response_end - response_start).total_seconds()
        #  total_elapsed = (response_end - start_time).total_seconds()
        #  response_times.append(response_time)

        # Prepare the response data dictionary
        response_data = response.to_dict()
        #  response_data["token_totals"] = token_counts.copy()
        response_data["timing"] = {
            "response_time": response_time,
            #  "total_elapsed": total_elapsed,
            #  "response_times": response_times.copy(),
        }
        response_data["response_file"] = str(
            response_file.name
        )  # Add filename for report

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
        prompt_count: int,
        token_counts: dict,
        response_times: list,
        start_time,
        description,
        elapsed_time,
    ):
        # Unpack the response and write elements to a markdown file
        response_md_file = self.task_dir / f"{prompt_count:03d}-response.md"
        banner = self._format_banner(prompt_count, description)

        try:  # Added try-except block
            with open(response_md_file, "w") as f:
                f.write(f"{banner}\n")
                f.write("---\n")
                f.write("\n".join(response_parts))
        except (IOError, PermissionError) as e:  # Catch potential write errors
            print(f"Error writing response Markdown to file: {e}")
            self.log_error(f"Error writing response Markdown to file: {e}")

        # Call display_response here
        self.display_response(
            response_parts, prompt_count, description, response.to_dict(), elapsed_time
        )

    def log_error(self, error_message: str, context: str = ""):
        error_log_file = self.session_dir / "error_log.txt"  # Log to session dir
        try:
            with open(error_log_file, "a") as f:
                f.write(f"[{datetime.now().isoformat()}] ERROR: {error_message}\n")
                if context:
                    if isinstance(context, str):
                        f.write(f"Context: {context}\n")
                    else:
                        f.write(f"Context: {str(context)}\n")
                f.write("\n")
        except (IOError, PermissionError) as e:
            print(f"FATAL: Error writing to error log: {e}")
            print(f"Attempted to log: {error_message=}, {context=}")

    def display_prompt(
        self, prompt: list, instructions: list, prompt_count: int, description: str
    ):
        """Displays the prompt and instructions using rich.markdown.Markdown."""
        banner = self._format_banner(prompt_count, description)  # Use the banner
        markdown_text = f"\n{banner}\n\n"  # Include banner in Markdown
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
        banner = self._format_banner(prompt_count, description)  # Use the banner
        markdown_text = f"\n## RESPONSE\n\n"  # Include banner in Markdown

        for part in response_parts:
            markdown_text += str(part) + "\n"

        # Add usage metadata
        usage = respdict.get("usage_metadata", {})
        if usage:
            markdown_text += "\n---\n\n**Usage Meta**\n\n```json\n"
            markdown_text += json.dumps(usage, indent=2)
            markdown_text += "\n```\n"

        # Add timing metadata
        timing = respdict.get("timing", {})
        if timing:
            markdown_text += "\n**Timing Meta**\n\n```json\n"
            markdown_text += json.dumps(timing, indent=2)
            markdown_text += "\n```\n"
            # Add elapsed time display here:
            #  total_elapsed_time = timing.get("total_elapsed") # REMOVE
            #  if total_elapsed_time is not None: # REMOVE
            #      markdown_text += f"\n**Total Elapsed Time:** {total_elapsed_time:.4f} seconds\n" # REMOVE
        # Use elapsed_time directly
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

    def _write_extracted_content( # REMOVE
        self, text, prompt_count, extracted_file_counts, task, verifier # REMOVE
    ): # REMOVE
        """Extracts content enclosed in triple backticks and writes it to files.""" # REMOVE
        matches = re.findall(r"```(\w+)?\n(.*?)\n```", text, re.DOTALL) # REMOVE
        for file_type, content in matches: # REMOVE
            file_type = file_type.lower() if file_type else "txt" # REMOVE
            if file_type == "python": # REMOVE
                file_type = "py"  # Correct extension # REMOVE
            if file_type not in extracted_file_counts: # REMOVE
                file_type = "txt" # REMOVE

            extracted_file_counts[file_type] += 1 # REMOVE
            count = extracted_file_counts[file_type] # REMOVE
            file_name = f"{prompt_count:03d}-{file_type}_{count:02d}.{file_type}" # REMOVE
            file_path = self.task_dir / file_name # REMOVE

            self._write_to_file(file_name, content) # REMOVE

            # If it's a Python file, also run tests # REMOVE
            if file_type == "py": # REMOVE
                test_results = verifier.test_code(content, file_path, task)  # Pass task # REMOVE
                # Write test results to file # REMOVE
                test_results_file = Path(f"{file_path.stem()}.md") # REMOVE
                self._write_to_file(test_results_file, "".join(test_results)) # REMOVE

                # TODO: review the test results - # REMOVE

    def _write_code_text( # NEW
        self, extracted_code, prompt_count, extracted_file_counts, task, verifier # NEW
    ):  # NEW
        """Writes extracted code blocks to files and runs tests on Python files.""" # NEW
        for file_type, content in extracted_code: # NEW
            if file_type not in extracted_file_counts: # NEW
                file_type = "txt"  # Default to txt for unknown types # NEW

            extracted_file_counts[file_type] += 1 # NEW
            count = extracted_file_counts[file_type] # NEW
            file_name = f"{prompt_count:03d}-{file_type}_{count:02d}.{file_type}" # NEW
            file_path = self.task_dir / file_name # NEW

            self._write_to_file(file_name, content) # NEW

            if file_type == "py": # NEW
                test_results = verifier.test_code(content, file_path, task) # NEW
                test_results_file = Path( # NEW
                    f"{file_path.stem()}.md" # NEW
                )  # Create Path object for .md file # NEW
                self._write_to_file(test_results_file, "".join(test_results)) # NEW

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
