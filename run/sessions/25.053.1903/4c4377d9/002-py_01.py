"""
The input grid's rows are duplicated and rearranged. The first row is duplicated at the bottom. Row 2 is duplicated above row 2. And finally Row 3 is duplicated above row 3.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with double the number of rows
    input_rows, input_cols = input_grid.shape
    output_grid = np.zeros((2 * input_rows, input_cols), dtype=int)

    # Duplicate and shift first row to the end
    output_grid[:input_rows-1, :] = input_grid[1:, :]
    output_grid[input_rows-1,:] = input_grid[0,:]

    # Add first row at the bottom
    output_grid[input_rows, :] = input_grid[0, :]
    #Duplicate second row
    output_grid[input_rows+1, :] = input_grid[1, :]

    #Duplicate and shift the other rows
    output_grid[input_rows+2:,:] = input_grid[1:,:]

    return output_grid