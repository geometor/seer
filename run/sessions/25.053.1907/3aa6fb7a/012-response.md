# 3aa6fb7a • 012 • refine_coder

---
```python
"""
Iterates through each pixel of the input grid. If a pixel is azure (8), it checks
if it could be the top-left corner of a 2x2 azure square. If it can, the pixel's
color is changed to blue (1). The modified grid is then returned.
"""

import numpy as np

def is_potential_top_left(grid, row, col):
    """Checks if a pixel *could* be the top-left of a 2x2 azure square."""
    rows, cols = grid.shape
    if grid[row,col] != 8:
        return False    
    # Check if within grid bounds for a 2x2 square. Don't check color value.
    if row + 1 < rows and col + 1 < cols:
        return True
    return False

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each pixel in the grid
    for row in range(rows):
        for col in range(cols):
            # Check if the pixel is azure and a potential top-left
            if is_potential_top_left(output_grid, row, col):
                # Change the pixel's color to blue (1)
                output_grid[row, col] = 1

    return output_grid
```
