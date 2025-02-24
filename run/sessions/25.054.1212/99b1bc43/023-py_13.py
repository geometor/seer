import numpy as np

def get_color_extents(grid):
    """
    Finds the bounding box for non-zero colors in the grid.

    Returns:
        A dictionary where keys are colors and values are (min_row, max_row, min_col, max_col) tuples.
        Returns an empty dictionary if no non-zero colors are found.
    """
    color_extents = {}
    rows, cols = np.where(grid != 0)
    if len(rows) > 0:
        min_row, max_row = np.min(rows), np.max(rows)
        min_col, max_col = np.min(cols), np.max(cols)
        color_extents[1] = (min_row, max_row, min_col, max_col) #color is essentially irrelevant
    return color_extents

def analyze_example(input_grid, expected_output, transformed_output):
    """Analyzes a single example and returns relevant metrics."""
    input_extents = get_color_extents(input_grid)
    expected_extents = get_color_extents(expected_output)
    transformed_extents = get_color_extents(transformed_output)

    print(f"Input Extents: {input_extents}")
    print(f"Expected Extents: {expected_extents}")
    print(f"Transformed Extents: {transformed_extents}")


#Example data provided in problem
input_grids = [
    np.array([[0, 1, 0, 1], [0, 0, 0, 1], [1, 0, 1, 0], [0, 0, 0, 1], [4, 4, 4, 4], [0, 2, 0, 2], [0, 0, 0, 2], [2, 0, 0, 2], [2, 2, 2, 0]]),
    np.array([[1, 1, 0, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], [4, 4, 4, 4], [0, 2, 2, 2], [2, 0, 2, 0], [2, 2, 2, 2], [2, 2, 2, 2]]),
    np.array([[0, 1, 0, 0], [1, 0, 1, 1], [1, 1, 1, 0], [1, 1, 1, 0], [4, 4, 4, 4], [0, 0, 0, 0], [0, 2, 0, 2], [2, 2, 0, 2], [0, 2, 0, 0]]),
    np.array([[1, 0, 1, 1], [0, 0, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [4, 4, 4, 4], [0, 2, 2, 2], [0, 2, 2, 2], [2, 0, 2, 2], [2, 2, 2, 2]])
]
expected_outputs = [
    np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 3, 3], [3, 3, 3, 3]]),
    np.array([[3, 0, 3, 3], [0, 0, 0, 0], [0, 0, 3, 0], [3, 0, 0, 3]]),
    np.array([[0, 3, 0, 0], [3, 3, 3, 0], [0, 0, 3, 3], [3, 0, 3, 0]]),
    np.array([[3, 3, 0, 0], [0, 3, 3, 0], [0, 3, 3, 3], [3, 3, 0, 0]])
]
transformed_outputs = [
    np.array([[0, 3, 0, 3], [0, 0, 0, 3], [3, 0, 3, 0], [0, 0, 0, 3]]),
    np.array([[3, 3, 0, 0], [3, 0, 3, 0], [3, 3, 0, 3], [0, 3, 3, 0]]),
    np.array([[0, 3, 0, 0], [3, 0, 3, 3], [3, 3, 3, 0], [3, 3, 3, 0]]),
    np.array([[3, 0, 3, 3], [0, 0, 0, 3], [3, 3, 0, 0], [0, 0, 3, 3]])
]

for i in range(len(input_grids)):
    print(f"--- Example {i+1} ---")
    analyze_example(input_grids[i], expected_outputs[i], transformed_outputs[i])