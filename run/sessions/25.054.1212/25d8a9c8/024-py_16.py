"""
1.  **Examine the bottom row of the input grid.**
    *   Determine if all cells in the bottom row of the input grid have the same value.
2.  **Initialize the output grid.** Create an output grid of the same dimensions as the input grid, and initialize all cells to 0 (white).
3.  **Conditionally modify the bottom row of the output grid.**
    *  If all cells in the bottom row of the *input* grid had the same value, set all cells in the bottom row of the *output* grid to 5 (gray).
4.  All other rows remain at their initialized value of 0 (white).

In summary: Create an output grid that is all white, except the bottom row. The bottom row of the output is grey if and only if the bottom row of the input grid had all the same value (color). Otherwise the bottom row will also be white.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""

    # Initialize output_grid to all white (0) and same shape as input
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Check if the bottom row of the input grid has all the same values.
    if np.all(input_grid[-1, :] == input_grid[-1, 0]):
        # Set the bottom row of the output grid to gray (5).
        output_grid[-1, :] = 5

    return output_grid