"""
Shifts a diagonal line of gray cells down and to the right by one cell.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by shifting the diagonal line of gray cells.

    Args:
        input_grid (list of lists): The input grid.

    Returns:
        list of lists: The transformed output grid.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols), dtype=int)

    # Find the diagonal and shift it
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 5:
                if r + 1 < rows and c + 1 < cols:
                    output_grid[r + 1, c + 1] = 5

    return output_grid.tolist()