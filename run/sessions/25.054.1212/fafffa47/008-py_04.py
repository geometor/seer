"""
Extracts and transforms color information from the top half of the input grid (maroon (9) becomes red (2), white (0) remains the same), then creates a 3x3 output grid representing this transformed top half, effectively discarding the bottom half of the input grid.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros((3, 3), dtype=int)

    # Iterate over the top 3 rows of the input grid (the top region).
    for i in range(3):
        for j in range(3):
            # Apply color mapping: 9 -> 2, 0 -> 0
            if input_grid[i][j] == 9:
                output_grid[i][j] = 2
            elif input_grid[i][j] == 0:
                output_grid[i][j] = 0
            # Implicitly, other values are ignored as the output grid starts filled with 0s.

    return output_grid