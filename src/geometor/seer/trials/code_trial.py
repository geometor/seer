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

        # --- MODIFICATION START ---

        # Initialize test_results to None
        self.test_results = None

        # Run train trials first
        self.train_results = self.test_code_with_timeout(code, task.train)

        # Check if training passed *after* running train trials
        # Use the train_passed property which checks for errors and matching
        if self.train_passed is True:
            # Only run test trials if all train trials passed successfully
            self.test_results = self.test_code_with_timeout(code, task.test)
        # else: self.test_results remains None

        # --- MODIFICATION END ---


        # Calculate total and average scores, handling potential None scores
        train_scores = [
            trial.score
            for trial in self.train_results.get("trials", [])
            if trial.score is not None
        ]

        # --- Simplified test_scores extraction ---
        test_scores = []
        if self.test_results: # Check if test_results is not None (i.e., tests were run)
            test_scores = [
                trial.score
                for trial in self.test_results.get("trials", []) # Safely get trials or empty list
                if trial.score is not None
            ]
        # --- End Simplified test_scores extraction ---


        # Initialize to None
        self.total_score = None
        self.average_score = None

        # Only calculate scores if there were no execution errors in the train set
        # (Test set errors are implicitly handled because test_results would be None if train failed)
        train_error = self.train_results.get("error")
        # test_error = self.test_results.get("error") if self.test_results else None # No longer needed here

        if not train_error: # Only need to check train error now
            all_scores = train_scores + test_scores
            valid_scores = [s for s in all_scores if s is not None]
            if valid_scores:
                self.total_score = sum(valid_scores)
                self.average_score = self.total_score / len(valid_scores)
            else:
                 # Handle case where all trials resulted in None scores (e.g., all test pairs had no output)
                 # We can set total_score to 0 or keep it None depending on desired behavior.
                 # Let's keep it None to indicate no comparable results.
                 self.total_score = None
                 self.average_score = None


        # --- Conditional Image Generation ---
        # The logic here remains mostly the same, show_test will be False if test_results is None
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
        # The existing serialization logic correctly handles self.test_results being None
        results_json = {
            "train": {
                "trials": [t.to_dict() for t in self.train_results.get("trials", [])] if self.train_results else None,
                "error": self.train_results.get("error") if self.train_results else None,
            } if self.train_results else None,
            "test": {
                "trials": [t.to_dict() for t in self.test_results.get("trials", [])] if self.test_results else None,
                "error": self.test_results.get("error") if self.test_results else None,
            } if self.test_results else None, # This correctly outputs null for "test" if it's None
            "total_score": self.total_score,
            "average_score": self.average_score,
        }

        self.task_step._write_to_json(json_file, results_json)


    def to_dict(self) -> dict:
        """Converts the CodeTrial results to a dictionary."""
        # This structure should match the JSON saved and what analyze_trial_data expects
        return {
            "code_filename": self.code_filename, # Include filename for reference
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
            # Add train_passed/test_passed status for completeness?
            # analyze_trial_data recalculates these, so maybe not strictly needed here,
            # but could be useful for debugging the dictionary representation.
            # "train_passed": self.train_passed,
            # "test_passed": self.test_passed,
        }

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
        if not self.train_results or self.train_results.get("error"):
            return None  # Error in overall execution or no results
        trials = self.train_results.get("trials", [])
        if not trials: # Handle case with no trials (shouldn't happen for train)
             return None
        if any(trial.error for trial in trials):
            return None  # Error in any individual trial
        # All trials must have an expected output and match it
        if all(trial.task_pair.output is not None and trial.match for trial in trials):
            return True
        return False # Some didn't match, or had no expected output, or had errors handled above

    @property
    def test_passed(self) -> bool | None:
        """
        Checks if the test trials passed.

        Returns:
            bool | None: True if test trials were run AND all relevant ones passed.
                         False if test trials were run AND some relevant ones failed.
                         None if test trials were NOT run (because train failed)
                         OR if an error occurred during test execution.
        """
        # If test_results is None, tests were not run or failed catastrophically before pair evaluation
        if not self.test_results:
            return None
        # If there was an overall error during test execution
        if self.test_results.get("error"):
            return None
        trials = self.test_results.get("trials", [])
        if not trials:
             # No test trials executed (e.g., test set was empty, but train passed)
             # Return True as no required tests failed? Or None? Let's stick with None for ambiguity.
             return None
        if any(trial.error for trial in trials):
            return None # Error in any individual trial

        # Check if *all* test pairs that *have* an expected output match.
        # Pairs without expected output are ignored for the 'passed' status.
        relevant_trials = [t for t in trials if t.task_pair.output is not None]
        if not relevant_trials:
            # If there are no test pairs with expected output, what does "passed" mean?
            # Let's return True, as no required comparisons failed.
            # Alternatively, return None if this state is ambiguous. Let's stick with True for now.
            return True
        if all(trial.match for trial in relevant_trials):
            return True
        return False # At least one relevant trial did not match

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
                # Expected output grid might be None
                expected_output_grid = pair.output.grid if pair.output else None

                try:
                    # Make a copy to prevent modification by the transform function
                    input_grid_copy = np.copy(input_grid)
                    transformed_output = transform_function(input_grid_copy)
                    error_message = None # Initialize error message

                    # --- Validation and Repair Logic ---
                    if transformed_output is None:
                        # Handle None output directly
                        pass # TaskPairTrial handles None transformed_output
                    else:
                        # Attempt to convert/normalize to a NumPy array of integers
                        try:
                            # Apply list wrapping if necessary (only if not already ndarray)
                            if not isinstance(transformed_output, np.ndarray):
                                if not isinstance(transformed_output, list):
                                    transformed_output = [[transformed_output]] # Wrap single value
                                elif not transformed_output: # Handle empty list
                                     transformed_output = np.empty((0,0), dtype=int) # Represent as empty array
                                elif not isinstance(transformed_output[0], list):
                                     # Check if it's a list of numbers (potential flat list)
                                     if all(isinstance(x, (int, float, np.number)) for x in transformed_output):
                                         transformed_output = [transformed_output] # Wrap flat list as single row
                                     # else: leave as is, np.array below might handle or fail

                            # Convert to NumPy array, explicitly requesting int dtype
                            # This might raise ValueError/TypeError if conversion is impossible
                            transformed_output = np.array(transformed_output, dtype=int)

                            # --- ADDED CHECK: Verify dtype and dimensionality ---
                            if not np.issubdtype(transformed_output.dtype, np.integer):
                                error_message = f"Validation Error: Transformed output could not be fully converted to integer type (dtype is {transformed_output.dtype})."
                                # Set output to None to prevent passing bad data, error handled below
                                transformed_output = None
                            elif transformed_output.ndim != 2:
                                 error_message = f"Validation Error: Transformed output must be a 2D grid (shape is {transformed_output.shape})."
                                 transformed_output = None # Set output to None

                        except (ValueError, TypeError) as conversion_error:
                            # Catch errors during np.array() conversion
                            error_message = f"Validation Error: Failed to convert transformed output to integer grid. Detail: {conversion_error}"
                            transformed_output = None # Set output to None

                    # Create TaskPairTrial
                    if error_message:
                        # If validation failed, create trial with error
                        trial = TaskPairTrial(
                            pair, error=error_message, function_output=output_capture.getvalue()
                        )
                    else:
                        # If validation passed (or output was None initially), create trial normally
                        trial = TaskPairTrial(
                            pair, transformed_output=transformed_output # Pass the validated ndarray or None
                        )


                except Exception as e:
                    # Catch errors from transform_function execution itself
                    trial = TaskPairTrial(
                        pair, error=f"Execution Error: {e}", function_output=output_capture.getvalue()
                    )

                trials.append(trial)

        results["trials"] = trials  # Store TaskPairTrial objects directly
                        if not isinstance(transformed_output, list):
                            # Case: Single element (not a list)
                            transformed_output = [[transformed_output]]
                        elif not isinstance(transformed_output[0], list):
                            # Case: Single row (list, but not list of lists)
        return results
