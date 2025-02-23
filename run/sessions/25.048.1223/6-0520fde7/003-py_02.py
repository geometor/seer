"""
Transformation Rule:

1. **Identify the Center:** Determine the center of the input grid.
2. **Extract a 3x3 Subgrid:** Imagine creating a 3x3 subgrid.
3. **Identify Gray Column:** Recognize that the central column.
4.  **Output Pattern:** Generate a specific 3x3 output grid based on the input:
        *   If the identified central column is ALL gray:
            *   A red (2) cell is placed in the center of each row of the output grid.
        *   Else:
            *   The output grid will be all white.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    center_col = cols // 2

    # Initialize the output grid as a 3x3 array filled with white (0)
    output_grid = np.zeros((3, 3), dtype=int)

    # Check if the entire center column is gray (5)
    if np.all(input_grid[:, center_col] == 5):
        # Place red (2) cells in the specified pattern
        output_grid[0, 1] = 2
        output_grid[1, 2] = 2
        output_grid[2, 1] = 2

    return output_grid