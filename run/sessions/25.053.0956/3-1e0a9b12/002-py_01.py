"""
Extracts non-zero values from the input grid, shifts them down by one row,
shifts right by 1 column, and places them on the bottom row of the output grid. All
other cells in the output grid are set to 0.
"""

import numpy as np

def get_nonzero_cells(grid):
    """Finds non-zero cells and their original positions."""
    nonzero_cells = []
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] != 0:
                nonzero_cells.append(((r, c), grid[r, c]))
    return nonzero_cells

def shift_position(pos, rows, cols):
    """Shifts a position down by one row and right by one column, wrapping around."""
    r, c = pos
    new_r = (r + 1) % rows
    new_c = (c + 1) % cols
    return (new_r, new_c)

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Find non-zero cells in input and their positions
    nonzero_cells = get_nonzero_cells(input_grid)

    # shift positions down by 1, right by 1
    shifted_cells = []
    for pos, val in nonzero_cells:
      shifted_cells.append( (shift_position(pos, rows, cols), val ))
      
    # apply shift
    for pos, val in shifted_cells:
        output_grid[pos] = val

    # Zero out all rows except the last row
    for r in range(rows - 1):
        for c in range(cols):
            output_grid[r, c] = 0
            
    # apply values to the bottom row
    original_values = [val for _, val in nonzero_cells]
    
    # place the values in their original order on the bottom row
    last_row_index = 0
    for val in original_values:
      output_grid[rows - 1, last_row_index] = val
      last_row_index += 1

    return output_grid