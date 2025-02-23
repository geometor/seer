# AboveBelow5 • 008 • example_2 • investigate_coder

---
```python
"""
The transformation identifies the orange (7) pixel in the second column of the input grid.
if the y position of the orange is > 1, then change the top most cell in column 2, to 7.
The yellow 4 fills the original position of the moved orange (7).
"""

import numpy as np

def find_pixel_by_color_in_column(grid, color, column_index):
    # Find the coordinates (row, col) of a pixel of the specified color within a given column.
    for row_index, row in enumerate(grid):
        if row[column_index] == color:
            return (row_index, column_index)
    return None  # Return None if no such pixel is found.

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # Find the orange pixel in the second column (index 1).
    orange_pixel_coords = find_pixel_by_color_in_column(input_grid, 7, 1)
    
    # if no orange, return
    if orange_pixel_coords is None:
      return output_grid
    
    # change the top cell to be orange
    output_grid[0][1] = 7
    
    if orange_pixel_coords[0] > 0:
        output_grid[orange_pixel_coords[0]][1] = 4

    return output_grid
```
