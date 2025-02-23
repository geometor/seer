"""
Identifies connected azure (8) colored objects and replaces some azure pixels with blue (1) if the azure pixels are adjacent to empty space (0).
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through the grid
    for r in range(rows):
        for c in range(cols):
            # Check if the current pixel is azure
            if output_grid[r, c] == 8:
                # Check for empty space to the right and if the adjacent pixel is also azure
                if c + 1 < cols and input_grid[r, c + 1] == 0 and (c+2 < cols and input_grid[r,c+2] == 8):
                    output_grid[r, c+1] = 1
                # Check for empty space below and if the adjacent pixel is also azure
                if r + 1 < rows and input_grid[r + 1, c] == 0 and (r + 2 < rows and input_grid[r+2, c] == 8):
                    output_grid[r+1, c] = 1
                # check for empty space to the left and if the adjacent pixel is also azure
                if c - 1 >= 0 and input_grid[r, c - 1] == 0 and (c-2 >= 0 and input_grid[r, c-2] == 8) :
                    output_grid[r, c-1] = 1
                # check for empty space above and if the adjacent pixel is also azure
                if r - 1 >= 0 and input_grid[r - 1, c] == 0 and (r - 2 >= 0 and input_grid[r-2,c] == 8):
                    output_grid[r-1, c] = 1

    return output_grid