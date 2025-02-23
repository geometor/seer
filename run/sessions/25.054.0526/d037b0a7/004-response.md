# d037b0a7 • 004 • refine_coder

---
```python
"""
1.  **Identify Key Pixels:** Locate all non-zero pixels in the input grid.
2. **Vertical Propagation**: For each non-zero pixel, copy its value downwards to all cells directly below it in the same column, within the bounds of the grid.
3. **Preserve 0's**: Leave the 0 valued pixels unchanged.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the vertical fill-down rule."""
    output_grid = np.copy(input_grid)  # Initialize output grid as a copy
    rows, cols = input_grid.shape

    # Iterate through each column.
    for j in range(cols):
        # Iterate through each row in the current column.
        for i in range(rows):
            # Check if the current pixel is non-zero.
            if input_grid[i, j] != 0:
                # Propagate the non-zero value downwards.
                for k in range(i + 1, rows):
                    output_grid[k, j] = input_grid[i, j]

    return output_grid
```

