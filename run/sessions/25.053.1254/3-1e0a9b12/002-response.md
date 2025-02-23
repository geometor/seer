# 3-1e0a9b12 • 002 • example_1 - CODE

---
```python
"""
The transformation moves all non-zero pixels to the last row of the output grid, preserving their original order from top to bottom, left to right, and fills the rest of the grid with zeros.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-zero pixels to the last row,
    preserving their order, and filling the rest with zeros.
    """
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = np.zeros_like(input_grid)

    # 1. Identify and Order Non-Zero Pixels
    non_zero_pixels = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] != 0:
                non_zero_pixels.append(input_grid[r][c])

    # 2. Fill last row with Non-Zero Pixels
    last_row_index = rows - 1
    for i in range(len(non_zero_pixels)):
        if i < cols:
          output_grid[last_row_index][i] = non_zero_pixels[i]

    return output_grid
```
