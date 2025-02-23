"""
Identifies and removes all pixels with a value of 0 (white) in the input grid.
"""

import numpy as np

def transform(input_grid):
    """
    Removes all white (0) pixels from the input grid.
    """
    # Create a copy of the input grid to serve as the output grid.
    output_grid = input_grid.copy()
    rows, cols = output_grid.shape

    # Iterate through all pixels
    for r in range(rows):
        for c in range(cols):
            # Check if the pixel is white (0)
            if output_grid[r, c] == 0:
                # set to some other value to test simple replace
                output_grid[r,c] = 1

    return output_grid