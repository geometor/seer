"""
The transformation removes the white background (color 0) from the input grid,
leaving the other colored regions unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Removes white background (color 0) from the input grid.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through all pixels
    for r in range(rows):
        for c in range(cols):
            # Check if the pixel is white (0)
            if output_grid[r, c] == 0:
                output_grid[r,c] = input_grid[r,c]

    return output_grid