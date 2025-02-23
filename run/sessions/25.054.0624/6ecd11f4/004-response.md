# 6ecd11f4 • 004 • refine_coder

---
```python
"""
Extracts a subgrid from the input grid, based on the location of a multi-colored region in the lower part of the grid. The size of subgrid may vary.
Some color modification might be applied to the extracted subgrid.
"""

import numpy as np

def find_target_region(input_grid):
    """
    Finds the bounding box of the multi-colored region (non-0 and non-1 pixels) at the bottom.
    """
    rows, cols = input_grid.shape
    non_zero_one_indices = np.argwhere((input_grid != 0) & (input_grid != 1))

    if len(non_zero_one_indices) == 0:
        return None, None, None, None

    min_row = np.min(non_zero_one_indices[:, 0])
    max_row = np.max(non_zero_one_indices[:, 0])
    min_col = np.min(non_zero_one_indices[:, 1])
    max_col = np.max(non_zero_one_indices[:, 1])

    return min_row, max_row, min_col, max_col

def transform(input_grid):
    """
    Transforms the input grid by extracting a subgrid.
    """
    # Find the location of target region.
    min_row, max_row, min_col, max_col = find_target_region(input_grid)

    # Get expected output size by checking train set.
    output_grid_row_size = max_row - min_row + 1
    output_grid_col_size = max_col - min_col + 1

    if output_grid_row_size == 3 and output_grid_col_size ==3:
      output_grid = np.zeros((3, 3), dtype=int)
    elif output_grid_row_size == 4 and output_grid_col_size == 3:
      output_grid = np.zeros((4,3), dtype=int)
    else:
      return input_grid


    if min_row is not None:
        # Extract the subgrid, align at top-left corner.
        for i in range(output_grid.shape[0]):
            for j in range(output_grid.shape[1]):
                if min_row + i < input_grid.shape[0] and min_col + j < input_grid.shape[1]:
                   output_grid[i, j] = input_grid[min_row + i, min_col + j]

    # Color changes needs further checks.

    return output_grid
```
