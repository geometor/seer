import ast
import io
import contextlib
import numpy as np
from geometor.seer.tasks.grid import Grid, string_to_grid
import json
from pathlib import Path
import multiprocessing
import time


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


def test_code_with_timeout(code, task_pairs, timeout=10):
    """Executes and validates the generated code with a timeout."""

    def worker(code, task_pairs, result_queue):
        """Worker function to execute the code."""
        try:
            test_results = test_code(code, task_pairs)
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


def test_code(code, task_pairs):
    """Executes and validates the generated code, returning results as a list of dicts."""
    results = {}

    try:
        transform_function = get_transform_function(code)
        if transform_function is None:
            results["error"] = "transform function not found"
            return results

    except SyntaxError as e:
        # TODO: log error
        results["error"] = "syntax error:\n" + e
        return results

    except Exception as e:
        # TODO: log error
        results["error"] = "error:\n" + e
        return results

    # Capture stdout - still needed for print statements in code
    output_capture = io.StringIO()
    with contextlib.redirect_stdout(output_capture):
        results["trials"] = []
        for i, pair in enumerate(task_pairs):
            input_grid = pair.input.grid
            expected_output = pair.output.grid

            example_result = {
                "id": i + 1,
                "input": pair.input.to_string(),
                "expected_output": pair.output.to_string(),
            }
            try:
                transformed_output = transform_function(input_grid)
            except Exception as e:
                example_result["match"] = False
                example_result["error"] = f"error calling transform:\n{str(e)}"
                example_result["function_output"] = output_capture.getvalue()
                results["trials"].append(example_result)
                continue

            if transformed_output is None:
                example_result["match"] = False
                example_result["error"] = "transform function returned None"
                example_result["function_output"] = output_capture.getvalue()
                results["trials"].append(example_result)
                continue

            try:
                transformed_output = np.array(transformed_output)  
            except Exception as e:
                example_result["match"] = False
                example_result["error"] = (
                    "could not convert output to NumPy array:\n" + str(e)
                )
                results["trials"].append(example_result)
                continue

            example_result["transformed_output"] = Grid(
                transformed_output, "", "", "", ""
            ).to_string()

            # --- Calculate Statistics ---
            # is size correct
            size_correct = transformed_output.shape == expected_output.shape
            example_result["size_correct"] = size_correct

            # do the color palettes match
            transformed_colors = set(np.unique(transformed_output))
            expected_colors = set(np.unique(expected_output))
            # TODO: why are we not testing if the two sets are equal
            color_palette_correct = transformed_colors.issubset(expected_colors)
            example_result["color_palette_correct"] = color_palette_correct

            # do the color counts match
            transformed_counts = dict(
                zip(*np.unique(transformed_output, return_counts=True))
            )
            expected_counts = dict(zip(*np.unique(expected_output, return_counts=True)))
            correct_pixel_counts = transformed_counts == expected_counts
            example_result["correct_pixel_counts"] = correct_pixel_counts

            # TODO: is it necessary to filter on size_correct?
            if size_correct:
                pixels_off = int(np.sum(transformed_output != expected_output))
                example_result["pixels_off"] = pixels_off
                example_result["percent_correct"] = 100 * (
                    (expected_output.size - pixels_off) / expected_output.size
                )

            if not np.array_equal(transformed_output, expected_output):
                example_result["match"] = False
            else:
                example_result["match"] = True

            results["trials"].append(example_result)

    return results



def write_test_results(test_results, task_dir, base_filename):
    """Formats test results as Markdown and writes to file, including saving images."""
    test_results_str = ""

    # Write JSON results
    test_results_json_file = task_dir / f"{base_filename}.json"
    with open(test_results_json_file, "w") as f:
        json.dump(test_results, f, indent=2)

    if "trials" in test_results:
        for result in test_results["trials"]:
            if "example" in result:  # It's an example result
                test_results_str += f"\n## example {result['example']}\n"
                test_results_str += f"*input:*\n```\n{result['input']}\n```\n"
                test_results_str += (
                    f"*expected output:*\n```\n{result['expected_output']}\n```\n"
                )

                if "transformed_output" in result:
                    test_results_str += f"*transformed output:*\n```\n{result['transformed_output']}\n```\n"

                    # Generate and save image of transformed output
                    try:
                        transformed_output_str = result["transformed_output"]  # NEW KEY
                        transformed_grid = string_to_grid(transformed_output_str)
                        transformed_image = transformed_grid.to_image()
                        image_filename = (
                            f"{base_filename}-example_{result['example']}.png"
                        )
                        image_path = task_dir / image_filename
                        transformed_image.save(image_path)

                    except ValueError as e:
                        test_results_str += f"**ERROR**: Could not create grid from transformed output: {e}\n"
                        continue  # Skip image creation and go to the next result
                    except Exception as e:  # Catch the PIL error
                        test_results_str += f"**ERROR**: Could not save image: {e}\n"
                        continue

                test_results_str += f"size: {result.get('size_correct')}\n"
                test_results_str += f"palette: {result.get('color_palette_correct')}\n"
                test_results_str += (
                    f"color count: {result.get('correct_pixel_counts')}\n"
                )
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


    return test_results_str
