"""
1. Identify a 2x2 square of azure pixels in the input grid.
2. Change the color of this square from azure to red.
3. Move the now red square down by one row.
4. The rest of the grid remains unchanged (white).
"""

import numpy as np

def find_square(grid, color, size):
    """Finds a square of a given color and size in the grid."""
    height, width = grid.shape
    for i in range(height - size + 1):
        for j in range(width - size + 1):
            if np.all(grid[i:i+size, j:j+size] == color):
                return i, j
    return None

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find the azure square
    square_pos = find_square(input_grid, 8, 2)

    if square_pos:
        row, col = square_pos

        # Clear the original square
        output_grid[row:row+2, col:col+2] = 0
        
        # Move the square down by one row and change color to red
        output_grid[row+1:row+3, col:col+2] = 2

    return output_grid