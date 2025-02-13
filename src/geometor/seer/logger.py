"""
Provides a Logger class for handling logging within a Seer session.
"""

from pathlib import Path
from datetime import datetime
import json
from rich.markdown import Markdown
from rich import print


class Logger:
    def __init__(self, session_dir: Path):
        self.session_dir = session_dir

    def _format_banner(self, task_dir: Path, description: str) -> str:
        """Helper function to format the banner."""
        session_folder = task_dir.parent.name  # Get the session folder name
        task_folder = task_dir.name  # Get the task folder name
        return f"{session_folder} • {task_folder} • {description}"

    def log_prompt(
        self,
        task_dir: Path,
        prompt: list,
        instructions: list,
        prompt_count: int,
        description: str = "",
    ):
        prompt_file = task_dir / f"{prompt_count:03d}-prompt.md"
        banner = self._format_banner(task_dir, description)
        try:
            with open(prompt_file, "w") as f:
                f.write(f"{banner}\n")
                f.write("---\n")
                f.write("\n")
                for part in prompt:
                    f.write(str(part))
                f.write("\n")
                for part in instructions:
                    f.write(str(part))
                f.write("\n")
        except (IOError, PermissionError) as e:
            print(f"Error writing prompt to file: {e}")
            self.log_error(task_dir, f"Error writing prompt to file: {e}")

    def log_total_prompt(
        self,
        task_dir: Path,
        total_prompt: list,  # Changed to list
        prompt_count: int,
        description: str = "",
    ):
        prompt_file = task_dir / f"{prompt_count:03d}-total_prompt.md"
        banner = self._format_banner(task_dir, description)
        try:
            with open(prompt_file, "w") as f:
                f.write(f"{banner}\n")
                f.write("---\n")
                for part in total_prompt: # Iterate through the list
                    f.write(str(part))
                f.write("\n")
        except (IOError, PermissionError) as e:
            print(f"Error writing total prompt to file: {e}")
            self.log_error(task_dir, f"Error writing total prompt to file: {e}")

    def log_response(
        self,
        task_dir: Path,
        response,
        prompt_count: int,
        token_counts: dict,
        response_times: list,
        start_time,
    ):
        response_start = datetime.now()  # Capture start time
        response_file = task_dir / f"{prompt_count:03d}-response.json"
        description = "Response" # description for banner

        # Get token counts and update totals (passed in)
        metadata = response.to_dict().get("usage_metadata", {})
        token_counts["prompt"] += metadata.get("prompt_token_count", 0)
        token_counts["candidates"] += metadata.get("candidates_token_count", 0)
        token_counts["total"] += metadata.get("total_token_count", 0)
        token_counts["cached"] += metadata.get("cached_content_token_count", 0)

        response_end = datetime.now()  # Capture end time
        response_time = (response_end - response_start).total_seconds()
        total_elapsed = (response_end - start_time).total_seconds()
        response_times.append(response_time)  # Append to passed in list

        # Prepare the response data dictionary
        response_data = response.to_dict()
        response_data["token_totals"] = token_counts.copy()
        response_data["timing"] = {
            "response_time": response_time,
            "total_elapsed": total_elapsed,
            "response_times": response_times.copy(),
        }

        try:
            with open(response_file, "w") as f:
                json.dump(response_data, f, indent=2)
        except (IOError, PermissionError) as e:
            print(f"Error writing response JSON to file: {e}")
            self.log_error(task_dir, f"Error writing response JSON to file: {e}")

        # Unpack the response and write elements to a markdown file
        response_md_file = task_dir / f"{prompt_count:03d}-response.md"
        banner = self._format_banner(task_dir, description)

        try:
            with open(response_md_file, "w") as f:
                f.write(f"{banner}\n")
                f.write("---\n")

                if hasattr(response.candidates[0].content, "parts"):
                    for part in response.candidates[0].content.parts:
                        if part.text:
                            f.write(part.text + "\n")
                        if part.executable_code:
                            f.write("code_execution:\n")
                            f.write(
                                f"```python\n{part.executable_code.code}\n```\n"
                            )
                        if part.code_execution_result:
                            f.write(
                                f"code_execution_result: {part.code_execution_result.outcome}\n"
                            )
                            f.write(
                                f"```\n{part.code_execution_result.output}\n```\n"
                            )
                        if part.function_call:
                            f.write("function_call:\n")
                            f.write(part.function_call.name + "\n")
                            #  We do not call functions here

                f.write("\n")

                # Include token totals and timing information (from response_data)
                f.write("Token Totals:\n")
                f.write(f"  Prompt: {response_data['token_totals']['prompt']}\n")
                f.write(f"  Candidates: {response_data['token_totals']['candidates']}\n")
                f.write(f"  Total: {response_data['token_totals']['total']}\n")
                f.write(f"  Cached: {response_data['token_totals']['cached']}\n")
                f.write("Timing:\n")
                f.write(f"  Response Time: {response_data['timing']['response_time']}s\n")
                f.write(f"  Total Elapsed: {response_data['timing']['total_elapsed']}s\n")

        except (IOError, PermissionError) as e:
            print(f"Error writing response Markdown to file: {e}")
            self.log_error(task_dir, f"Error writing response Markdown to file: {e}")

    def log_error(self, task_dir: Path, error_message: str, context: str = ""):
        error_log_file = self.session_dir / "error_log.txt"  # Log to session dir
        try:
            with open(error_log_file, "a") as f:
                f.write(f"[{datetime.now().isoformat()}] ERROR: {error_message}\n")
                if context:
                    f.write(f"Context: {context}\n")
                f.write("\n")
        except (IOError, PermissionError) as e:
            print(f"FATAL: Error writing to error log: {e}")
            print(f"Attempted to log: {error_message=}, {context=}")

    def display_prompt(self, prompt, instructions, prompt_count):
        """Displays the prompt and instructions using rich.markdown.Markdown."""
        markdown_text = f"# PROMPT {prompt_count}\n\n"
        for part in prompt:
            markdown_text += str(part) + "\n"

        for part in instructions:
            markdown_text += str(part) + "\n"

        markdown = Markdown(markdown_text)
        print(markdown)

    def display_response(self, response_parts, prompt_count):
        """Displays the response using rich.markdown.Markdown."""
        markdown_text = f"# RESPONSE {prompt_count}\n\n"
        for part in response_parts:
            markdown_text += str(part) + "\n"

        markdown = Markdown(markdown_text)
        print(markdown)
