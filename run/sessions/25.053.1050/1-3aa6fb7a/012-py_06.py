"""
1.  **Identify:** Find all azure (8) and white (0) pixels in the input grid.
2.  **Iterate:** For each white pixel, check its row.
3.  **Condition:** A white pixel changes to blue (1) *if and only if* there are azure pixels both to its immediate left and right on the *same* row.
4.  **Output:** The modified grid, with the appropriate white pixels changed to blue, is the final output.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # Check if the current cell is white
            if output_grid[r, c] == 0:
                # Check for azure neighbors to the immediate left and right on the same row
                if c > 0 and c < cols - 1 and output_grid[r, c - 1] == 8 and output_grid[r, c + 1] == 8:
                    output_grid[r, c] = 1  # Change white to blue

    return output_grid