# ea786f4a • 008 • example_2 • investigate_coder

---
```python
"""
Transforms a grid by inverting a frame of pixels around a central pixel, 
keeping the central pixel unchanged, and extending any white
pixels into full-row and full-column crosses.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Place a white frame in output
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows - 1:
                output_grid[i,j] = 0
            if j == 0 or j == cols - 1:
                output_grid[i,j] = 0
                

    return output_grid
```
