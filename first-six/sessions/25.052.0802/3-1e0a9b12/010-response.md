# 3-1e0a9b12 • 010 • example_3 - CODE

---
```python
"""
The transformation rule is as follows:
1. Iterate through each column of the input grid.
2. For each column, identify the non-white cells from bottom to top.
3. Starting from the last row and moving upwards, move these cells to the output grid
   maintaining their relative vertical order within the column.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving the non-white cells in each column
    to the bottom of the output grid, maintaining their original column and
    relative vertical order.
    """
    # Initialize the output grid as all zeros (white).
    output_grid = np.zeros_like(input_grid)

    # Iterate through each column of the input grid.
    for j in range(input_grid.shape[1]):
        # Collect non-white cells from the current column, from bottom to top.
        non_white_cells = []
        for i in reversed(range(input_grid.shape[0])):
            if input_grid[i, j] != 0:
                non_white_cells.append(input_grid[i, j])

        # Place the collected non-white cells in the output grid, starting from the last row.
        for i, color in enumerate(non_white_cells):
            output_grid[output_grid.shape[0] - 1 - i, j] = color

    return output_grid
```

