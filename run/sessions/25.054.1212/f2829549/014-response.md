# f2829549 • 014 • example_3 • investigate_coder

---
```python
"""
The transformation rule works as follows:

1.  **Identify Key Feature:** Locate the vertical blue (1) line in the input grid.
2.  **Reduce Columns:** Condense each set of columns into 1.
3.  **Determine New Value:**
      *   If an entire column in original is white, it maps to white (0).
      *   If a column to left of blue contains orange or to right contains grey, then it maps green.
"""

import numpy as np

def find_vertical_line(grid, color):
    """Finds the column index of a full-height vertical line of the specified color."""
    rows, cols = grid.shape
    for j in range(cols):
        if all(grid[i, j] == color for i in range(rows)):
            return j
    return -1  # Return -1 if no such line is found

def transform(input_grid):
    """Transforms the input grid according to the described rules."""
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, 3), dtype=int)
    blue_line_col = find_vertical_line(input_grid, 1)

    # Iterate through input columns in groups
    col_groups = [(0, 1, 2), (blue_line_col,), (5, 6)] # split in the groups
    
    for i, group in enumerate(col_groups) :
        for row in range(rows) :
            if i == 1 : # blue
                output_grid[row, 1] = 0 # all white
            else:
                is_all_white = True
                for col in group :
                    if input_grid[row, col] != 0:
                        is_all_white = False
                        break
                if is_all_white:
                    output_grid[row, i] = 0
                else:
                     output_grid[row,i] = 3

    return output_grid
```
