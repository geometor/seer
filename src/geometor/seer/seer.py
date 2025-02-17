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

        with open("nlp_instructions.md", "r") as f:
            self.nlp_instructions = f.read().strip()
        with open("code_instructions.md", "r") as f:
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
        response_data = self._gather_response_data()
        self._create_summary_report(response_data)

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
        file_path = self.session.task_dir / file_name
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

        #  print(f"Using model: {self.dreamer_client.model_name}")

        # Use session_dir for the initial context display
        #  self.session.display_prompt(
        #      [self.system_context],
        #      [self.task_context],
        #      0,
        #      description="Initial Context",
        #  )
        #  self.session.display_prompt(
        #  [self.dreamer_system_context],
        #  [self.task_context],
        #  0,
        #  description="Initial Dreamer Context",
        #  )
        #  self.session.display_prompt(
        #  [self.coder_system_context],
        #  [self.task_context],
        #  0,
        #  description="Initial Coder Context",
        #  )

        for task in self.tasks:
            self.session.task_dir = self.session.session_dir / task.id  # Set task_dir
            self.session.task_dir.mkdir(parents=True, exist_ok=True)

            self.solve(task)

    def _gather_response_data(self):
        """Gathers data from all response.json files in the task directory."""
        response_data = []
        for response_file in self.session.task_dir.glob("*-response.json"):
            try:
                with open(response_file, "r") as f:
                    data = json.load(f)
                    response_data.append(data)
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error reading or parsing {response_file}: {e}")
                self.session.log_error(f"Error reading or parsing {response_file}: {e}")
        return response_data

    def _create_summary_report(self, response_data):
        """Creates a summary report (Markdown and JSON) of token usage, timing, and test results."""

        # Aggregate data
        total_tokens = {"prompt": 0, "candidates": 0, "total": 0, "cached": 0}
        total_response_time = 0
        all_response_times = []
        test_results = []

        for data in response_
            for key in total_tokens:
                total_tokens[key] += data["token_totals"].get(key, 0)
            total_response_time += data["timing"]["response_time"]
            all_response_times.extend(data["timing"]["response_times"])

            # Collect test results from JSON files
            for py_file in self.session.task_dir.glob("*-py_*.json"):
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
        report_md_file = self.session.task_dir / "summary_report.md"
        report_json_file = self.session.task_dir / "summary_report.json"

        self._write_to_file(report_md_file, report_md)
        with open(report_json_file, "w") as f:
            json.dump(report_json, f, indent=2)

        # Display report
        self.session.display_response(
            [report_md], 0, "Task Summary", {}
        )  # prompt_count=0, as this isn't a regular prompt/response

