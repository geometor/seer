# 0a938d79 • 012 • refine_coder

---
```python
"""
Examine each row of the input grid. If a row contains a single, isolated non-zero colored pixel (surrounded by zeros), fill the entire row with that pixel's color.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid based on the presence of single non-zero pixels in each row.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    for i in range(rows):
        row = output_grid[i]
        non_zero_pixels = row[row != 0]

        if len(non_zero_pixels) == 1:
            # Fill the entire row with the single non-zero color
            output_grid[i, :] = non_zero_pixels[0]

    return output_grid
```

