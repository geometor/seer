"""
The transformation combines a green (3) cross shape onto the existing background grid. The cross shape is centered on the grid,
with its arms extending nearly to the edges, leaving a one-pixel border.
"""

import numpy as np

def transform(input_grid):
    """
    Combines a green cross shape onto the input grid.
    """
    # Initialize output_grid as a copy of the input grid
    output_grid = input_grid.copy()
    rows, cols = output_grid.shape

    # Determine the center of the grid
    center_row = rows // 2
    center_col = cols // 2

    # Create the vertical part of the cross, extending to one pixel from the edges
    for r in range(1, rows - 1):
        output_grid[r, center_col] = 3

    # Create the horizontal part of the cross, extending to one pixel from the edges
    for c in range(1, cols - 1):
        output_grid[center_row, c] = 3

    return output_grid