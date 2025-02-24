"""
1.  **Input:** Receive a 2D grid of color values.
2.  **Rotation**: Rotate the grid 90 degrees clockwise.
3.  **Identify Non-White:** Locate all pixels in the rotated input grid that are not white (0).
4.  **Create Output Grid:** Create a 3x3 output grid initialized with all zeros (white).
5.  **Map Colors:** For the first 3 rows and 3 columns of the rotated input, map any non-white pixel to the value 6 (magenta) in the corresponding location in the output grid.
6.  **Output:** Return the 3x3 output grid.
"""

import numpy as np

def rotate_grid(grid):
    """Rotates a 2D grid 90 degrees clockwise."""
    return np.rot90(grid, k=-1).tolist()


def transform(input_grid):
    # Rotate the input grid 90 degrees clockwise
    rotated_grid = rotate_grid(input_grid)
    
    # Create a 3x3 output grid initialized with zeros
    output_grid = [[0] * 3 for _ in range(3)]

    # Iterate through the first 3 rows and columns of the rotated grid
    for i in range(min(3, len(rotated_grid))):
        for j in range(min(3, len(rotated_grid[0]))):
            # If the pixel is not white, map it to 6 in the output grid
            if rotated_grid[i][j] != 0:
                output_grid[i][j] = 6

    return output_grid