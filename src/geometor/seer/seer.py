"""
The Seer class orchestrates the process of solving tasks.

It interacts with the Gemini model, manages the session, handles logging,
and controls the flow of execution for analyzing examples and generating solutions.
"""
from rich import print
from datetime import datetime
from pathlib import Path
import json
import numpy as np
import os
import re
import ast
import contextlib
import io

from geometor.seer.tasks import Tasks, Task, Grid
from geometor.seer.oracle import Oracle

from geometor.seer.gemini_client import GeminiClient as Client
from geometor.seer.exceptions import (
    MultipleFunctionCallsError,
    MaxRetriesExceededError,
    UnknownFunctionError,
    FunctionArgumentError,
    FunctionExecutionError,
)
from geometor.seer.session import Session


class Seer:
    """
    Initialize the Seer with all necessary components for solving and logging.

    Seer expects tasks with input/output pairs of training examples.
    """

    def __init__(
        self,
        config: dict,
        max_iterations: int = 5,
    ):
        self.config = config
        self.start_time = datetime.now()
        self.response_times = []

        #  self.nlp_model = config["nlp_model"]
        #  self.code_model = config["code_model"]
        self.dreamer_config = config["dreamer"]
        self.coder_config = config["coder"]
        self.oracle_config = config["oracle"] # New

        with open(self.dreamer_config["system_context_file"], "r") as f:
            self.dreamer_system_context = f.read().strip()
        with open(self.coder_config["system_context_file"], "r") as f:
            self.coder_system_context = f.read().strip()
        with open(config["task_context_file"], "r") as f:
            self.task_context = f.read().strip()

        with open(self.oracle_config["system_context_file"], "r") as f: # New
            self.oracle_system_context = f.read().strip() # New

        with open(config["investigate_nlp"], "r") as f:
            self.nlp_instructions = f.read().strip()
        with open(config["investigate_code"], "r") as f:
            self.code_instructions = f.read().strip()

        self.max_iterations = config["max_iterations"]
        self.current_iteration = 0

        self.dreamer_client = Client(
            self.dreamer_config, f"{self.dreamer_system_context}\n\n{self.task_context}"
        )
        self.coder_client = Client(
            self.coder_config, f"{self.coder_system_context}\n\n{self.task_context}"
        )
        self.oracle_client = Oracle(  # New
            self.oracle_config, self.oracle_system_context
        )  # New

        self.token_counts = {"prompt": 0, "candidates": 0, "total": 0, "cached": 0}
        self.extracted_file_counts = {"py": 0, "yaml": 0, "json": 0, "txt": 0}

    def solve(
        self,
        task,
    ):
        """
        Main method to orchestrate the task solving workflow.
        """
        self.prompt_count = 0
        self.task = task  # Store the task for use in _process_response and _test_code
        history = [""]

        # Reset extracted file counts for each task
        self.extracted_file_counts = {"py": 0, "yaml": 0, "json": 0, "txt": 0}

        self._investigate_examples(task.train)
        #  self._review_programs()
        #  self._run_solution_loop()

        # Gather response data and create summary report
        respdata = self.session.gather_response_data(self.session.task_dir)
        self.session.create_summary_report(respdata, self.session.task_dir)


    def _investigate_examples(self, examples, include_images=True):
        """
        investigate all training pairs
        """
        history = [""]

        for i, pair in enumerate(examples, 1):
            input_grid_str = pair.input.to_string()
            output_grid_str = pair.output.to_string()

            # dreamer prompt
            prompt = [
                "\n**input**\n```\n",
                input_grid_str,
                "\n```\n\n",
            ]
            if include_images:
                prompt.append(pair.input.to_image())
                prompt.append("\n")
            prompt.append("\n**output**\n```\n")
            prompt.append(output_grid_str)
            prompt.append("\n```\n\n")
            if include_images:
                prompt.append(pair.output.to_image())
                prompt.append("\n")

            instructions = [self.nlp_instructions]
            response = self._generate(
                self.dreamer_client,  # Use dreamer_client
                history,
                prompt,
                instructions,
                #  tools=None,
                description=f"example_{i} - NLP",
            )
            history.extend(prompt)
            history.extend(response)

            # coder prompt
            instructions = [
                self.code_instructions.format(
                    input_grid_rows=pair.input.to_python_string(),
                    expected_output_grid_rows=pair.output.to_python_string(),
                )
            ]
            prompt = [""]
            response = self._generate(  # Use coder_client
                self.coder_client,
                history,
                prompt,
                instructions,
                #  tools="code_execution",
                description=f"example_{i} - CODE",
            )
            history.extend(prompt)
            history.extend(response)

    def _review_programs(self, instructions):
        """
        summarize observations on pairs
        """

        prompt = [""]
        instructions = [""]
        self._generate(
            prompt,
            instructions,
            #  tools="code_execution",
            description=f"example_summary",
        )

    def _generate(
        self,
        client,
        history,
        prompt,
        instructions,
        tools=None,
        functions=None,
        description="",
    ):
        """
        Generate content from the model with standardized logging and function call handling.
        """
        self.prompt_count += 1

        total_prompt = history + prompt + instructions

        self.session.log_prompt(
            prompt,
            instructions,
            self.prompt_count,
            description=description,
        )
        self.session.log_total_prompt(
            total_prompt,
            self.prompt_count,
            description=description,
        )

        #  history = history + prompt

        #  response = self.nlp_client.generate_content(
        response = client.generate_content(
            total_prompt,
            tools=tools,
        )

        response_parts, function_call_found, last_result = self._process_response(
            response, functions, total_prompt
        )

        self.session.log_response(
            response,
            response_parts,
            self.prompt_count,
            self.token_counts,
            self.response_times,
            self.start_time,
        )

        #  history = history + response_parts

        return response_parts

    def _process_response(self, response, functions, total_prompt):
        """Processes the response from the Gemini model."""
        response_parts = []
        function_call_found = False
        last_result = None

        if hasattr(response.candidates[0].content, "parts"):
            for part in response.candidates[0].content.parts:
                if part.text:
                    response_parts.append("\n*text:*\n")
                    response_parts.append(part.text + "\n")
                    # Check for triple backticks and write to file
                    self._write_extracted_content(part.text)

                if part.executable_code:
                    response_parts.append("\n*code_execution:*\n")
                    code = part.executable_code.code
                    response_parts.append(f"```python\n{code}\n```\n")
                    code_file_path = (
                        self.session.task_dir / f"{self.prompt_count:03d}-code.py"
                    )
                    self._write_to_file(code_file_path, code)

                    # Call _test_code and extend response_parts
                    test_results = self.oracle_client.test_code(code, code_file_path, self.task)
                    response_parts.extend(test_results)

                if part.code_execution_result:
                    response_parts.append("\n*code_execution_result:*\n")
                    outcome = part.code_execution_result.outcome
                    output = part.code_execution_result.output
                    response_parts.append(f"outcome: {outcome}\n")
                    response_parts.append(f"```\n{output}\n```\n")
                    self._write_to_file(
                        f"{self.prompt_count:03d}-code_result.txt", output
                    )

                if part.function_call:
                    function_call_found = True
                    response_parts.append("\n*function_call:*\n")
                    response_parts.append(part.function_call.name + "\n")

                    result, msg = self._call_function(
                        part.function_call, functions, total_prompt
                    )
                    last_result = msg

                    response_parts.append("\nresult:\n")
                    response_parts.append(f"{result}\n")
                    response_parts.append(f"{msg}\n")

        return response_parts, function_call_found, last_result

    def _write_extracted_content(self, text):
        """Extracts content enclosed in triple backticks and writes it to files."""
        matches = re.findall(r"```(\w+)?\n(.*?)\n```", text, re.DOTALL)
        for file_type, content in matches:
            file_type = file_type.lower() if file_type else "txt"
            if file_type == "python":
                file_type = "py"  # Correct extension
            if file_type not in self.extracted_file_counts:
                file_type = "txt"

            self.extracted_file_counts[file_type] += 1
            count = self.extracted_file_counts[file_type]
            file_name = f"{self.prompt_count:03d}-{file_type}_{count:02d}.{file_type}"
            file_path = self.session.task_dir / file_name

            self._write_to_file(file_name, content)

            # If it's a Python file, also run tests
            if file_type == "py":
                test_results = self.oracle_client.test_code(content, file_path, self.task) # Pass task
                # Write test results to file
                test_results_file = Path(f"{file_path.stem}.md")
                self._write_to_file(test_results_file, "".join(test_results))


    def _write_to_file(self, file_name, content):
        """Writes content to a file in the task directory."""
        file_path = self.session.task_dir / file_name  # Always use task_dir
        try:
            with open(file_path, "w") as f:
                f.write(content)
        except (IOError, PermissionError) as e:
            print(f"Error writing to file {file_name}: {e}")
            self.session.log_error(f"Error writing to file {file_name}: {e}")

    def _call_function(self, function_call, functions, total_prompt):
        """Execute a function call with improved error handling."""
        if not functions:
            raise ValueError("No functions provided")

        function_name = function_call.name
        function_args = function_call.args

        if function_name not in functions:
            raise UnknownFunctionError(f"Unknown function: {function_name}")

        try:
            result = functions[function_name](**function_args)
            return result
        except TypeError as e:
            raise FunctionArgumentError(
                f"Invalid arguments for {function_name}: {str(e)}"
            )
        except Exception as e:
            raise FunctionExecutionError(f"Error executing {function_name}: {str(e)}")

        # If we get here, we've exhausted retries without success
        error_msg = "Failed to get valid function call after maximum retries"
        print(f"\nERROR: {error_msg}")
        self.session.log_error(error_msg, "".join(total_prompt))

    def run(self, tasks):
        """
        Runs the Seer over the set of tasks.
        """
        self.tasks = tasks  # Set tasks here
        self.prompt_count = 0
        self.session = Session(self.config, self.tasks)

        for task in self.tasks:
            self.session.task_dir = self.session.session_dir / task.id  # Set task_dir
            self.session.task_dir.mkdir(parents=True, exist_ok=True)

            self.solve(task)

        # Create session summary report
        self.create_session_summary_report()

    def create_session_summary_report(self):
        """
        Creates a session-level summary report by aggregating task summary reports.
        """
        session_response_report_json = []
        session_test_report_json = {}

        # Iterate through each task directory
        for task_dir in self.session.session_dir.iterdir():
            if task_dir.is_dir():  # Ensure it's a directory
                summary_report_json_path = task_dir / "summary_report.json"
                if summary_report_json_path.exists():
                    try:
                        with open(summary_report_json_path, "r") as f:
                            task_summary = json.load(f)
                            # Aggregate response reports
                            session_response_report_json.extend(
                                task_summary.get("response_report", [])
                            )
                            # Aggregate test reports, keyed by task ID
                            task_id = task_dir.name
                            session_test_report_json[task_id] = task_summary.get(
                                "test_report", {}
                            )
                    except (IOError, json.JSONDecodeError) as e:
                        print(f"Error reading or parsing {summary_report_json_path}: {e}")
                        self.session.log_error(
                            f"Error reading or parsing {summary_report_json_path}: {e}"
                        )

        # Combine into a session-level report
        session_summary_report = {
            "response_report": session_response_report_json,
            "test_report": session_test_report_json,
        }

        # Write the session summary report to the session directory
        # Corrected: Use self.session.session_dir, not self.session.task_dir
        session_summary_report_json_file = "session_summary_report.json"
        self._write_to_file_session(  # Use the session-level writing method
            session_summary_report_json_file,
            json.dumps(session_summary_report, indent=2),
        )

        # --- Create Markdown Report ---
        session_summary_report_md = "# Session Summary Report\n\n"

        # Response Report
        session_summary_report_md += "## Response Summary\n\n"
        session_summary_report_md += "| Task ID | Response File | Prompt Tokens | Candidate Tokens | Total Tokens | Cached Tokens | Response Time (s) | Total Elapsed (s) |\n"
        session_summary_report_md += "|-------|---------------|---------------|------------------|--------------|---------------|-------------------|-------------------|\n"

        total_tokens = {"prompt": 0, "candidates": 0, "total": 0, "cached": 0}
        total_response_time = 0

        for response in session_response_report_json:
            task_id = response.get("response_file", "N/A").split("-")[
                0
            ]  # Extract task ID
            session_summary_report_md += f"| {task_id} | {response.get('response_file', 'N/A')} | {response['token_usage'].get('prompt', 0)} | {response['token_usage'].get('candidates', 0)} | {response['token_usage'].get('total', 0)} | {response['token_usage'].get('cached', 0)} | {response['timing']['response_time']:.4f} | {response['timing']['total_elapsed']:.4f} |\n"

            for key in total_tokens:
                total_tokens[key] += response["token_usage"].get(key, 0)
            total_response_time += response["timing"]["response_time"]

        session_summary_report_md += f"| **Total** | | **{total_tokens['prompt']}** | **{total_tokens['candidates']}** | **{total_tokens['total']}** | **{total_tokens['cached']}** | **{total_response_time:.4f}** |  |\n\n"

        # Test Report - More complex due to nested structure
        session_summary_report_md += "## Test Summary\n\n"
        for task_id, test_report in session_test_report_json.items():
            session_summary_report_md += f"### Task: {task_id}\n\n"
            for file_index, file_results in test_report.items():
                session_summary_report_md += f"#### Code File: {file_index}\n\n"
                session_summary_report_md += "| Example | Status | size | palette | color count | diff pixels |\n"
                session_summary_report_md += "|---------|--------|------|---------|-------------|-------------|\n"
                for result in file_results:
                    if "example" in result:
                        session_summary_report_md += f"| {result['example']} | {result['status']} | {result.get('size_correct', 'N/A')} | {result.get('color_palette_correct', 'N/A')} | {result.get('correct_pixel_counts', 'N/A')} | {result.get('pixels_off', 'N/A')} |\n"
                    elif "captured_output" in result:
                        session_summary_report_md += f"| Captured Output |  |  |  |  |\n"
                        session_summary_report_md += f"|---|---|---|---|---|\n"
                        session_summary_report_md += (
                            f"|  | ```{result['captured_output']}``` |  |  |  |\n"
                        )
                    elif "code_execution_error" in result:
                        session_summary_report_md += (
                            f"| Code Execution Error |  |  |  |  |\n"
                        )
                        session_summary_report_md += f"|---|---|---|---|---|\n"
                        session_summary_report_md += (
                            f"|  | ```{result['code_execution_error']}``` |  |  |  |\n"
                        )
                session_summary_report_md += "\n"

        # Write the session summary report (Markdown) to the session directory
        # Corrected: Use self.session.session_dir
        session_summary_report_md_file = "session_summary_report.md"
        self._write_to_file_session(  # Use session-level writing method
            session_summary_report_md_file, session_summary_report_md
        )

        # Display report
        self.session.display_response(
            [session_summary_report_md],
            0,
            "Session Summary",
            {},
        )  # prompt_count=0

    def _write_to_file_session(self, file_name, content):
        """
        Writes content to a file in the session directory.  
        Distinct from _write_to_file, which writes to task directory.
        """
        file_path = self.session.session_dir / file_name  # Use session_dir
        try:
            with open(file_path, "w") as f:
                f.write(content)
        except (IOError, PermissionError) as e:
            print(f"Error writing to file {file_name}: {e}")
            self.session.log_error(f"Error writing to file {file_name}: {e}")
