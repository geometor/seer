# 1e0a9b12 • 005 • refine_coder

---
```python
"""
Transforms the input grid by compacting non-zero pixels downwards within their respective columns.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid by moving non-zero elements down within their columns."""
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Iterate through each column
    for c in range(cols):
        # Collect non-zero pixels from the current column
        non_zero_pixels = []
        for r in range(rows):
            if input_grid[r, c] != 0:
                non_zero_pixels.append(input_grid[r, c])

        # Place non-zero pixels in the output grid, starting from the bottom
        for i, value in enumerate(non_zero_pixels):
            output_grid[rows - len(non_zero_pixels) + i, c] = value

    return output_grid
```
