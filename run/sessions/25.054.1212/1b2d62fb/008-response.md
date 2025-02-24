# 1b2d62fb • 008 • example_2 • investigate_coder

---
```python
"""
Transforms an input grid by extracting three columns centered around a blue (color 1) stripe, 
and mapping the blue color to azure (color 8).
"""

import numpy as np

def find_blue_stripe_column(grid):
    """Finds the column index of the vertical blue stripe (color 1)."""
    for j in range(grid.shape[1]):
        if np.any(grid[:, j] == 1):
            return j
    return -1  # Return -1 if no blue stripe is found


def transform(input_grid):
    """Transforms the input grid according to the rule."""
    rows = input_grid.shape[0]
    cols = 3
    output_grid = np.zeros((rows, cols), dtype=int)

    # Find the blue stripe column
    blue_stripe_col = find_blue_stripe_column(input_grid)

    if blue_stripe_col == -1:
        return output_grid # all 0 if no blue strip

    center_col_index = blue_stripe_col // 2

    # Populate the output grid
    # First Column with 0
    # output_grid[:, 0] = 0  # Already initialized to 0

    # Middle and Third column: azure where blue was, 0 otherwise
    if(center_col_index >= 0 and center_col_index < input_grid.shape[1]):
        for i in range(rows):
            if input_grid[i, blue_stripe_col] == 1:
                output_grid[i, 1] = 8
                output_grid[i, 2] = 8

    return output_grid
```
