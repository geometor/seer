"""
1.  **Identify the Yellow Region:** Find the contiguous region of yellow (4) pixels and determine its bounding box. This region remains unchanged in the output.

2.  **Process Columns Individually:** For each column in the grid, do the following:

    * If any existing azure pixels exist to the right of the right most yellow pixel, fill entire column with azure pixels.
    * If the column is to the left of the left most yellow pixel, and no existing azure exists to the right of yellow, fill entire column with azure.
    *   Otherwise, the column remains unchanged.

3. Preserve the yellow region.
"""

import numpy as np

def find_yellow_region(grid):
    """Finds the bounding box of the connected yellow region."""
    rows, cols = grid.shape
    min_row, max_row = rows, -1
    min_col, max_col = cols, -1

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 4:
                min_row = min(min_row, r)
                max_row = max(max_row, r)
                min_col = min(min_col, c)
                max_col = max(max_col, c)

    return min_row, max_row, min_col, max_col

def transform(input_grid):
    # initialize output_grid
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols), dtype=int)

    # 1. Identify and preserve the yellow region.
    min_yellow_row, max_yellow_row, min_yellow_col, max_yellow_col = find_yellow_region(input_grid)

    for r in range(rows):
        for c in range(cols):
            if input_grid[r,c] == 4:
                output_grid[r,c] = 4


    # 2. Process Columns Individually
    for c in range(cols):
        # Check for azure to the right of yellow
        azure_right = False
        for r in range(rows):
            for col_check in range(max_yellow_col + 1, cols):
                if input_grid[r,col_check] == 8:
                    azure_right = True
                    break
            if azure_right:
                break

        # Fill based on the conditions
        if azure_right and c > max_yellow_col:
              for r in range(rows):
                  output_grid[r,c] = 8
        elif not azure_right and c < min_yellow_col :
            for r in range(rows):
                output_grid[r,c] = 8
        elif input_grid[r,c] != 4: #Preserve yellow, otherwise don't change
            output_grid[r,c] = input_grid[r,c] # Transfer the original pixel
        

    return output_grid