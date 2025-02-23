# 3-1e0a9b12 • 004 • refine_coder

---
```python
"""
The transformation involves a column-wise stacking of non-zero pixels to the bottom of the grid, preserving the relative vertical order of the elements within each column.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by stacking non-zero pixels to the bottom of each column.
    """
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = np.zeros_like(input_grid)

    # Iterate through each column
    for c in range(cols):
        # Collect non-zero pixels from the current column
        non_zero_pixels = []
        for r in range(rows):
            if input_grid[r][c] != 0:
                non_zero_pixels.append(input_grid[r][c])

        # Stack non-zero pixels at the bottom of the column in the output grid
        for i, pixel_value in enumerate(non_zero_pixels):
            output_grid[rows - len(non_zero_pixels) + i][c] = pixel_value

    return output_grid
```
