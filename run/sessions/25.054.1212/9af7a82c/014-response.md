# 9af7a82c • 014 • example_3 • investigate_coder

---
```python
"""
The transformation involves finding the positions of colors '3','8','4' and '2' in the input, preserving those, reordering the '4' and'2' columns, and setting cells to zero (white) below maintained elements.
"""

import numpy as np

def get_column(grid, col_index):
    return grid[:, col_index]

def set_column(grid, col_index, col_values):
    grid[:, col_index] = col_values

def find_first_instance_in_column(column, value):
     for i, val in enumerate(column):
        if val == value:
           return i
     return -1

def transform(input_grid):
    # initialize output_grid
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols), dtype=int)

    #find relevant columns
    col_3 = -1
    col_8 = -1
    col_4 = -1
    col_2 = -1

    for i in range(cols):
      col = get_column(input_grid, i)
      if find_first_instance_in_column(col, 3) != -1:
        col_3 = i
      if find_first_instance_in_column(col, 8) != -1:
        col_8 = i
      if find_first_instance_in_column(col, 4) != -1:
        col_4 = i
      if find_first_instance_in_column(col, 2) != -1:
        col_2 = i

    # copy and reorder the found columns to their new spot
    if (col_3 != -1):
       set_column(output_grid, 0, get_column(input_grid, col_3))
    if (col_8 != -1):
       set_column(output_grid, 1, get_column(input_grid, col_8))
    if (col_4 != -1):
       set_column(output_grid, 2, get_column(input_grid, col_4))
    if (col_2 != -1):
      set_column(output_grid, 3, get_column(input_grid, col_2))
    

    # zero out below maintained elements
    for c in range(cols):
        first_non_zero = -1
        for r in range(rows):
          if output_grid[r][c] != 0:
             first_non_zero = r
             break
        if first_non_zero != -1:
          for r in range(first_non_zero + 1, rows):
             output_grid[r][c] = 0

    return output_grid
```
