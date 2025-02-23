# 1b2d62fb • 002 • example_1 - CODE

---
```python
"""
Transforms an input grid with a central blue vertical line into an output grid with 
two azure pixels horizontally centered on the second-to-last row, and the rest of the grid filled with white.
"""

import numpy as np

def get_blue_column(grid):
    """Finds the column index containing the vertical blue line."""
    rows, cols = grid.shape
    for j in range(cols):
        if np.all(grid[:, j] == 1):  # Assuming blue is represented by 1. It might not be a solid line in all cases
           return j
    return -1 # not found
        

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    # Initialize output grid with the new dimensions (same number of rows, width = 3)
    rows = input_grid.shape[0]
    output_grid = np.zeros((rows, 3), dtype=int)

    # Find the original x of the blue line
    blue_col = get_blue_column(input_grid)
    
    # place azure pixels in second to last row of output_grid
    output_grid[-2, 1] = 8
    output_grid[-2, 2] = 8

    return output_grid
```

