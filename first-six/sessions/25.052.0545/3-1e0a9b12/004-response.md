# 3-1e0a9b12 • 004 • refine_code - CODE

---
```python
"""
Transforms the input grid by moving non-zero colored cells down within their columns
to occupy the lowest available rows, and filling the rest with zeros.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving non-zero colored cells down within their columns
    to occupy the lowest available rows, and filling the rest with zeros.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    for j in range(cols):
        # Collect non-zero elements from the column
        non_zero_elements = [input_grid[i, j] for i in range(rows) if input_grid[i, j] != 0]

        # Fill the column from the bottom up
        for i, val in enumerate(non_zero_elements):
            output_grid[rows - len(non_zero_elements) + i, j] = val

    return output_grid
```

