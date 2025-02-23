# 6ecd11f4 • 002 • example_1 • investigate_coder

---
```python
"""
Extracts a specific 3x3 subgrid from the input grid, based on the location of a multi-colored region in the lower part of the grid.
"""

import numpy as np

def find_3x3_subgrid(input_grid):
    # Find the bounding box of non-zero and non-one pixels.
    rows, cols = input_grid.shape
    non_zero_one_indices = np.argwhere((input_grid != 0) & (input_grid !=1))

    if len(non_zero_one_indices) == 0:
        return None
    
    min_row = np.min(non_zero_one_indices[:, 0])
    max_row = np.max(non_zero_one_indices[:, 0])
    min_col = np.min(non_zero_one_indices[:, 1])
    max_col = np.max(non_zero_one_indices[:, 1])

    #Check if the region is 3x3.
    if max_row - min_row == 2 and max_col - min_col == 2:
       return (min_row, min_col)

    return None #no 3x3 region found

def transform(input_grid):
    """
    Transforms the input grid by extracting a 3x3 subgrid.
    """
    # Find the location of 3x3 subgrid.
    subgrid_start = find_3x3_subgrid(input_grid)

    # initialize output_grid as 3x3 of all 0
    output_grid = np.zeros((3, 3), dtype=int)

    if subgrid_start:
        # Extract the 3x3 subgrid.
        row_start, col_start = subgrid_start
        for i in range(3):
            for j in range(3):
                output_grid[i, j] = input_grid[row_start + i, col_start + j]

    return output_grid
```
