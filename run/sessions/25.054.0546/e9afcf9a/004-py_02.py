"""
The transformation takes a 2x6 grid as input. The output grid is also 2x6.
The output grid exhibits a checkerboard pattern. The colors used in the
checkerboard pattern are derived from the input grid. The color of the first
row of the input grid becomes the color of the top-left cell of the output
grid, and the color of the second row of the input grid becomes the color of
the cell directly below the top-left cell of the output grid. Colors then
alternate in a checkerboard fashion.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid with the same dimensions as the input
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols), dtype=int)

    # Get the colors from the first and second rows of the input grid
    color_row1 = input_grid[0, 0]
    color_row2 = input_grid[1, 0]

    # Iterate through each cell of the output grid
    for i in range(rows):
        for j in range(cols):
            # Alternate colors based on row and column indices
            if (i + j) % 2 == 0:
                output_grid[i, j] = color_row1  # Even sum: color from first row
            else:
                output_grid[i, j] = color_row2  # Odd sum: color from second row

    return output_grid