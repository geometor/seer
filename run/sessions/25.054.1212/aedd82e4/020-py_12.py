"""
The transformation replaces the white (0) cells in the bottom-right 2x2 subgrid with blue (1).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by changing white (0) cells in the bottom-right 2x2 subgrid to blue (1).
    """
    output_grid = np.copy(input_grid)  # Create a copy to avoid modifying the original
    rows, cols = output_grid.shape

    # Iterate through the bottom-right 2x2 subgrid
    for i in range(rows - 2, rows):
        for j in range(cols - 2, cols):
            # Check if the cell is white (0)
            if output_grid[i, j] == 0:
                # Change the color to blue (1)
                output_grid[i, j] = 1

    return output_grid