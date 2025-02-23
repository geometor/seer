# 2-0ca9ddb6 • 006 • Response

---

*text:*

```python
"""
The transformation rule identifies all single-pixel red and blue objects.  A 2x2 yellow shape, cross-like, is drawn, centered on each red object's original location, and a cross of orange color, with arms of length 1 cell is created around each blue object's location.  The red and blue pixels are preserved. All other single pixels objects with distinct colors and the background remain unchanged.
"""

import numpy as np

def find_all_objects(grid, color):
    # Find the coordinates of *all* single-pixel objects of the specified color.
    coords = np.where(grid == color)
    return list(zip(coords[0], coords[1]))

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Find all red objects (color 2).
    red_positions = find_all_objects(input_grid, 2)
    for red_pos in red_positions:
        # Draw a yellow cross around each red object
        row, col = red_pos
        for i in range(-1,2):
            output_grid[row+i, col] = 4 if abs(i) == 1 else output_grid[row+i,col]
            output_grid[row, col+i] = 4 if abs(i) == 1 else output_grid[row,col+i]


    # Find all blue objects (color 1).
    blue_positions = find_all_objects(input_grid, 1)
    for blue_pos in blue_positions:
         # Draw an orange cross centered on each blue object.
        row, col = blue_pos
        for i in range(-1, 2):
            output_grid[row + i, col] = 7 if abs(i)==1 else output_grid[row + i, col]
            output_grid[row, col + i] = 7 if abs(i) == 1 else output_grid[row, col+i]

    return output_grid
```

