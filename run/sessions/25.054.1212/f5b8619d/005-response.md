# f5b8619d • 005 • refine_coder

---
```python
"""
1.  **Expansion:** The output grid is created by expanding the input grid. The number of rows in the output is double the number of rows in the input. The number of columns in the output is double the number of columns in the input, *plus* the number of unique non-zero colors in the input
2.  **Color Alternation:** For each cell in the input, two cells are created in the output. The first cell created has the same color. The next adjacent cell is 'azure' (color 8).
3. **New Columns:** create a new column after each original input column, fill the new column with 'azure' (color 8)
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    unique_non_zero_colors = len(np.unique(input_grid[input_grid != 0]))
    new_cols = 2 * cols + unique_non_zero_colors
    new_rows = 2 * rows
    output_grid = np.zeros((new_rows, new_cols), dtype=int)

    # Expand and alternate colors
    for i in range(rows):
        for j in range(cols):
            output_grid[2*i, 2*j] = input_grid[i, j]
            output_grid[2*i, 2*j+1] = 8
            output_grid[2*i+1, 2*j] = 8 # fill row below with 8
            output_grid[2*i+1, 2*j+1] = 8

    # insert extra columns of 8 after processing original grid
    for k in range(unique_non_zero_colors):
      output_grid[:,(2*cols + k)] = 8

    return output_grid
```
