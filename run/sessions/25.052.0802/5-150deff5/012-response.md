# 5-150deff5 • 012 • refine_code - CODE

---
```python
"""
The gray shape (color 5) present in the input is recolored. The initial part of the 'path' defined by the gray shape is filled with color 2 (red), and the final or latter part of the path is filled by color 8 (azure). The white background is preserved.
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

    # If no gray object is present, return the original grid.
    if gray_coords.size == 0:
      return output_grid

    # Recolour the entire shape with color 8 initially.
    output_grid[input_grid == 5] = 8

    # Determine the "start" and "end" of the path.  This is the tricky part
    # and relies on observation of the examples.  We are making an assumption
    # about how the path is traced. We'll use a simple heuristic based on row-major
    # order, then refine if necessary.  We convert the coordinates to a list of tuples.

    gray_coords_list = [(y, x) for y, x in gray_coords]
    gray_coords_list.sort() # Sorts primarily by row, then by column
    
    min_row = gray_coords_list[0][0]
    min_col = gray_coords_list[0][1]

    for r,c in gray_coords_list:
        if r == min_row or c == min_col:
            if input_grid[r,c] == 5:
                output_grid[r,c] = 2
        

    return output_grid
```

