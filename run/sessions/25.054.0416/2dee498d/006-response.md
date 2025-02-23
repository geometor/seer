# 2dee498d • 006 • refine_coder

---
```python
"""
The transformation extracts a sub-grid from the input grid. The output grid has the same number of rows as the input grid. The number of columns is input_columns // 2.
The output grid consists of every other column of the input grid, starting with column 0 and up to the calculated output grid's width.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts a sub-grid by selecting every other column from the input grid, starting from column 0.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_cols = cols // 2
    output_grid = np.zeros((rows, output_cols), dtype=int)

    # Iterate through the input grid and select every other column, up to the new width.
    for i in range(rows):
        for j in range(output_cols):
            output_grid[i, j] = input_grid[i, j * 2]

    return output_grid.tolist()
```
