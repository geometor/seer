"""
The transformation takes the location of the initial blue pixel and uses it as
the origin of the entire output pattern. It extends a diagonal line of blue
pixels, wrapping around to the left when it hits the right edge, and continues
until the entire output grid is filled.
"""

import numpy as np

def find_seed(grid):
    # Find the coordinates of the blue pixel (value 1).
    rows, cols = np.where(grid == 1)
    if len(rows) > 0:
        return rows[0], cols[0]
    return None

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid, but all white.
    output_grid = np.zeros_like(input_grid)
    height, width = input_grid.shape

    # Find the seed (the initial blue pixel).
    seed = find_seed(input_grid)
    if seed is None:
        return output_grid # return all white grid if no seed
    
    seed_row, seed_col = seed

    # initialize output grid with seed position
    output_grid[seed_row, seed_col] = 1

    # propagate the pattern
    row = seed_row
    col = seed_col
    
    for i in range(height):
        # place pixel to the right
        row = (row - 1) % height
        col = (col + 1) % width
        output_grid[row, col] = 1

        # place pixel back to the left
        row = (row - 1) % height
        col = (col - 1) % width
        output_grid[row, col] = 1
    

    return output_grid