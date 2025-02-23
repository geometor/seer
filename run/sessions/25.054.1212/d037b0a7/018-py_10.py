"""
1.  Iterate through the input grid.
2.  If a yellow pixel (value 4) is found, duplicate it downwards until the end of the column.
3.  If a red pixel (value 2) is found, duplicate it downwards until the end of the column.
4.  Other pixels in columns without red or yellow remain unchanged.
5.  If a column has both yellow and red, both are propogated, and the propogation to the right of the first pixel takes precidence.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each column
    for c in range(cols):
        # Find yellow and red pixels in the current column
        yellow_found = False
        red_found = False
        yellow_row = -1
        red_row = -1

        for r in range(rows):
            if output_grid[r, c] == 4:
                yellow_found = True
                yellow_row = r
            elif output_grid[r, c] == 2:
                red_found = True
                red_row = r

        # Duplicate downwards if found
        if yellow_found:
            for r in range(yellow_row + 1, rows):
                output_grid[r, c] = 4
        if red_found:
            for r in range(red_row + 1, rows):
                output_grid[r, c] = 2

    return output_grid