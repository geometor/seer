# 1fad071e • 018 • refine_coder

---
```python
"""
The output grid is always a single row and 5 columns wide. For each of the *first five columns* of the input grid, examine the column. If the column contains a blue pixel (value 1) *anywhere* within the column, place a blue pixel (1) in the corresponding column of the output grid. Otherwise, place a white pixel (0) in that position of the output grid.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid to output grid based on presence of blue pixels in the first five columns."""
    grid = np.array(input_grid)
    num_cols = 5  # Output is always 5 columns wide
    output_grid = np.zeros((1, num_cols), dtype=int)

    # Iterate through the first five columns.
    for j in range(min(num_cols, grid.shape[1])):
        # Check if any cell in the column is blue.
        if np.any(grid[:, j] == 1):
            output_grid[0, j] = 1

    return output_grid.tolist()
```
