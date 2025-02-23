# 9af7a82c • 024 • refine_coder

---
```python
"""
Transforms an input grid into an output grid by:
1. Reversing the order of columns.
2. Duplicating rows from the reversed grid, but setting the first element of each to zero.
3. Adding new rows and populating with zero.
"""

import numpy as np

def transform(input_grid):
    # Reverse the columns
    reversed_grid = input_grid[:, ::-1]
    input_rows, input_cols = input_grid.shape
    output_rows = input_rows + (input_rows - 1)
    output_cols = input_cols
    output_grid = np.zeros((output_rows, output_cols), dtype=int)

    # Duplicate n-1 rows, modifying the first element
    for i in range(input_rows -1):
        output_grid[i, 1:] = reversed_grid[i, 1:]
        output_grid[i,0] = reversed_grid[i,0]


    #Add rows
    for i in range(input_rows - 1):
        output_grid[input_rows + i, 0] = reversed_grid[0,0] #first element of first new row
        #remaining are zero.

    return output_grid
```
