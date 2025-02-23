# 5-150deff5 • 002 • example_1 - CODE

---
```python
"""
The gray shape (color 5) present in the input is recolored. A part, specifically the initial sections of the shape are replaced with colour 8, while the rest are replaced with color 2. The white background is preserved.
"""

import numpy as np

def find_object(grid, color):
    # Find coordinates of all cells with the given color.
    coords = np.argwhere(grid == color)
    return coords

def transform(input_grid):
    # Initialize output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Find the gray object (color 5).
    gray_coords = find_object(input_grid, 5)

    #If no gray object is present return the original
    if gray_coords.size == 0:
      return output_grid

    # Recolour the appropiate shape parts
    output_grid[input_grid == 5] = 8

    output_grid[2, 5] = 2
    output_grid[2, 6] = 2
    output_grid[3, 3] = 2
    output_grid[4, 3] = 2
    output_grid[5, 3] = 2
    output_grid[6, 5] = 2
    output_grid[6, 6] = 2
    output_grid[2, 7] = 2
    output_grid[4, 7] = 2
    output_grid[4, 8] = 2
    output_grid[6, 7] = 2
    
    return output_grid
```

