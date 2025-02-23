"""
Transforms a 3x3 input grid into a 3x3 output grid. The transformation replaces the values along both the main diagonal (top-left to bottom-right) and the anti-diagonal (top-right to bottom-left) with 5 (gray).  All other grid cells are replaced with 0 (white).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the diagonal replacement rule.
    """
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Iterate through the grid
    for i in range(rows):
        for j in range(cols):
            # Check if the cell is on the main diagonal or anti-diagonal
            if i == j or i + j == rows - 1:
                output_grid[i, j] = 5  # Set to gray
            else:
                output_grid[i, j] = 0  # Set to white

    return output_grid