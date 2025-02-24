"""
1.  **Initialization:** Start with the input grid. Create a copy of the input grid, this will become the output grid.
2.  **Locate Blue Pixels:** Examine row 3 (index 2) of the input grid. Identify the column indices where the pixels are blue (value 1).
3.  **Conditional Modification:** For each column index found in step 2:
    *   Check the pixel at row 5 (index 4) and the located column index within the *output* grid.
    *   If that pixel in the *output* grid is gray (5), change it to blue (1).
    * if that pixel is not gray (5), do not modify
4.  **Output:** The modified copy is the output grid.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)

    # Find column indices where row 3 has blue pixels (value 1).
    blue_indices = np.where(input_grid[2] == 1)[0]

    # Modify corresponding pixels in row 5 of the output grid.
    for col_index in blue_indices:
        if output_grid[4, col_index] == 5:  # Check if it's gray (5)
            output_grid[4, col_index] = 1  # Change to blue (1)

    return output_grid