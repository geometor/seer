# 3-1e0a9b12 • 006 • example_3 - CODE

---
```python
"""
1. For each column in the input grid:
2. Collect all non-zero values within that column, maintaining their original top-to-bottom order.
3. In the same column of the output grid, place these collected values starting from the top-most row and stacking them downwards, filling only previously empty cells.
4. Leave columns that were entirely zeros in the input grid unchanged (all zeros) in the output grid.
5. Any remaining unfilled cells in the output grid remain or become zeros.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the column-wise stacking rule."""

    output_grid = np.zeros_like(input_grid)
    rows, cols = output_grid.shape

    for j in range(cols):  # Iterate through columns
        column_values = []
        for i in range(rows):
            if input_grid[i, j] != 0:
                column_values.append(input_grid[i, j])

        # Place values in the same column, stacking downwards
        row_idx = 0
        for val in column_values:
            while row_idx < rows and output_grid[row_idx, j] != 0:
              row_idx+=1
            if (row_idx < rows):
              output_grid[row_idx, j] = val
            row_idx += 1

    return output_grid
```

