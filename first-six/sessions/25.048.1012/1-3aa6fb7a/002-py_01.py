"""
The transformation rule can be described as background. For each cell, If a cell, that is not part of a azure rectangle, is between two azure colored cells (neighbor to the left is azure and neighbor to the right is azure), change the cells to blue (1).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    If a cell (not color 8) has a direct neighbor to the left of color 8 and a direct neighbor to the right of color 8, change it to color 1.
    """
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each cell of the grid
    for r in range(rows):
        for c in range(cols):
            # Check if the current cell is not azure (color 8)
            if input_grid[r, c] != 8:
                # Check for azure neighbors to the left and right
                if c > 0 and c < cols - 1 and input_grid[r, c-1] == 8 and input_grid[r, c+1] == 8:
                    output_grid[r, c] = 1  # Change the cell color to blue (1)

    return output_grid