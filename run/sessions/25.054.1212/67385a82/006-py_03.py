"""
Transforms an input grid based on the following rule:

Green pixels in the top two rows (row index 0 or 1) are changed to azure.
All other pixels remain unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through the grid and apply the transformation rule.
    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] == 3:  # Check if the cell is green.
                if r < 2:  # Top two rows.
                    output_grid[r, c] = 8  # Change to azure.
            # Non-green pixels and green pixels outside top two rows remain unchanged.

    return output_grid