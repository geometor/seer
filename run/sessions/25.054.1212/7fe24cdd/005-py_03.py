import numpy as np

def analyze_pixel_mapping(input_grid, expected_output_grid):
    """
    Analyzes the mapping of each input pixel to output pixels.

    Args:
        input_grid: The input grid as a NumPy array.
        expected_output_grid: The expected output grid as a NumPy array.

    Returns:
        A dictionary where keys are input pixel coordinates (i, j) and
        values are lists of corresponding output pixel coordinates [(oi1, oj1), (oi2, oj2), ...].
    """

    input_height, input_width = input_grid.shape
    output_height, output_width = expected_output_grid.shape
    mapping = {}

    for i in range(input_height):
        for j in range(input_width):
            input_pixel = input_grid[i, j]
            output_coordinates = []
            for oi in range(output_height):
                for oj in range(output_width):
                    if expected_output_grid[oi, oj] == input_pixel:
                        output_coordinates.append((oi, oj))
            mapping[(i, j)] = output_coordinates

    return mapping

def report(task_id, input_grid, expected_output, code_output):
    print(f"Task: {task_id}")
    print("Input:\n", input_grid)
    print("Expected Output:\n", expected_output)
    print("Code Output:\n", code_output)

    if code_output.shape != expected_output.shape:
        print("Incorrect output size")
        return

    print("Mapping:")
    mapping_data = analyze_pixel_mapping(input_grid, expected_output)
    for in_coord, out_coords in mapping_data.items():
        print(f"  Input {in_coord} -> Output: {out_coords}")

    matches = np.array_equal(code_output, expected_output)
    print(f"{matches=}")
    if not matches:
        pixels_off = np.sum(code_output != expected_output)
        print(f"{pixels_off=}")

    print("=" * 20)


# Example Usage (replace with your actual task data)
task_1_input = np.array([[8, 5, 0], [8, 5, 3], [0, 3, 2]])
task_1_expected = np.array([[8, 5, 0, 0, 8, 8], [8, 5, 3, 3, 5, 5], [0, 3, 2, 2, 3, 0], [0, 3, 2, 2, 3, 0], [5, 5, 3, 3, 5, 8], [8, 8, 0, 0, 5, 8]])
task_1_code = np.array([[8, 8, 5, 5, 0, 0], [8, 8, 5, 5, 0, 0], [8, 8, 5, 5, 3, 3], [8, 8, 5, 5, 3, 3], [0, 0, 3, 3, 2, 2], [0, 0, 3, 3, 2, 2]])

task_2_input = np.array([[3, 8, 2], [3, 2, 2], [8, 5, 2]])
task_2_expected = np.array([[3, 8, 2, 8, 3, 3], [3, 2, 2, 5, 2, 8], [8, 5, 2, 2, 2, 2], [2, 2, 2, 2, 5, 8], [8, 2, 5, 2, 2, 3], [3, 3, 8, 2, 8, 3]])
task_2_code = np.array([[3, 3, 8, 8, 2, 2], [3, 3, 8, 8, 2, 2], [3, 3, 2, 2, 2, 2], [3, 3, 2, 2, 2, 2], [8, 8, 5, 5, 2, 2], [8, 8, 5, 5, 2, 2]])

task_3_input = np.array([[0, 3, 0], [6, 6, 6], [0, 3, 0]])
task_3_expected = np.array([[0, 3, 0, 0, 6, 0], [6, 6, 6, 3, 6, 3], [0, 3, 0, 0, 6, 0], [0, 6, 0, 0, 3, 0], [3, 6, 3, 6, 6, 6], [0, 6, 0, 0, 3, 0]])
task_3_code = np.array([[0, 0, 3, 3, 0, 0], [0, 0, 3, 3, 0, 0], [6, 6, 6, 6, 6, 6], [6, 6, 6, 6, 6, 6], [0, 0, 3, 3, 0, 0], [0, 0, 3, 3, 0, 0]])

report("Task 1", task_1_input, task_1_expected, task_1_code)
report("Task 2", task_2_input, task_2_expected, task_2_code)
report("Task 3", task_3_input, task_3_expected, task_3_code)
