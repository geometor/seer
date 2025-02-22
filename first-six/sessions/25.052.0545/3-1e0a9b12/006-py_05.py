"""
Translates a 2x2 square from the top-left corner to the bottom-right corner of a 3x3 grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving the 2x2 gray square to the bottom-right.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)

    # Find the 2x2 square (assuming it's in the top-left)
    square_color = input_grid[0, 0]

    # Check if the top-left 2x2 is indeed a square of the same color
    if (input_grid[0:2, 0:2] == square_color).all() and square_color != 0:
         # Move the square to the bottom-right
         output_grid[1:3, 1:3] = square_color

    return output_grid