"""
The transformation identifies two rectangular objects, one blue (1) and one orange (7), and applies a checkerboard pattern to each. The checkerboarding alternates the object's color with 0 (background), starting the alternation in the second column for both objects in the rectangle.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a checkerboard pattern to the blue and orange rectangles,
    starting the alternation at the second column for both.

    Args:
        input_grid (numpy.ndarray): The input grid.

    Returns:
        numpy.ndarray: The transformed output grid.
    """
    output_grid = np.copy(input_grid)

    # Helper function to apply checkerboard pattern
    def apply_checkerboard(grid, color, start_offset):
        rows, cols = np.where(grid == color)
        if rows.size > 0:  # Check if the color exists
            min_row, max_row = np.min(rows), np.max(rows)
            min_col, max_col = np.min(cols), np.max(cols)

            for i in range(min_row, max_row + 1):
                for j in range(min_col, max_col + 1):
                    if (i + j) % 2 != 0:
                        grid[i, j] = 0
        return grid

    # Apply checkerboard to blue (1)
    output_grid = apply_checkerboard(output_grid, 1, 1)

    # Apply checkerboard to orange (7)
    output_grid = apply_checkerboard(output_grid, 7, 1)


    return output_grid