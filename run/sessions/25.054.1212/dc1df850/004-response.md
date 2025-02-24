# dc1df850 • 004 • refine_coder

---
```python
"""
1.  **Identify Starting Points:** Locate all red pixels (value 2) in the grid.
2.  **Propagate Blue:** For each red pixel, change the color of connected white pixels (value 0) to its right and below it to blue (value 1). The change stops when a non-white pixel is encountered in either direction.
3.  **Preservation:** All other color pixels stay.
"""

import numpy as np

def flood_fill(grid, x, y):
    """
    Performs a flood fill operation, changing connected white pixels (0) to blue (1)
    to the right and below the starting point (x, y). Stops when hitting non-white pixels.
    """
    if x < 0 or x >= grid.shape[1] or y < 0 or y >= grid.shape[0] or grid[y, x] != 0:
        return

    grid[y, x] = 1
    flood_fill(grid, x + 1, y)  # Right
    flood_fill(grid, x, y + 1)  # Down

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    output_grid = np.copy(input_grid)

    # Iterate through all pixels in the grid
    for y in range(output_grid.shape[0]):
        for x in range(output_grid.shape[1]):
            # If a red pixel is found, initiate flood fill
            if output_grid[y, x] == 2:
                flood_fill(output_grid, x, y)

    return output_grid
```
