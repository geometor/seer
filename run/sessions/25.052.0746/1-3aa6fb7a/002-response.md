# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
The transformation rule is as follows:
1. Identify two azure (8) colored "L" shaped objects (2x2 blocks with one cell removed). One is positioned at the top-left and the other at the bottom-right of the grid.
2. Change the color of the cell immediately to the right of the top-left object to blue (1).
3. Change the color of the cell immediately to the left of the bottom-right object to blue (1).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through the grid to find the objects and apply transformations
    for r in range(rows):
        for c in range(cols):
            # Check for the top-left L-shape object (right-most cell)
            if (
                output_grid[r, c] == 8 and
                r + 1 < rows and
                c + 1 < cols and
                output_grid[r + 1, c] == 8 and
                output_grid[r + 1, c + 1] == 8
            ):
                if c + 2 < cols: # Boundary
                  output_grid[r, c + 1] = 1

            # Check for the bottom-right L-shape object (left-most cell)
            if (
                output_grid[r, c] == 8 and
                r - 1 >= 0 and
                c - 1 >= 0 and
                output_grid[r - 1, c] == 8 and
                output_grid[r - 1, c - 1] == 8
            ):
                if c-2 >=0:
                    output_grid[r, c - 1] = 1

    return output_grid
```
