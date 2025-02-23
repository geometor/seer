# 0a938d79 • 018 • example_3 - CODE

---
```python
"""
Replicates red and green pixels from the input grid horizontally across their respective rows,
then repeats this pattern of red line, a white line, green line, a white line, throughout the output grid.
"""

import numpy as np

def find_pixel_by_color(grid, color):
    # Find the coordinates of the first pixel with the specified color.
    coords = np.argwhere(grid == color)
    if coords.size > 0:
      return coords[0]
    return None

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid, filled with white (0).
    output_grid = np.zeros_like(input_grid)

    # Find the red (2) and green (3) pixels in the input_grid.
    red_coord = find_pixel_by_color(input_grid, 2)
    green_coord = find_pixel_by_color(input_grid, 3)

    # Extend red and green pixels horizontally.
    if red_coord is not None:
        output_grid[red_coord[0], :] = 2
    if green_coord is not None:
        output_grid[green_coord[0], :] = 3

    # Create repeating pattern.
    if red_coord is not None and green_coord is not None:
      red_row = red_coord[0]
      green_row = green_coord[0]
      rows, cols = output_grid.shape
      
      pattern_rows = []
      
      pattern_rows.append(output_grid[red_row,:])
      pattern_rows.append(np.zeros(cols, dtype=int))
      pattern_rows.append(output_grid[green_row,:])
      pattern_rows.append(np.zeros(cols, dtype=int))
      
      for i in range(0,rows,4):
          for j in range(len(pattern_rows)):
            if i + j < rows:
                output_grid[i+j,:] = pattern_rows[j]


    return output_grid
```
