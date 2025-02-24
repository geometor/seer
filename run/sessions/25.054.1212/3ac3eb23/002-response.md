# 3ac3eb23 • 002 • example_1 • investigate_coder

---
```python
"""
Copies the input grid and adds vertically-offset pixels below colored pixels on odd rows.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Copy all pixels (including background)
    output_grid[:] = input_grid[:]

    # Iterate through the grid and apply the transformation rule
    for row in range(rows):
        for col in range(cols):
            # Check for the target colors and odd row
            if input_grid[row, col] != 0 and (row % 2 == 0):
                if row + 1 < rows:  # ensure offset within output grid boundaries
                    output_grid[row + 1, col] = input_grid[row, col]

    return output_grid
```
