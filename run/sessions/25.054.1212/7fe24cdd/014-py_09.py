"""
The transformation rule is a cross-product-like expansion. Each cell in the 3x3 input grid maps to a 2x2 block in the 6x6 output grid, resulting in an expansion.
The expansion interacts with neighboring cells.
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((2 * rows, 2 * cols), dtype=int)

    for row in range(rows):
        for col in range(cols):
            # Each input cell maps to four output cell locations.
            output_grid[2*row][2*col] = input_grid[row][col]

            # Handle the cell to the right
            if col + 1 < cols:
                output_grid[2*row][2*col + 1] = input_grid[row][col+1]
            else:
                output_grid[2*row][2*col + 1] = 0

            # Handle the cell below.
            if row + 1 < rows:
                output_grid[2*row + 1][2*col] = input_grid[row+1][col]
            else:
                output_grid[2*row + 1][2*col] = 0

            # Handle the cell to the bottom right (mirrored from original cell)
            if row + 1 < rows and col + 1 < cols:
               output_grid[2*row+1][2*col+1] = input_grid[row][col]
            # cases where original cell is on an edge
            elif row + 1 == rows and col+1 < cols:
                output_grid[2*row + 1][2 * col + 1] = 0
            elif col + 1 == rows and row+1 < cols:
                output_grid[2*row + 1][2 * col + 1] = 0
            else:
                output_grid[2*row + 1][2*col+1] = 0


    return output_grid.tolist()