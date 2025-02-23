"""
The transformation involves rotating the gray corner cells clockwise by one position. The red cell in the center remains fixed.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by rotating the gray corner cells clockwise by one position,
    while the red center cell remains fixed.
    """
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Identify gray corner positions
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    gray_corners = [pos for pos in corners if input_grid[pos] == 5]

    # Rotate gray corners clockwise
    rotated_corners = {}
    for r, c in gray_corners:
        if (r, c) == (0, 0):
            rotated_corners[(0, 2)] = 5
        elif (r, c) == (0, 2):
            rotated_corners[(2, 2)] = 5
        elif (r, c) == (2, 2):
            rotated_corners[(2, 0)] = 5
        elif (r, c) == (2, 0):
            rotated_corners[(0, 0)] = 5

    # Update output grid, keeping the original grid and placing the rotated corners.
    for (r,c), value in rotated_corners.items():
          output_grid[r,c] = value

    return output_grid