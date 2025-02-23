"""
1.  **Find the Blue Column:** Scan the input grid to locate the single column that is entirely filled with blue (1) pixels. Note its index. If no such column is found, no transformation occurs.
2.  **Create Output Grid:** Create an output grid that has the same height as the input grid but with the width fixed to 3 columns.
3.  **Transform Blue Column:** The blue column in the input grid is transformed to azure (8) in the output grid's center column (index 1).
4.  **Process Adjacent Columns**:
    *   For each row, examine the pixels immediately to the left and right of the original blue column in the input grid.
        *   If the left and right pixels have the same color, copy these pixels to the left and right of the new azure column in the output.
        * If the left and right pixels have different colors, the output is black (0).
"""

import numpy as np

def find_blue_column(grid):
    """Finds the index of the all-blue column."""
    for j in range(grid.shape[1]):
        if np.all(grid[:, j] == 1):
            return j
    return -1

def transform(input_grid):
    """Transforms the input grid based on the blue column rule."""
    blue_column_index = find_blue_column(input_grid)

    if blue_column_index == -1:
        return None  # Or perhaps return the original grid, depending on desired behavior

    output_grid = np.zeros((input_grid.shape[0], 3), dtype=int)

    # Fill the center column with azure (8)
    output_grid[:, 1] = 8

    # Process adjacent columns
    for row in range(input_grid.shape[0]):
        left_val = input_grid[row, blue_column_index - 1] if blue_column_index > 0 else None
        right_val = input_grid[row, blue_column_index + 1] if blue_column_index < input_grid.shape[1] - 1 else None

        if left_val is not None and right_val is not None:
            if left_val == right_val:
                output_grid[row, 0] = left_val
                output_grid[row, 2] = right_val
            else:
                output_grid[row, 0] = 0
                output_grid[row, 2] = 0
        elif left_val is not None:
            output_grid[row,0] = 0
            output_grid[row,2] = 0
        elif right_val is not None:
            output_grid[row,0] = 0
            output_grid[row,2] = 0
    return output_grid