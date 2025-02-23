# 2dee498d • 004 • refine_coder

---
```python
"""
The transformation extracts a sub-grid from the input grid. The output grid has the same number of rows as the input grid.
The number of columns in the output grid is (input_columns + 1) // 2.
The output grid consists of every other column of the input, starting from column 0.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts a sub-grid by selecting every other column from the input grid, starting from column 0.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_cols = (cols + 1) // 2
    output_grid = np.zeros((rows, output_cols), dtype=int)

    # Iterate through the input grid and select every other column.
    for i in range(rows):
        for j in range(0, cols, 2):
            output_col_index = j // 2
            if output_col_index < output_cols:
              output_grid[i, output_col_index] = input_grid[i, j]

    return output_grid.tolist()
```
