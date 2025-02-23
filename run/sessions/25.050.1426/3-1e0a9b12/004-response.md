# 3-1e0a9b12 • 004 • example_2 - CODE

---
```python
"""
The transformation is applied column by column. For each column, we identify the colored blocks (non-zero cells). The action is to "push down" these colored blocks to the bottom of the column, maintaining their original order from top to bottom within that column. Any empty spaces created at the top of the column after pushing the colored blocks down are filled with white (color 0). This effectively sorts the colors in each column by placing all white blocks (0) at the top and all colored blocks at the bottom, preserving the relative order of the colored blocks.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by pushing all non-zero values in each column to the bottom.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Iterate over each column
    for j in range(cols):
        # Extract non-zero values from the current column
        non_zero_values = input_grid[:, j][input_grid[:, j] != 0]
        # Calculate the starting row index for placing non-zero values
        start_row = rows - len(non_zero_values)
        # Place the non-zero values at the bottom of the output column
        output_grid[start_row:, j] = non_zero_values

    return output_grid.tolist()
```

