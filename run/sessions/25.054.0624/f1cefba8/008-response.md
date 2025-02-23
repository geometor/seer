# f1cefba8 • 008 • example_2 • investigate_coder

---
```python
"""
Transforms an input grid containing a central shape of blue and yellow pixels. 
The blue pixels are preserved. Some yellow pixels are changed to another color.
Yellow vertical lines are added and also elements colored yellow are added 
to the left and right borders where white columns existed.
"""

import numpy as np

def find_object(grid, colors):
    rows, cols = grid.shape
    object_pixels = []
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] in colors:
                object_pixels.append((r, c))
    return object_pixels

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find the central object (blue and yellow pixels)
    object_pixels = find_object(input_grid, [1, 4])

    # keep blue pixels
    for r, c in object_pixels:
      if input_grid[r,c] == 1:
        output_grid[r, c] = 1

    # keep yellow lines
    for r, c in object_pixels:
      if input_grid[r,c] == 4 and (r == 6 or r == 8):
           output_grid[r,c] = 4
    
    # yellow vertical lines
    for r in [3, 7, 11]:
        output_grid[r,7] = 4

    # yellow borders
    for r in range(rows):
      if output_grid[r, 0] == 0:
        output_grid[r,0] = 4
      if output_grid[r, cols - 1] == 0:
        output_grid[r, cols-1] = 4
        

    return output_grid
```
