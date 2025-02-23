# AboveBelow1 • 010 • refine_coder

---
```python
"""
1.  **Preserve Top Rows:** Copy the first three rows (rows 0, 1, and 2) of the input grid directly to the output grid without changes.
2.  **Blanking Subsequent Rows:** For all rows below the top three (starting from row 3), change all pixel values to 0 (white).
3.  **Exception:** If a horizontal line exists below the first three rows, preserve the first horizontal line, changing all rows below this horizontal line to 0 (white).
"""

import numpy as np

def is_horizontal_line(grid, row):
    """Checks if a given row in the grid forms a horizontal line (all pixels have the same non-zero color)."""
    if row < 0 or row >= grid.shape[0]:
        return False
    first_color = grid[row, 0]
    if first_color == 0:  # Consider 0 as background, not a line
       return False
    for col in range(1, grid.shape[1]):
        if grid[row, col] != first_color:
            return False
    return True

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.zeros_like(input_grid)

    # 1. Preserve Top Rows
    for row in range(min(3, input_grid.shape[0])):
        output_grid[row, :] = input_grid[row, :]

    # 2 & 3. Blanking Subsequent Rows with Exception
    found_horizontal_line = False
    for row in range(3, input_grid.shape[0]):
        if not found_horizontal_line and is_horizontal_line(input_grid, row):
            output_grid[row, :] = input_grid[row, :]
            found_horizontal_line = True
        #else all 0, which is already set during initialization

    return output_grid
```
