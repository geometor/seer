"""
1.  **Rotate:** Rotate the entire input grid by 180 degrees.
2.  **Color Transform:** In the rotated grid, change all gray (5) pixels to red (2).
3.  **Set to Black:** Change all other pixels (that were not originally gray) in the rotated grid to black (0).
"""

import numpy as np

def rotate_grid(grid):
    """Rotates a 2D numpy array by 180 degrees."""
    return np.rot90(grid, 2)

def transform(input_grid):
    """Transforms the input grid according to the rules."""
    # Rotate the input grid by 180 degrees.
    rotated_grid = rotate_grid(input_grid)

    # Initialize the output grid as a copy of the rotated grid.
    output_grid = rotated_grid.copy()

    # Iterate through the rotated grid and apply color transformations.
    rows, cols = output_grid.shape
    for i in range(rows):
        for j in range(cols):
            if output_grid[i, j] == 5:  # If the pixel is gray (5)
                output_grid[i, j] = 2   # Change it to red (2)
            else:                      # Otherwise
                output_grid[i, j] = 0   # Change it to black (0)

    return output_grid