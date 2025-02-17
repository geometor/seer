# 6-0520fde7 • 002 • Response

---

*text:*

```python
"""
The transformation extracts a 3x3 subgrid centered around the gray cells, counts related blue cells, and sets the central pixel of the output to red, leaving the rest as background (white).
"""

import numpy as np

def find_gray_column(grid):
    # Find the column index containing gray cells (value 5).
    for j in range(grid.shape[1]):
        if np.any(grid[:, j] == 5):
            return j
    return -1

def count_blue_cells(grid, row, gray_column):
    # Count blue cells (value 1) to the left and right of the gray column in the given row.
    left_count = 0
    for j in range(gray_column):
        if grid[row, j] == 1:
            left_count += 1

    right_count = 0;
    for j in range(gray_column + 1, grid.shape[1]):
        if grid[row, j] == 1:
            right_count += 1
    return left_count, right_count
            

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    input_grid = np.array(input_grid)
    gray_column = find_gray_column(input_grid)
    
    # Initialize the output grid as 3x3 with all zeros.
    output_grid = np.zeros((3, 3), dtype=int)

    if gray_column != -1:
      # compute blue cells around gray cells
      blue_left_top, blue_right_top = count_blue_cells(input_grid, 0, gray_column)
      blue_left_mid, blue_right_mid = count_blue_cells(input_grid, 1, gray_column)
      blue_left_bot, blue_right_bot = count_blue_cells(input_grid, 2, gray_column)

      # determine central pixel color
      if (blue_right_top + blue_right_mid + blue_right_bot) > (blue_left_top + blue_left_mid + blue_left_bot):
        output_grid[1,1] = 2

    return output_grid
```
