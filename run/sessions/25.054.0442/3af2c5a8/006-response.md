# 3af2c5a8 • 006 • refine_coder

---
```python
"""
1.  **Double Rows:** Duplicate each row of the input grid, creating two identical rows in the output grid for each original row.
2.  **Double and Fill Columns:** For each column (index `n`) in the input grid:
    *   Create a new column in the output grid at index `2n`, filling it with the values from input column `n`.
    *   Create another new column in the output grid at index `2n + 1`, also filling it with the values from input column `n`.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows * 2, cols * 2), dtype=int)

    # Double Rows:
    for i in range(rows):
        output_grid[i*2, :] = input_grid[i, :]      # copy row i to 2i
        output_grid[i*2+1, :] = input_grid[i, :]    # copy row i to 2i+1
    
    # Double, and fill Columns:
    for j in range(cols):
        output_grid[:,j*2] = output_grid[:,j*2]      # input col j to output col 2j
        output_grid[:,j*2+1] = output_grid[:, j*2]  #   also to 2j + 1
       

    return output_grid.tolist()
```
