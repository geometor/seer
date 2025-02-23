"""
Divide the input grid into four quadrants and represent each quadrant in a 2x2 output grid.  If a quadrant contains any non-zero color, the corresponding output cell will have that color.  If a quadrant contains only zeros, the output cell will be zero.
"""

import numpy as np

def get_first_nonzero(quadrant):
    """
    Returns the first non-zero element in a quadrant, or 0 if none are found.
    """
    for value in quadrant.flatten():
        if value != 0:
            return value
    return 0

def transform(input_grid):
    """
    Transforms an input grid into a 2x2 output grid based on the presence of any non-zero color in each quadrant.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((2, 2), dtype=int)

    # Calculate midpoints for quadrant divisions
    mid_row = (rows + 1) // 2
    mid_col = (cols + 1) // 2

    # Define quadrant boundaries
    quadrants = [
        (0, mid_row, 0, mid_col),       # Top-left
        (0, mid_row, mid_col, cols),   # Top-right
        (mid_row, rows, 0, mid_col),       # Bottom-left
        (mid_row, rows, mid_col, cols)    # Bottom-right
    ]

    # Iterate through quadrants and check for non-zero colors
    for i, (row_start, row_end, col_start, col_end) in enumerate(quadrants):
        quadrant = input_grid[row_start:row_end, col_start:col_end]
        # Get first non-zero value in quadrant
        first_non_zero_val = get_first_nonzero(quadrant)
        output_grid[i // 2, i % 2] = first_non_zero_val

    return output_grid.tolist()