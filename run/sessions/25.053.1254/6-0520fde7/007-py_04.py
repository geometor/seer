"""
The transformation creates a 3x3 output grid. The grey (5) object in the input grid determines the placement of red (2) pixels in the output grid. Specifically, the red pixels appear at locations one column to the left of the grey object's column, using the same row indices. All other pixels in the output grid are black (0).
"""

import numpy as np

def get_grey_column(grid):
    # Find the column index where grey (5) pixels are located.
    grid = np.array(grid)
    for col in range(grid.shape[1]):
        if np.any(grid[:, col] == 5):
            return col
    return -1  # Should not happen, based on problem description.

def transform(input_grid):
    # Initialize a 3x3 output grid filled with black (0).
    output_grid = np.zeros((3, 3), dtype=int)

    # Get the column of the grey object.
    grey_column = get_grey_column(input_grid)

    # Determine the output column for red pixels (one to the left).
    output_column = grey_column - 1

    # Handle edge case where grey_column is 0.
    if output_column < 0:
         output_column = 0


    # Place red pixels based on row indices relative to grey location.
    input_grid_np = np.array(input_grid)
    grey_rows = np.where(input_grid_np[:, grey_column] == 5)[0]

    # Place Red pixels in output grid relative to the grey object rows
    for i, grey_row in enumerate(grey_rows):
        output_row = grey_row

        if( 0 <= output_row < 3 and 0 <= output_column < 3) :
            output_grid[output_row, output_column] = 2


    return output_grid