"""
The Oracle class acts as a verifier and code tester.

It analyzes generated code, executes tests, provides feedback,
and suggests improvements to guide the Coder.
"""
import ast
import io
import contextlib
import numpy as np
from geometor.seer.tasks import Grid
import json

class Oracle:
    def __init__(self, config, system_context):
        self.config = config
        self.system_context = system_context

    def test_code(self, code, code_file_path, task):
        """Executes and validates the generated code, writing results to a file."""
        test_results_str = ""
        test_results_json = []  # Store results for JSON output
        try:
            tree = ast.parse(code)
            namespace = {}
            # Capture stdout
            output_capture = io.StringIO()
            with contextlib.redirect_stdout(output_capture):
                exec(
                    compile(tree, filename=str(code_file_path), mode="exec"), namespace
                )

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name == "transform":
                    test_results_str += "\n# validation:*\n"
                    for i, pair in enumerate(task.train):
                        input_grid = pair.input.grid
                        expected_output = pair.output.grid

                        test_results_str += f"\n## example {i + 1}\n"
                        example_result = {
                            "example": i + 1,
                            "input": pair.input.to_string(),
                            "expected_output": pair.output.to_string(),
                        }
                        try:
                            transformed_output = namespace["transform"](input_grid)
                            test_results_str += (
                                f"*input:*\n```\n{pair.input.to_string()}\n```\n"
                            )
                            test_results_str += f"*expected output:*\n```\n{pair.output.to_string()}\n```\n"
                            test_results_str += f"*transformed output:*\n```\n{Grid(transformed_output, '', '', '', '').to_string()}\n```\n"

                            # Generate and save image of transformed output
                            transformed_grid = Grid(
                                transformed_output,
                                task.id,
                                "train",
                                i,
                                "transformed",
                            )
                            transformed_image = transformed_grid.to_image()
                            image_filename = (
                                f"{code_file_path.stem}-example_{i + 1}-transformed.png"
                            )
                            image_path = code_file_path.parent / image_filename # Use code_file_path's directory
                            transformed_image.save(image_path)
                            #  test_results_str += f"  Transformed Output Image: ![Transformed Output]({image_filename})\n"

                            example_result["transformed_output"] = Grid(transformed_output, '', '', '', '').to_string()

                            if not np.array_equal(transformed_output, expected_output):
                                test_results_str += f"**FAILED!**\n"
                                example_result["status"] = "FAILED"
                            else:
                                test_results_str += f"  PASSED\n"
                                example_result["status"] = "PASSED"
                        except Exception as e:
                            test_results_str += (
                                f"  Error during validation for example {i + 1}: {e}\n"
                            )
                            example_result["status"] = f"ERROR: {e}"
                            # Removed session.log_error call, as Oracle doesn't have session

                        test_results_json.append(example_result)

            captured_output = output_capture.getvalue()
            if captured_output:
                test_results_str += f"*captured output:*\n```\n{captured_output}\n```\n"
                test_results_json.append({"captured_output": captured_output})


        except SyntaxError as e:
            test_results_str += f"\n*code_execution_error:*\n```\n{e}\n```\n"
            test_results_json.append({"code_execution_error": str(e)})
            # Removed session.log_error call

        except Exception as e:
            test_results_str += f"\n*code_execution_error:*\n```\n{e}\n```\n"
            test_results_json.append({"code_execution_error": str(e)})
            # Removed session.log_error call

        # Save test results as JSON
        test_results_json_file = Path(f"{code_file_path.stem}.json")
        with open(code_file_path.parent / test_results_json_file, "w") as f:
            json.dump(test_results_json, f, indent=2)


        return [test_results_str]  # return the string

    def analyze_results(self, test_results_str):
        """Analyzes the test results and provides feedback."""
        # Placeholder for analysis logic.  This is where the core of the
        # Oracle's "intelligence" will reside.  For now, it's very basic.
        if "FAILED" in test_results_str:
            return "The code failed some tests.  Review the errors and try again."
        else:
            return "The code passed all tests."

    def generate_next_prompt(self, test_results_str, previous_prompt):
        """Generates the next prompt for the coder based on test results."""
        # Placeholder for prompt generation.  This will also become more
        # sophisticated.
        analysis = self.analyze_results(test_results_str)
        return f"{analysis}\n\nPrevious prompt:\n{previous_prompt}\n\nFix the errors."
