"""
The transformation rule is to extract a 3xN subgrid centered on the vertical line of azure (8) pixels in the input grid. The output grid has the same number of rows as the input grid and 3 columns. The central column of the output is a copy of the column containing the vertical line of 8's. The other cells of the output are white (0), unless a row contains azure in both the original central azure column and an azure cell to its immediate left or right.
"""

import numpy as np

def find_vertical_line(grid, color):
    # Find the column index of the vertical line of the specified color.
    rows, cols = grid.shape
    for j in range(cols):
        if all(grid[i, j] == color for i in range(rows)):
            return j
    return -1  # Return -1 if no such line is found.

def transform(input_grid):
    # Convert input grid to a NumPy array
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape

    # Find the column with the vertical line of 8s.
    center_col = find_vertical_line(input_grid, 8)

    # Initialize the output grid as all zeros (white).
    output_grid = np.zeros((rows, 3), dtype=int)

    if center_col != -1:
        # copy central column
        for i in range(rows):
            output_grid[i,1] = input_grid[i,center_col]

        # copy horizontally adjancent cells
        for i in range(rows):
            if output_grid[i,1] == 8:
                if center_col > 0 and input_grid[i,center_col-1] == 8:
                    output_grid[i,0] = 8
                if center_col < cols-1 and input_grid[i, center_col+1] == 8:
                    output_grid[i,2] = 8


    return output_grid.tolist()