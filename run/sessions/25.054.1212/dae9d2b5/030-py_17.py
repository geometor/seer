"""
1.  **Input:** Take the 2D input grid.
2.  **Rotate:** Rotate the entire input grid 90 degrees clockwise.
3.  **Output Initialization:** Create a new 3x3 output grid, initially filled entirely with white pixels (0).
4.  **Conditional Color Mapping:** Examine the top-left 3x3 region of the *rotated* grid.  For each cell within this 3x3 region:
    *   If the cell in the rotated grid is *not* white (0), set the corresponding cell in the output grid to magenta (6).
    *   If the cell in the rotated grid *is* white (0), leave the corresponding cell in the output grid as white (0).
5.  **Output:** Return the 3x3 output grid.
"""

import numpy as np

def rotate_grid(grid):
    """Rotates a 2D grid 90 degrees clockwise."""
    return np.rot90(grid, k=-1).tolist()

def transform(input_grid):
    # Rotate the input grid 90 degrees clockwise
    rotated_grid = rotate_grid(input_grid)

    # Create a 3x3 output grid initialized with zeros (white)
    output_grid = [[0] * 3 for _ in range(3)]

    # Iterate through the first 3 rows and columns of the rotated grid
    for i in range(min(3, len(rotated_grid))):
        for j in range(min(3, len(rotated_grid[0]))):
            # If the pixel is not white, map it to 6 in the output grid
            if rotated_grid[i][j] != 0:
                output_grid[i][j] = 6

    return output_grid