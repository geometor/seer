# 7b7f7511 • 006 • refine_coder

---
```python
"""
The transformation rule extracts the top-left quadrant of the input grid to create the output grid. The output grid's dimensions are determined by halving the corresponding input dimensions and rounding up to the nearest integer (taking the ceiling). Specifically, the new height is the ceiling of the original height divided by two, and the new width is the ceiling of the original width divided by two. The pixels within these calculated bounds, starting from the top-left corner (0,0) of the input grid, are copied to form the output grid.
"""

import numpy as np
import math

def transform(input_grid):
    # Get input grid dimensions
    height = len(input_grid)
    width = len(input_grid[0])

    # Calculate new dimensions (half of original, rounded up)
    new_height = math.ceil(height / 2)
    new_width = math.ceil(width / 2)

    # Initialize output grid with correct dimensions, filled by zeros to begin
    output_grid = np.zeros((new_height, new_width), dtype=int)
    
    # Copy the relevant portion (top-left quadrant) of the input grid to the output grid
    for i in range(new_height):
        for j in range(new_width):
            output_grid[i][j] = input_grid[i][j]

    return output_grid
```
