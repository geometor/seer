"""
The transformation rule is to replace the input grid with a grid of the same dimensions, where all cell values are 9 (maroon).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms an input grid into an output grid of the same dimensions,
    with all cells set to the value 9.
    """
    # Get the dimensions of the input grid.
    rows = len(input_grid)
    cols = len(input_grid[0])

    # Create a new grid of the same dimensions, filled with 9s.
    output_grid = np.full((rows, cols), 9)

    # Return the new grid.
    return output_grid