"""
Copies red, blue, and magenta pixels from the input grid to the output grid. Adds yellow pixels diagonally adjacent to red pixels and orange pixels surrounding blue pixels.
"""

import numpy as np

def find_objects(grid, color):
    # Find the coordinates of all single-cell objects of the specified color.
    coords = np.where(grid == color)
    return list(zip(coords[0], coords[1]))

def transform(input_grid):
    """
    Transforms the input grid according to the defined rules:
    1. Copies red (2), blue (1), and magenta (6) pixels.
    2. Adds yellow (4) pixels diagonally adjacent to red pixels.
    3. Adds orange (7) pixels in all 8 neighboring positions around blue pixels.
    """
    output_grid = np.zeros_like(input_grid)

    # Find the red, blue and magenta pixels
    red_pixels = find_objects(input_grid, 2)
    blue_pixels = find_objects(input_grid, 1)
    magenta_pixels = find_objects(input_grid, 6)

    # Copy red, blue and magenta pixels
    for pos in red_pixels:
        output_grid[pos] = 2
    for pos in blue_pixels:
        output_grid[pos] = 1
    for pos in magenta_pixels:
        output_grid[pos]= 6

    # Add yellow pixels diagonally adjacent to red pixels
    for row, col in red_pixels:
        if row > 0 and col > 0:
          output_grid[row - 1, col-1] = 4  # Up-left
        if row > 0 and col < output_grid.shape[1] - 1:
          output_grid[row - 1, col+1] = 4  # Up-right
        if row < output_grid.shape[0] - 1 and col > 0:
          output_grid[row + 1, col-1] = 4  # Down-left
        if row < output_grid.shape[0] - 1 and col < output_grid.shape[1] - 1:
          output_grid[row + 1, col+1] = 4  # Down-right


    # Add orange pixels around the blue pixel (8-neighbors)
    for row, col in blue_pixels:
        for i in range(max(0, row - 1), min(output_grid.shape[0], row + 2)):
            for j in range(max(0, col - 1), min(output_grid.shape[1], col + 2)):
                output_grid[i, j] = 7

    return output_grid