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
from rich import print


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
            self._write_context_files(
                config["dreamer"]["system_context_file"],
                config["coder"]["system_context_file"],
                config["task_context_file"],
            )
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

    def _write_context_files(
        self,
        dreamer_system_context_file: str,
        coder_system_context_file: str,
        task_context_file: str,
    ):
        with open(dreamer_system_context_file, "r") as f:
            dreamer_system_context = f.read().strip()
        with open(coder_system_context_file, "r") as f:
            coder_system_context = f.read().strip()
        with open(task_context_file, "r") as f:
            task_context = f.read().strip()

        (self.session_dir / "dreamer_system_context.md").write_text(
            dreamer_system_context
        )
        (self.session_dir / "builder_system_context.md").write_text(
            coder_system_context
        )
        (self.session_dir / "task_context.md").write_text(task_context)

    def _format_banner(self, prompt_count: int, description: str) -> str:
        """Helper function to format the banner."""
        session_folder = self.task_dir.parent.name  # Get the session folder name
        task_folder = self.task_dir.name  # Get the task folder name
        return f"# {task_folder} • {prompt_count:03d} • {description}\n"

    def log_prompt(
        self,
        prompt: list,
        instructions: list,
        prompt_count: int,
        description: str = "",
    ):
        prompt_file = self.task_dir / f"{prompt_count:03d}-prompt.md"
        banner = self._format_banner(prompt_count, description)
        image_count = 0
        try:
            with open(prompt_file, "w") as f:
                f.write(f"{banner}\n")
                f.write("---\n")
                f.write("\n")
                for i, part in enumerate(prompt):  # Use enumerate to get index
                    if hasattr(part, "save"):  # Check if it's an image
                        image_count += 1

                        image_filename = (
                            f"{prompt_count:03d}-{description}-{image_count}.png"
                        )
                        image_path = self.task_dir / image_filename
                        part.save(image_path)
                        f.write(f"![Image]({image_filename})\n")
                    else:
                        f.write(str(part))
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

    def log_response(
        self,
        response,
        response_parts,
        prompt_count: int,
        token_counts: dict,
        response_times: list,
        start_time,
    ):
        response_start = datetime.now()
        response_file = self.task_dir / f"{prompt_count:03d}-response.json"
        description = "Response"

        # Get token counts and update totals (passed in)
        metadata = response.to_dict().get("usage_metadata", {})
        token_counts["prompt"] += metadata.get("prompt_token_count", 0)
        token_counts["candidates"] += metadata.get("candidates_token_count", 0)
        token_counts["total"] += metadata.get("total_token_count", 0)
        token_counts["cached"] += metadata.get("cached_content_token_count", 0)

        response_end = datetime.now()
        response_time = (response_end - response_start).total_seconds()
        total_elapsed = (response_end - start_time).total_seconds()
        response_times.append(response_time)

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
            self.log_error(f"Error writing response JSON to file: {e}")

        # Unpack the response and write elements to a markdown file
        response_md_file = self.task_dir / f"{prompt_count:03d}-response.md"
        banner = self._format_banner(prompt_count, description)

        with open(response_md_file, "w") as f:
            f.write(f"{banner}\n")
            f.write("---\n")
            f.write("\n".join(response_parts))

        # Call display_response here
        self.display_response(response_parts, prompt_count, description, response_data)

    def log_error(self, error_message: str, context: str = ""):
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
        respdata: dict,
    ):
        """Displays the response using rich.markdown.Markdown."""
        #  banner = self._format_banner(prompt_count, description)  # Use the banner
        markdown_text = f"\n## RESPONSE\n\n"  # Include banner in Markdown

        # Extract test_results_str, if present, and remove from response_parts
        #  test_results_str = ""
        #  if response_parts and isinstance(response_parts[-1], str):
        #  test_results_str = response_parts.pop()

        for part in response_parts:
            markdown_text += str(part) + "\n"

        # Add usage metadata
        usage = respdata.get("usage_metadata", {})
        if usage:
            markdown_text += "\n---\n\n**Usage Meta**\n\n```json\n"
            markdown_text += json.dumps(usage, indent=2)
            markdown_text += "\n```\n"

        markdown = Markdown(markdown_text)
        print()
        print(markdown)

        # Display test results here, after usage metadata
        #  if test_results_str:
        #  self.display_test_results(test_results_str, prompt_count)

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

    def gather_response_data(self, task_dir):
        """Gathers data from all response.json files in the task directory."""
        respdata = []
        for respfile in task_dir.glob("*-response.json"):
            try:
                with open(respfile, "r") as f:
                    data = json.load(f)
                    respdata.append(data)
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error reading or parsing {respfile}: {e}")
                self.log_error(f"Error reading or parsing {respfile}: {e}")
        return respdata

    def create_summary_report(self, respdata, task_dir):
        """Creates a summary report (Markdown and JSON) of token usage, timing, and test results."""

        # Aggregate data
        total_tokens = {"prompt": 0, "candidates": 0, "total": 0, "cached": 0}
        total_response_time = 0
        all_response_times = []
        test_results = []

        for data in respdata:
            for key in total_tokens:
                total_tokens[key] += data["token_totals"].get(key, 0)
            total_response_time += data["timing"]["response_time"]
            all_response_times.extend(data["timing"]["response_times"])

            # Collect test results from JSON files
            for py_file in task_dir.glob("*-py_*.json"):
                try:
                    with open(py_file, 'r') as f:
                        test_results.extend(json.load(f))
                except Exception as e:
                    print(f"Failed to load test results from {py_file}: {e}")

        # Create Markdown report
        report_md = "# Task Summary Report\n\n"
        report_md += "## Token Usage\n\n"
        report_md += "| Category        | Token Count |\n"
        report_md += "|-----------------|-------------|\n"
        report_md += f"| Prompt Tokens   | {total_tokens['prompt']} |\n"
        report_md += f"| Candidate Tokens| {total_tokens['candidates']} |\n"
        report_md += f"| Total Tokens    | {total_tokens['total']} |\n"
        report_md += f"| Cached Tokens   | {total_tokens['cached']} |\n\n"

        report_md += "## Timing\n\n"
        report_md += "| Metric          | Time (s) |\n"
        report_md += "|-----------------|----------|\n"
        report_md += f"| Total Resp Time | {total_response_time:.4f} |\n"
        report_md += f"| Avg Resp Time   | {sum(all_response_times) / len(all_response_times) if all_response_times else 0:.4f} |\n\n"
        #  report_md += f"| All Response Times | {all_response_times} |\n\n"

        report_md += "## Test Results\n\n"
        if test_results:
             for result in test_results:
                if 'example' in result:
                    report_md += f"### Example {result['example']}\n"
                    report_md += f"- **Status:** {result['status']}\n"
                    report_md += f"- **Input:**\n```\n{result['input']}\n```\n"
                    report_md += f"- **Expected Output:**\n```\n{result['expected_output']}\n```\n"
                    if 'transformed_output' in result:
                        report_md += f"- **Transformed Output:**\n```\n{result['transformed_output']}\n```\n"
                elif 'captured_output' in result:
                    report_md += f"### Captured Output\n```\n{result['captured_output']}\n```\n"
                elif 'code_execution_error' in result:
                    report_md += f"### Code Execution Error\n```\n{result['code_execution_error']}\n```\n"
        else:
            report_md += "No test results found.\n"

        # Create JSON report
        report_json = {
            "token_usage": total_tokens,
            "timing": {
                "total_response_time": total_response_time,
                "all_response_times": all_response_times,
            },
            "test_results": test_results,
        }

        # Save reports
        report_md_file = task_dir / "summary_report.md"
        report_json_file = task_dir / "summary_report.json"

        self._write_to_file(report_md_file, report_md)
        with open(report_json_file, "w") as f:
            json.dump(report_json, f, indent=2)

        # Display report
        self.display_response(
            [report_md], 0, "Task Summary", {}
        )  # prompt_count=0, as this isn't a regular prompt/response

    def _write_to_file(self, file_name, content):
        """Writes content to a file in the task directory."""
        file_path = self.task_dir / file_name  # Use self.task_dir
        try:
            with open(file_path, "w") as f:
                f.write(content)
        except (IOError, PermissionError) as e:
            print(f"Error writing to file {file_name}: {e}")
            self.log_error(f"Error writing to file {file_name}: {e}")
