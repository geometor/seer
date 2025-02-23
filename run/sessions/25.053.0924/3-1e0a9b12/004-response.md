# 3-1e0a9b12 • 004 • example_2 - CODE

---
```python
"""
Moves the maroon (9) pixel from the top-right corner to the bottom-right corner.
Leaves the yellow (4) vertical line unchanged.
The azure (8) pixel stays on the 5th row and combines with orange.
"""

import numpy as np

def find_object(grid, color):
    # Find the coordinates of a single-pixel object of the specified color.
    coords = np.argwhere(grid == color)
    if len(coords) > 0:
        return coords.tolist()
    return []

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    grid_size = input_grid.shape

    # Find the maroon (9) pixel
    maroon_pixel = find_object(input_grid, 9)
    if maroon_pixel:
      # Move the maroon pixel to the bottom-right corner
      output_grid[maroon_pixel[0][0], maroon_pixel[0][1]] = 0  # Clear original position
      output_grid[grid_size[0]-1, grid_size[1]-1] = 9      # Place at new position
    
    # azure pixel stays on row, we will return the input for now
    # we need more information to decide the rule

    return output_grid
```
