"""
Locate a 3x3 square region of gray (5) pixels and change all pixels within this region to blue (1).
Leave every other pixel unchanged.
"""

import numpy as np

def find_3x3_gray_square(grid):
    # Find a 3x3 gray square.  This version looks at a specific location.
    rows, cols = grid.shape
    for r in range(rows - 2):
        for c in range(cols - 2):
            if all(grid[r+i][c+j] == 5 for i in range(3) for j in range(3)):
                return (r, c)
    return None

def transform(input_grid):
    """
    Transforms the input grid by changing a single 3x3 gray square to blue.
    """
    output_grid = np.copy(input_grid)  # Initialize output as a copy of the input

    # Find the coordinates of the 3x3 gray square.
    square_coords = find_3x3_gray_square(input_grid)

    if square_coords:
      #change the output
        row, col = square_coords
        for i in range(3):
            for j in range(3):
                output_grid[row + i][col + j] = 1  # Change to blue

    return output_grid