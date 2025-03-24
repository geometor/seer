import ast
import contextlib
import io
import numpy as np
import multiprocessing

from geometor.seer.tasks.tasks import Task
from geometor.seer.tasks.grid import Grid

from geometor.seer.trials.task_pair_trial import TaskPairTrial


class CodeTrial:
    """
    Represents a single trial of running a piece of code against a task.

    This class encapsulates the execution of the code, the comparison of the
    output with the expected output, and the calculation of a score.
    """

    def __init__(
        self,
        task_step,
        code_filename: str,
        code,
        task: Task,
    ):
        """
        Initializes a CodeTrial.

        Args:
            task_step: The TaskStep object this trial belongs to.
            code_filename: The name of the file containing the code.
            code: The Python code string.
            task: The Task object this trial is run against.
        """
        self.code_filename = code_filename
        self.code = code
        self.task = task
        self.task_step = task_step  # store

        # Run and store results directly in CodeTrial
        self.train_results = self.test_code_with_timeout(
            code, task.train
        )
        self.test_results = None  # Initialize
        if self.train_passed is True:  # Only run tests if train passed
            self.test_results = self.test_code_with_timeout(code, task.test)

        # Calculate total and average scores
        train_scores = [
            trial.score
            for trial in self.train_results.get("trials", [])
            if trial.score is not None
        ]  # Access score directly
        test_scores = [
            trial.score
            for trial in self.test_results.get("trials", [])
            if trial.score is not None
        ] if self.test_results else []  # Handle None test_results, access score

        # Initialize to None
        self.total_score = None
        self.average_score = None

        if not self.train_results.get("error") and not (self.test_results and self.test_results.get("error")):
            total_score = sum(train_scores) + sum(test_scores)
            num_scores = len(train_scores) + len(test_scores)
            if num_scores > 0:
                self.total_score = total_score
                self.average_score = total_score / num_scores

        # --- Conditional Image Generation ---
        if self.has_valid_transformed_output:
            show_test = bool(self.test_results)
            results_image = self.task.to_image(
                train_results=self.train_results,
                test_results=self.test_results,
                show_test=show_test,
            )
            png_file = self.task_step.dir / f"{self.code_filename}.trial.png"
            results_image.save(png_file)

        json_file = self.code_filename + ".trial.json"
        # Convert TaskPairTrial objects to dicts before serialization
        results_json = {
            "train": {
                "trials": [t.to_dict() for t in self.train_results.get("trials", [])] if self.train_results else None,
                "error": self.train_results.get("error") if self.train_results else None,
            } if self.train_results else None,
            "test": {
                "trials": [t.to_dict() for t in self.test_results.get("trials", [])] if self.test_results else None,
                "error": self.test_results.get("error") if self.test_results else None,
            } if self.test_results else None,
            "total_score": self.total_score,
            "average_score": self.average_score,
        }

        self.task_step._write_to_json(json_file, results_json)

    @property
    def train_passed(self) -> bool | None:
        """
        Checks if the training trials passed.

        Returns:
            bool | None: True if all training trials passed, False if some
            failed (but no errors occurred), and None if any error occurred
            during the trials (either in the overall execution or in
            individual trials).
        """
        if not self.train_results:
            return None
        if self.train_results.get("error"):
            return None  # Error in the overall results
        trials = self.train_results.get("trials", [])
        if any(trial.error for trial in trials):  # Check for error directly
            return None  # Error in any individual trial
        if all(trial.match for trial in trials):  # Check for match directly
            return True  # All trials passed
        return False  # No errors, but not all passed

    @property
    def test_passed(self) -> bool | None:
        """
        Checks if the test trials passed.

        Returns:
            bool | None: True if all test trials passed, False if some
            failed (but no errors occurred), and None if any error occurred
            during the trials (either in the overall execution or in
            individual trials).
        """
        if not self.test_results:
            return None
        if self.test_results.get("error"):
            return None  # Error in overall results
        trials = self.test_results.get("trials", [])
        if any(trial.error for trial in trials):  # Check for error directly
            return None  # Error in any individual trial
        if all(trial.match for trial in trials):   # Check for match directly
            return True  # All trials passed
        return False  # No errors, but not all passed

    @property
    def has_valid_transformed_output(self) -> bool:
        """Checks for at least one valid transformed output in train or test."""

        def has_valid_output(results):
            if not results or results.get("error"):
                return False
            trials = results.get("trials")
            if not trials:
                return False
            return any(trial.transformed_output is not None for trial in trials) # Check for transformed_output

        return has_valid_output(self.train_results) or has_valid_output(
            self.test_results
        )

    def generate_report(self) -> str:
        """Generates a textual report of the trial results."""
        report = f"Results for {self.code_filename}:\n"

        if self.train_results:
            if "error" in self.train_results:
                report += f"Train Set Error: {self.train_results['error']}\n"
            else:
                report += "\nTrain Set Results:\n"
                for i, trial in enumerate(self.train_results.get("trials", [])):
                    report += f"\n## Example {i+1}:\n"
                    report += trial.generate_report()  # Use TaskPairTrial's report

        if self.test_results:
            if "error" in self.test_results:
                report += f"Test Set Error: {self.test_results['error']}\n"
            else:
                report += "\nTest Set Results:\n"
                for i, trial in enumerate(self.test_results.get("trials", [])):
                    report += f"\n## Example {i+1}:\n"
                    report += trial.generate_report()   # Use TaskPairTrial's report

        return report

    @staticmethod
    def get_transform_function(code):
        """Parses the code, finds the 'transform' function, and returns it."""
        try:
            tree = ast.parse(code)
            namespace = {}
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name == "transform":
                    exec(compile(tree, filename="<string>", mode="exec"), namespace)
                    return namespace.get("transform")  # Returns None if not found
            return None  # Explicitly return None if no transform function
        except SyntaxError as e:
            raise  # Re-raise SyntaxError to be handled by caller



    def test_code_with_timeout(self, code, task_pairs, timeout=10) -> dict:
        """
        Executes and validates the generated code with a timeout.

        Args:
            code: The Python code to execute.
            task_pairs: A list of TaskPair objects to test the code against.
            timeout: The maximum execution time in seconds.

        Returns:
            dict: A dictionary containing the results of the code execution.
                If an error occurs, the dictionary will contain an "error" key
                with a description of the error.  Otherwise, it contains a
                "trials" key, with a list of trial results.
        """

        def worker(code, task_pairs, result_queue):
            """Worker function to execute the code."""
            try:
                test_results = self.test_code(code, task_pairs)  # Use self.test_code
                result_queue.put(test_results)
            except Exception as e:
                result_queue.put({"error": str(e)})

        result_queue = multiprocessing.Queue()
        process = multiprocessing.Process(
            target=worker, args=(code, task_pairs, result_queue)
        )
        process.start()

        process.join(timeout)

        if process.is_alive():
            process.terminate()
            process.join()  # Ensure termination
            return {  # Return a dict, not a list
                "error": f"Timeout: Code execution exceeded {timeout} seconds"
            }
        else:
            return result_queue.get()

    def test_code(self, code, task_pairs) -> dict:
        """
        Executes and validates the generated code.

        Args:
            code: The Python code to execute.
            task_pairs: A list of TaskPair objects to test the code against.

        Returns:
            dict: A dictionary containing the results of the code execution.  If
            an error occurs during parsing or execution, the dictionary will
            contain an "error" key with a description of the error.  Otherwise,
            it contains a "trials" key, with a list of per-pair trial results,
            which are now TaskPairTrial objects.
        """
        results = {}
        trials = []  # List to store TaskPairTrial objects

        try:
            transform_function = CodeTrial.get_transform_function(
                code
            )  # Use CodeTrial's method
            if transform_function is None:
                results["error"] = "transform function not found"
                return results

        except SyntaxError as e:
            # TODO: log error
            results["error"] = "syntax error:\n" + str(e)
            return results

        except Exception as e:
            # TODO: log error
            results["error"] = "error:\n" + str(e)
            return results

        # Capture stdout - still needed for print statements in code
        output_capture = io.StringIO()
        with contextlib.redirect_stdout(output_capture):
            for i, pair in enumerate(task_pairs):
                input_grid = pair.input.grid
                expected_output = pair.output.grid

                try:
                    transformed_output = transform_function(input_grid)

                    # --- Validation and Repair Logic ---
                    if not isinstance(transformed_output, np.ndarray):
                        if not isinstance(transformed_output, list):
                            # Case: Single element (not a list)
                            transformed_output = [[transformed_output]]
                        elif not isinstance(transformed_output[0], list):
                            # Case: Single row (list, but not list of lists)
                            transformed_output = [transformed_output]
                    # Ensure it's a NumPy array
                    if transformed_output is not None:
                        transformed_output = np.array(transformed_output)

                    trial = TaskPairTrial(
                        pair, transformed_output=transformed_output
                    )

                except Exception as e:
                    trial = TaskPairTrial(
                        pair, error=str(e), function_output=output_capture.getvalue()
                    )

                trials.append(trial)

        results["trials"] = trials  # Store TaskPairTrial objects directly
        return results
