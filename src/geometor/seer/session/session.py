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
#  from rich.table import Table  # Removed
#  from rich.console import Console  # Removed
from rich import print

from geometor.seer.session.summary import create_session_summary_report


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

    def log_response_json(
        self,
        response,
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
        response_data["response_file"] = str(response_file.name)  # Add filename for report

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
        description
    ):
        # Unpack the response and write elements to a markdown file
        response_md_file = self.task_dir / f"{prompt_count:03d}-response.md"
        banner = self._format_banner(prompt_count, description)

        with open(response_md_file, "w") as f:
            f.write(f"{banner}\n")
            f.write("---\n")
            f.write("\n".join(response_parts))


        #TODO: refactor with log_response_json
        # Prepare the response data dictionary
        response_data = response.to_dict()
        #  response_data["token_totals"] = token_counts.copy()
        #  response_data["timing"] = {
            #  "response_time": response_times,
            #  "total_elapsed": total_elapsed,
            #  "response_times": response_times.copy(),
        #  }
        #  response_data["response_file"] = str(response_file.name)  # Add filename for report
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
        respdict: dict,
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
        usage = respdict.get("usage_metadata", {})
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
        resplist = []
        for respfile in task_dir.glob("*-response.json"):
            try:
                with open(respfile, "r") as f:
                    data = json.load(f)
                    resplist.append(data)
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error reading or parsing {respfile}: {e}")
                self.log_error(f"Error reading or parsing {respfile}: {e}")
        return resplist

    def _create_response_table(self, resplist):
        """Creates a rich.table.Table for the response report."""
        table = Table(title="Response Report")
        table.add_column("Response File", style="cyan", no_wrap=True)
        table.add_column("Prompt Tokens", justify="right")
        table.add_column("Candidate Tokens", justify="right")
        table.add_column("Total Tokens", justify="right")
        table.add_column("Cached Tokens", justify="right")
        table.add_column("Response Time (s)", justify="right")
        table.add_column("Total Elapsed (s)", justify="right")

        total_tokens = {"prompt": 0, "candidates": 0, "total": 0, "cached": 0}
        total_response_time = 0

        sorted_resplist = sorted(resplist, key=lambda x: x.get("response_file", ""))

        for data in sorted_resplist:
            table.add_row(
                data.get("response_file", "N/A"),
                str(data["token_totals"].get("prompt", 0)),
                str(data["token_totals"].get("candidates", 0)),
                str(data["token_totals"].get("total", 0)),
                str(data["token_totals"].get("cached", 0)),
                f"{data['timing']['response_time']:.4f}",
                f"{data['timing']['total_elapsed']:.4f}",
            )

            for key in total_tokens:
                total_tokens[key] += data["token_totals"].get(key, 0)
            total_response_time += data["timing"]["response_time"]

        # Add a summary row
        table.add_row(
            "Total",
            str(total_tokens["prompt"]),
            str(total_tokens["candidates"]),
            str(total_tokens["total"]),
            str(total_tokens["cached"]),
            f"{total_response_time:.4f}",
            "",
            style="bold",
        )
        return table

    def _create_test_table(self, grouped_test_results):
        """Creates a rich.table.Table for the test report."""
        tables = {}
        for file_index, test_results in grouped_test_results.items():
            table = Table(title=f"Code File: {file_index}")
            table.add_column("Example", style="cyan")
            table.add_column("Status")
            table.add_column("size")
            table.add_column("palette")
            table.add_column("color count")
            table.add_column("diff pixels")

            for result in test_results:
                if "example" in result:
                    table.add_row(
                        result["example"],
                        result["status"],
                        str(result.get("size_correct", "N/A")),
                        str(result.get("color_palette_correct", "N/A")),
                        str(result.get("correct_pixel_counts", "N/A")),
                        str(result.get("pixels_off", "N/A")),
                    )
                elif "captured_output" in result:
                    table.add_row("Captured Output", result["captured_output"])
                elif "code_execution_error" in result:
                    table.add_row("Code Execution Error", result["code_execution_error"])
            tables[file_index] = table
        return tables

    def create_summary_report(self, resplist, task_dir):
        """Creates a summary report (Markdown and JSON) using rich.table.Table."""

        # --- Response Report ---
        response_table = self._create_response_table(resplist)

        # --- Test Report ---
        grouped_test_results = {}
        for py_file in sorted(task_dir.glob("*-py_*.json")):
            try:
                with open(py_file, "r") as f:
                    test_results = json.load(f)
                    file_index = py_file.stem.split("-")[0]
                    grouped_test_results[file_index] = test_results
            except Exception as e:
                print(f"Failed to load test results from {py_file}: {e}")
                self.log_error(f"Failed to load test results from {py_file}: {e}")

        sorted_grouped_test_results = dict(sorted(grouped_test_results.items()))
        test_tables = self._create_test_table(sorted_grouped_test_results)

        # --- Combine Reports and Save ---
        console = Console(record=True)  # Use record=True to capture output
        console.print(response_table)
        for table in test_tables.values():
            console.print(table)

        report_md = console.export_text()  # Export captured output as plain text
        report_md_file = "summary_report.md"
        self._write_to_file(report_md_file, report_md)

        # --- JSON Report (Keep as before, but use sorted data) ---
        response_report_json = []
        for data in sorted(resplist, key=lambda x: x.get("response_file", "")):
            response_report_json.append({
                "response_file": data.get("response_file", "N/A"),
                "token_usage": data["token_totals"],
                "timing": data["timing"],
            })

        test_report_json = {}
        for file_index, test_results in sorted_grouped_test_results.items():
            test_report_json[file_index] = []
            for result in test_results:
                if "example" in result:
                    test_report_json[file_index].append(
                        {
                            "example": result["example"],
                            "input": result["input"],
                            "expected_output": result["expected_output"],
                            "transformed_output": result.get("transformed_output", ""),
                            "status": result["status"],
                            "size_correct": result.get("size_correct", "N/A"),
                            "color_palette_correct": result.get(
                                "color_palette_correct", "N/A"
                            ),
                            "correct_pixel_counts": result.get(
                                "correct_pixel_counts", "N/A"
                            ),
                            "pixels_off": result.get("pixels_off", "N/A"),
                        }
                    )
                elif "captured_output" in result:
                    test_report_json[file_index].append(
                        {"captured_output": result["captured_output"]}
                    )
                elif "code_execution_error" in result:
                    test_report_json[file_index].append(
                        {"code_execution_error": result["code_execution_error"]}
                    )

        report_json = {
            "response_report": response_report_json,
            "test_report": test_report_json,
        }
        report_json_file = "summary_report.json"
        self._write_to_file(report_json_file, json.dumps(report_json, indent=2))

        # Display report
        self.display_response(
            [report_md], 0, "Task Summary", {}
        )  # prompt_count=0

    def _write_to_file(self, file_name, content):
        """Writes content to a file in the task directory."""
        file_path = self.task_dir / file_name  # Use self.task_dir
        try:
            with open(file_path, "w") as f:
                f.write(content)
        except (IOError, PermissionError) as e:
            print(f"Error writing to file {file_name}: {e}")
            self.log_error(f"Error writing to file {file_name}: {e}")

    # Removed: _create_session_response_table
    # Removed: _create_session_test_table
    # Removed: create_session_summary_report
    # Removed: _write_to_file_session

