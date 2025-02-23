# 1b2d62fb • 020 • example_4 • investigate_coder

---
```python
"""
Extracts the central blue stripe from the input, maps the blue color (1) to azure (8), and represents it within a 3-column wide grid, with the rest of the pixels as white(0).
"""

import numpy as np

def find_central_stripe_column(grid):
    # Iterate through columns to find the one with all blue (1) pixels.
    height = len(grid)
    for j in range(len(grid[0])):
        is_stripe = True
        for i in range(height):
            if grid[i][j] != 1:
                is_stripe = False
                break
        if is_stripe:
            return j
    return -1  # Return -1 if no stripe is found


def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    height = input_grid.shape[0]
    width = 3
    output_grid = np.zeros((height, width), dtype=int)

    # Find central stripe
    stripe_col = find_central_stripe_column(input_grid)

    # change output pixels, mapping 1 to 8
    if stripe_col != -1:
      for i in range(height):
        output_grid[i, 1] = 8


    return output_grid
```
