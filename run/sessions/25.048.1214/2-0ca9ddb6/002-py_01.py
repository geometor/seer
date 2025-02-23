"""
The transformation rule involves identifying single-pixel red and blue objects. A 2x2 yellow square is drawn, cross-like, centered on the red object's original location, and a three-length orange cross is created around the blue object.  The red and blue pixels are preserved, and the background remains unchanged.
"""

import numpy as np

def find_object(grid, color):
    # Find the coordinates of a single-pixel object of the specified color.
    coords = np.where(grid == color)
    if len(coords[0]) > 0:
        return (coords[0][0], coords[1][0])  # Return first instance of the color
    return None

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Find the red object (color 2).
    red_pos = find_object(input_grid, 2)
    if red_pos:
        # Draw a yellow cross centered on the red object
        row, col = red_pos
        for i in range(-1,2):
            output_grid[row+i, col] = 4 if abs(i) == 1 else output_grid[row+i,col]
            output_grid[row, col+i] = 4 if abs(i) == 1 else output_grid[row,col+i]

    # Find the blue object (color 1).
    blue_pos = find_object(input_grid, 1)
    if blue_pos:
        # Draw an orange cross around the blue object.
        row, col = blue_pos
        for i in range(-1, 2):
            output_grid[row + i, col] = 7 if abs(i)==1 else output_grid[row + i, col]
            output_grid[row, col + i] = 7 if abs(i) == 1 else output_grid[row, col+i]

    return output_grid