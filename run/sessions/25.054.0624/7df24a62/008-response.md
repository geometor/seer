# 7df24a62 • 008 • example_2 • investigate_coder

---
```python
"""
Preserves the yellow pixels and adds a mirrored blue square on the opposite vertical side of the grid.
"""

import numpy as np

def find_blue_square(grid):
    # Find the blue square in the grid
    rows, cols = grid.shape
    for r in range(rows - 3):
        for c in range(cols - 3):
            if np.all(grid[r:r+4, c:c+4] == 1):
                return (r, c)
    return None

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find the blue square
    blue_square_start = find_blue_square(input_grid)

    if blue_square_start:
      # Find the number of rows to the vertical center of the grid.
      blue_square_row, _ = blue_square_start
      rows_to_center = (rows - (blue_square_row + 4))
      new_blue_row_start = rows - rows_to_center - 4

    # reflect blue square, adding to empty rows
    if blue_square_start is not None:
        blue_square_row, blue_square_col = blue_square_start
        output_grid[new_blue_row_start:new_blue_row_start+4, blue_square_col:blue_square_col+4] = 1

    return output_grid
```
