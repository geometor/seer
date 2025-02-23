# 5-150deff5 • 006 • example_3 - CODE

---
```python
"""
The transformation rule is as follows:
1. Identify the Object: Find the contiguous region of color '5' (gray) in the input grid. This is our primary object.
2. Substitution 1: Every cell to the rigth of the central vertical axis of the object, that have color 5 is transformed to color 8.
3. Substitution 2: Every cell to the left of the central vertical axis of the object, that have color 5 is transformed to color 2.
"""

import numpy as np

def find_object(grid, color):
    # Find the coordinates of all cells with the specified color.
    coords = np.argwhere(grid == color)
    return coords

def find_object_center(object_coords):
    # Calculate the center (mean) of the object's coordinates.
    center = np.mean(object_coords, axis=0)
    return center

def transform(input_grid):
    # Create a copy of the input grid to serve as the output grid.
    output_grid = np.copy(input_grid)

    # Find the object with color 5.
    object_coords = find_object(input_grid, 5)

    # Find the x-coordinate of the object's center.
    if len(object_coords) > 0:
      center_x = find_object_center(object_coords)[1]


      # Iterate through the object coordinates and apply the transformation.
      for coord in object_coords:
          x, y = coord
          if y >= center_x:
              output_grid[x, y] = 8  # Right side: change to 8
          else:
              output_grid[x, y] = 2  # Left side: change to 2

    return output_grid
```

