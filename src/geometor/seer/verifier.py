import ast
import io
import contextlib
import numpy as np
from geometor.seer.tasks import Grid
import json
from pathlib import Path


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


def test_code(code, task_dir, task_pairs):
    """Executes and validates the generated code, returning results as a list of dicts."""
    test_results_json = []  # Store results for JSON output

    try:
        transform_function = get_transform_function(code)
        if transform_function is None:
            test_results_json.append(
                {"code_execution_error": "transform function not found"}
            )
            return test_results_json

    except SyntaxError as e:
        # Catch SyntaxError from get_transform_function
        # TODO: log error
        return test_results_json

    except Exception as e:
        # TODO: log error
        return test_results_json

    # Capture stdout - still needed for print statements in code
    output_capture = io.StringIO()
    with contextlib.redirect_stdout(output_capture):
        for i, pair in enumerate(task_pairs):
            input_grid = pair.input.grid
            expected_output = pair.output.grid

            example_result = {
                "example": i + 1,
                "input": pair.input.to_string(),
                "expected_output": pair.output.to_string(),
            }
            try:
                transformed_output = transform_function(input_grid)
            except Exception as e:
                example_result["match"] = f"ERROR: {e}"
                example_result["function_output"] = output_capture.getvalue()
                test_results_json.append(example_result)
                continue

            # ADD THESE LINES: Check for None return value
            if transformed_output is None:
                example_result["match"] = "ERROR: transform function returned None"
                test_results_json.append(example_result)
                continue  # Skip to the next iteration

            example_result["transformed_output"] = Grid(
                transformed_output, "", "", "", ""
            ).to_string()

            # --- Calculate Statistics ---
            size_correct = transformed_output.shape == expected_output.shape
            example_result["size_correct"] = size_correct

            transformed_colors = set(np.unique(transformed_output))
            expected_colors = set(np.unique(expected_output))
            color_palette_correct = transformed_colors.issubset(expected_colors)
            example_result["color_palette_correct"] = color_palette_correct

            transformed_counts = dict(
                zip(*np.unique(transformed_output, return_counts=True))
            )
            expected_counts = dict(zip(*np.unique(expected_output, return_counts=True)))
            correct_pixel_counts = transformed_counts == expected_counts
            example_result["correct_pixel_counts"] = correct_pixel_counts

            pixels_off = int(np.sum(transformed_output != expected_output))
            example_result["pixels_off"] = pixels_off
            example_result["percent_correct"] = 100 * (
                ( expected_output.size - pixels_off ) / expected_output.size
            )

            if not np.array_equal(transformed_output, expected_output):
                example_result["match"] = False
            else:
                example_result["match"] = True

            test_results_json.append(example_result)

    return test_results_json


def write_test_results(test_results_json, task_dir, base_filename):
    """Formats test results as Markdown and writes to file, including saving images."""
    test_results_str = ""

    for result in test_results_json:
        if "example" in result:  # It's an example result
            test_results_str += f"\n## example {result['example']}\n"
            test_results_str += f"*input:*\n```\n{result['input']}\n```\n"
            test_results_str += (
                f"*expected output:*\n```\n{result['expected_output']}\n```\n"
            )

            if "transformed_output" in result:
                test_results_str += (
                    f"*transformed output:*\n```\n{result['transformed_output']}\n```\n"
                )

                # Generate and save image of transformed output
                try:
                    # Use the shape of the ACTUAL transformed output
                    grid = []
                    for row in result["transformed_output"].split("\n"):
                        grid.append(row.split())

                    transformed_grid = Grid(
                        grid,
                        "",
                        "",
                        "",
                        "",
                    )
                except ValueError as e:
                    test_results_str += f"**ERROR**: Could not create grid from transformed output: {e}\n"
                    continue  # Skip image creation and go to the next result

                transformed_image = transformed_grid.to_image()
                image_filename = f"{base_filename}-example_{result['example']}.png"
                image_path = task_dir / image_filename
                transformed_image.save(image_path)

            test_results_str += f"size: {result.get('size_correct')}\n"
            test_results_str += f"palette: {result.get('color_palette_correct')}\n"
            test_results_str += f"color count: {result.get('correct_pixel_counts')}\n"
            test_results_str += f"pixels off: {result.get('pixels_off')}\n"

            if result["match"] is True:
                test_results_str += "PASSED\n"
            elif result["match"] is False:
                test_results_str += "**FAILED!**\n"
            else:  # Error case
                test_results_str += f"**ERROR**: {result['match']}\n"

        elif "captured_output" in result:
            test_results_str += (
                f"*captured output:*\n```\n{result['captured_output']}\n```\n"
            )
        elif "code_execution_error" in result:
            test_results_str += f"\n*code_execution_error:*\n```\n{result['code_execution_error']}\n```\n"

    # Write Markdown results
    test_results_md_file = task_dir / f"{base_filename}.md"
    with open(test_results_md_file, "w") as f:
        f.write(test_results_str)

    # Write JSON results
    test_results_json_file = task_dir / f"{base_filename}.json"
    with open(test_results_json_file, "w") as f:
        json.dump(test_results_json, f, indent=2)

    return test_results_str


#  def analyze_results(test_results_str):
#  """Analyzes the test results and provides feedback."""
#  # Placeholder for analysis logic.  This is where the core of the
#  # Oracle's "intelligence" will reside.  For now, it's very basic.
#  if "FAILED" in test_results_str:
#  return "The code failed some tests.  Review the errors and try again."
#  else:
#  return "The code passed all tests."

#  def generate_next_prompt(test_results_str, previous_prompt):
#  """Generates the next prompt for the coder based on test results."""
#  # Placeholder for prompt generation.  This will also become more
#  # sophisticated.
#  analysis = analyze_results(test_results_str)
#  return f"{analysis}\n\nPrevious prompt:\n{previous_prompt}\n\nFix the errors."

#  def test_test_input(
#  transform_function, test_input_grid, task_id, task_dir, base_filename
#  ):
#  """Tests the transform function on the test input and saves the result."""
#  try:
#  transformed_test_output = transform_function(test_input_grid)
#  transformed_test_grid = Grid(
#  transformed_test_output, task_id, "test", 0, "transformed"
#  )
#  transformed_test_image = transformed_test_grid.to_image()
#  test_image_filename = f"{base_filename}-test_output.png"
#  test_image_path = task_dir / test_image_filename
#  transformed_test_image.save(test_image_path)
#  return test_image_filename
#  except Exception as e:
#  return f"Error running transform on test input: {e}"
