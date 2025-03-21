import ast
import contextlib
import io
import multiprocessing
from typing import Dict

import numpy as np

from geometor.seer.trials.code_trial import CodeTrial
from geometor.seer.trials.task_pair_trial import TaskPairTrial
from geometor.seer.tasks.grid import Grid


class StepCodeTrials:
    """
    Manages a collection of CodeTrial instances for a TaskStep.
    """

    def __init__(self):
        self.code_trials: Dict[str, CodeTrial] = {}

    def add_code_trial(self, code_filename: str, code_trial: CodeTrial):
        """Adds a CodeTrial instance to the collection."""
        self.code_trials[code_filename] = code_trial

    def get_code_trial(self, code_filename: str) -> CodeTrial | None:
        """Retrieves a CodeTrial by its filename."""
        return self.code_trials.get(code_filename)

    def get_first_code_trial(self) -> CodeTrial | None:
        """Retrieves the first CodeTrial, if any."""
        if self.code_trials:
            return next(iter(self.code_trials.values()))
        return None

    @property
    def any_train_passed(self) -> bool:
        """Checks if any train trials passed."""
        return any(trial.train_passed for trial in self.code_trials.values())

    @property
    def any_test_passed(self) -> bool:
        """Checks if any test trials passed."""
        return any(trial.test_passed for trial in self.code_trials.values())

    @property
    def count_trials(self) -> int:
        """Checks if any test trials passed."""
        return len(self.code_trials)

    def get_all_trials(self):
        """Returns a list of all CodeTrial objects."""
        return list(self.code_trials.values())

    def test_code_with_timeout(self, code, task_pairs, timeout=10):
        """Executes and validates the generated code with a timeout."""

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
            return [
                {
                    "code_execution_error": f"Timeout: Code execution exceeded {timeout} seconds"
                }
            ]

        else:
            return result_queue.get()

    def test_code(self, code, task_pairs):
        """Executes and validates the generated code, returning results as a list of dicts."""
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

        results["trials"] = [
            t.to_dict() for t in trials
        ]  # Convert to dicts for output
        return results

    def execute_trials(self, task_step, task):
        """Executes trials for all available code."""
        for code_filename, code in task_step.codes["py"].items():
            code_trial = self.get_code_trial(code_filename)
            if code_trial is None:
                code_trial = CodeTrial(task_step, code_filename, code, task)
                self.add_code_trial(code_filename, code_trial)

            # Run and store results directly in CodeTrial
            code_trial.train_results = self.test_code_with_timeout(
                code, task.train
            )
            code_trial.test_results = (
                self.test_code_with_timeout(code, task.test)
                if code_trial.train_passed
                else []
            )
            code_trial.execute_and_save_results()
