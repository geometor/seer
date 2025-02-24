"""
The input grid is transformed by replacing white (0) pixels with a repeating pattern of magenta (6), green (3), and red (2), starting the pattern based on non-zero values to the left. The dimensions of the grid remain the same.
"""

import numpy as np

def get_left_non_zero_neighbor(grid, row, col):
    """Finds the nearest non-zero pixel to the left in the same row.
       Returns the color, and -1, -1 if there is not a non-zero pixel to the left
    """
    for c in range(col - 1, -1, -1):
        if grid[row, c] != 0:
            return grid[row, c]
    return -1

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""

    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 0:
                left_neighbor_color = get_left_non_zero_neighbor(input_grid, r, c)
                if left_neighbor_color == 5:

                  pattern = [6,3,3]
                  if input_grid[r,3] == 2:
                    pattern = [2,3,3]
                  output_grid[r,c] = pattern[(c-4)%len(pattern)]

    return output_grid