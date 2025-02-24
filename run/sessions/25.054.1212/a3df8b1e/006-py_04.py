"""
Creates a checkerboard pattern that shifts based on the location of '1' in the input grid.
The '1' determines the starting row and column of the checkerboard, with a column inversion.
"""

import numpy as np

def find_trigger(input_grid):
    # Find the location of the '1' in the input grid.
    rows, cols = input_grid.shape
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 1:
                return r, c
    return 0, 0  # Default to (0, 0) if no '1' is found


def transform(input_grid):
    # Initialize output_grid with the same dimensions as the input
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols), dtype=int)

    # Find the trigger (location of '1')
    trigger_row, trigger_col = find_trigger(input_grid)

    # Create the shifted checkerboard pattern
    for r in range(rows):
        for c in range(cols):
            # Determine the effective row and column relative to the trigger
            eff_row = (r - trigger_row) % rows
            eff_col = (c - trigger_col) % cols
            
            # Basic checkerboard pattern based on effective row
            if (eff_row + eff_col) % 2 == 0:
              val = 0
            else:
              val = 1

            # column inversion.  
            if c < trigger_col:
                output_grid[r,c] = 1 - val
            else:
                output_grid[r,c] = val


    return output_grid