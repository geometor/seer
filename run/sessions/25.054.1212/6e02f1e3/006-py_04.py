"""
Transforms a 3x3 input grid into a 3x3 output grid. The transformation fills the top row and the main diagonal with gray (5). All other cells are set to white (0).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the top row and main diagonal rule.
    """
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Iterate through the grid
    for i in range(rows):
        for j in range(cols):
            # Fill the top row with gray (5)
            if i == 0:
                output_grid[i, j] = 5
            #Fill the main diagonal
            elif i == j:
                output_grid[i,j] = 5
            # Fill other cells with white (0)
            else:
                output_grid[i, j] = 0

    return output_grid