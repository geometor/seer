"""
1. Collect Blues: Scan the entire input grid. Whenever you find a blue pixel (value 1), remember its column number. Keep these column numbers in the order you found them.
2. Create Output: Make a new, empty grid (all zeros) that is the same size as the input grid.
3. Place Reds: In the first row of this new grid, place red pixels (value 2) in the column positions you recorded in step 1.
4. Fill with Zeros: The rest of the output grid should be filled with 0.
"""

import numpy as np

def collect_blue_columns(grid):
    # helper to store the column indices of blue pixels
    blue_columns = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 1:
                blue_columns.append(j)
    return blue_columns

def transform(input_grid):
    # initialize output_grid as a copy of input filled with zeros
    output_grid = np.zeros_like(input_grid)

    # Collect column indices of blue pixels
    blue_columns = collect_blue_columns(input_grid)

    # Place red pixels (2) in the first row based on collected column indices
    for col_index, col in enumerate(blue_columns):
        output_grid[0, col] = 2

    return output_grid