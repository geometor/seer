"""
1. Find the Top-Left Blue: Iterate through the input grid, row by row. The first blue (1) pixel encountered is the "top-left blue". Record its row and column.
2. Move Zeroes: Move all zeroes (0) down one row
3. Transform Blues:
    *   If no blue pixel was found, skip this step.
    * replace all 1's with 2's, starting at column 0 of the top row, and
      proceeding to the end of the row.
4. Output Grid: Return a new grid that reflects all of these changes
"""

import numpy as np

def find_top_left_blue(grid):
    # Iterate through the grid row by row
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            # If a blue pixel (1) is found, return its coordinates
            if grid[i, j] == 1:
                return (i, j)
    # If no blue pixel is found, return None
    return None

def transform(input_grid):
    # Initialize output_grid as an empty array of the same size and type as input_grid, filled with zeros
    output_grid = np.zeros_like(input_grid)

    # Find top-left blue pixel
    top_left_blue = find_top_left_blue(input_grid)

    # shift 0s
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i,j] == 0:
                if i+1 < input_grid.shape[0]:
                    output_grid[i+1, j] = input_grid[i,j]


    # Transform blues based on top-left blue position
    if top_left_blue is not None:

        # get top row
        row = 0
        for col in range(input_grid.shape[1]):
            # check if there is 1 present in that row of the input
            if input_grid[row, col] == 1:
                # if yes, then start replacing
                output_grid[row, col] = 2

    return output_grid