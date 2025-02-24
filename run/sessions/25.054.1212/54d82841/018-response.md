# 54d82841 • 018 • refine_coder

---
```python
"""
The output grid is the input grid with a new row added to the bottom. The values in the new row are determined by the values in the third row from the bottom of the input grid. If a cell in the third row from the bottom of the input is non-zero, a '4' is placed in the corresponding column of the new row. Only one '4' is placed in the output row for each distinct non-zero color in the third to last input row. If a cell in the third-to-last row of the input is '0', a '0' is placed in the corresponding column of the new row.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid: create a copy, add one new row initialized to 0
    output_grid = np.copy(input_grid)
    new_row = np.zeros(input_grid.shape[1], dtype=int)
    output_grid = np.vstack([output_grid, new_row])

    # change output pixels: iterate through the third-to-last row of the input
    rows, cols = input_grid.shape
    target_row = rows - 3  # Third row from the bottom of the *input*
    distinct_values = set() # Keep track of distinct non-zero values

    for j in range(cols):
        target_value = input_grid[target_row, j]

        if target_value == 0:
            output_grid[-1, j] = 0  # Set to 0 if target is 0.  -1 index is last row
        elif target_value not in distinct_values:
            output_grid[-1, j] = 4  # Set to 4 if distinct non-zero
            distinct_values.add(target_value)

    return output_grid
```
