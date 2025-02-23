"""
Shift all pixels down by one row, wrapping from bottom to top.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by shifting all pixels down by one row,
    with wraparound from the bottom to the top.
    """
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Iterate through each pixel in the input grid
    for r in range(rows):
        for c in range(cols):
            # Calculate the new row index with wraparound
            new_row = (r + 1) % rows
            # Copy the pixel value to the new position in the output grid
            output_grid[new_row, c] = input_grid[r, c]

    return output_grid