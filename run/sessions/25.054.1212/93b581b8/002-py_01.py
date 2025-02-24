"""
1.  **Identify the Central Block:** Locate the 2x2 block of non-zero pixels in the center of the input grid.
2.  **Top Extension**: Copy/mirror pixels `[2,1]` and `[2,0]` and `[3,1]` and `[3,0]`(using 0-indexed based row and column) of the input to the top two rows of the entire grid
3. **Bottom Extension**: Copy pixels `[3,1]` and `[3,0]` and `[2,1]` and `[2,0]` to the bottom two rows of the grid.
4.  **Preserve Center:** The original 2x2 central block remains unchanged in its original position.
"""

import numpy as np

def find_central_block(grid):
    # Find the bounding box of non-zero elements
    rows, cols = np.where(grid != 0)
    if len(rows) == 0:  # Handle empty grid case
        return None
    min_row, max_row = np.min(rows), np.max(rows)
    min_col, max_col = np.min(cols), np.max(cols)

    # Check if it's a 2x2 block
    if max_row - min_row == 1 and max_col - min_col == 1:
        return (min_row, min_col, max_row, max_col)
    else:
        return None

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find the central 2x2 block
    central_block_coords = find_central_block(input_grid)
    if central_block_coords is None:
        return output_grid # Return original grid if central block not present

    min_row, min_col, max_row, max_col = central_block_coords


    # Top Extension:
    output_grid[0:2, 0:2] = input_grid[max_row,max_col] # azure
    output_grid[0:2, cols-2:cols] = input_grid[max_row,min_col] # orange

    # Bottom Extension:
    output_grid[rows-2:rows, 0:2] = input_grid[min_row, max_col] # green
    output_grid[rows-2:rows, cols-2:cols] = input_grid[min_row,min_col] # maroon

    return output_grid