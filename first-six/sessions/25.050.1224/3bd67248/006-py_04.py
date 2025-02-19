"""
The input grid has a vertical line of a specific color on the leftmost edge. The transformation creates a red (2) diagonal line from the bottom-left to the top-right corner. The bottom row is changed to yellow (4), except for the first cell, which retains its original color. The rest of the grid becomes white (0).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    output_grid = np.zeros_like(input_grid)

    # Keep first column the same
    output_grid[:, 0] = input_grid[:, 0]

    # Create a red diagonal
    for i in range(input_grid.shape[0]):
        output_grid[i, input_grid.shape[1] - 1 - i] = 2

    # Make the last row yellow, except for the first cell
    output_grid[-1, 1:] = 4
    output_grid[-1, 0] = input_grid[-1, 0]

    return output_grid