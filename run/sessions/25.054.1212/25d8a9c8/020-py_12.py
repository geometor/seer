"""
1.  **Examine the bottom row of the input grid.**
    *   If all cells in the bottom row of the input have the same value (and therefore, color)
2.  **Modify the Bottom Row.** Set all values in the output grid's bottom row to the value 5 (gray).
3.  **Modify all other rows.** Set all the values in all other rows of the output grid to 0 (white)

In summary, the transformation detects if the entire bottom row of input is of the same color, it changes bottom row of the output grid all to grey, and the other rows all to white.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""

    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Initialize output_grid to all white (0).
    output_grid[:] = 0

    # Check if the bottom row has all the same values.
    if np.all(input_grid[-1, :] == input_grid[-1, 0]):
        # Set the bottom row to gray (5).
        output_grid[-1, :] = 5

    return output_grid