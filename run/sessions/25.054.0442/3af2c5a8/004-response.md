# 3af2c5a8 • 004 • refine_coder

---
```python
"""
1.  **Double Rows:** Duplicate each row of the input grid.
2.  **Double and Fill Columns:** For each column in the original grid (index `n`):
    - Create a new column in the output grid at index `2n`, filling it with the values of column `n`.
    - Create a new column in the output grid at index `2n + 1`, filling it with the values of column `n`.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows * 2, cols * 2), dtype=int)

    # Double Rows
    for i in range(rows):
        output_grid[i*2, 0:cols] = input_grid[i, :]
        output_grid[i*2+1, 0:cols] = input_grid[i, :]
    
    # Double, and fill Columns:
    for j in range(cols):
      for i in range(rows * 2):
        output_grid[i,j*2] = input_grid[i//2,j]
        output_grid[i, j*2 + 1] = input_grid[i//2, j]

    return output_grid.tolist()
```

