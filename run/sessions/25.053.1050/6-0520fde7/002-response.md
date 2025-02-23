# 6-0520fde7 • 002 • example_1 - CODE

---
```python
"""
1.  **Identify Key Feature:** Locate the vertical gray stripe (all pixels with color value 5) running down the center of the input grid.
2.  **Extract Central Region:** Consider a 3x3 sub-grid centered on the overall input.
3.  Count the blue pixels in the input
4.  **Determine Center Color** If the count of blue pixel is greater than 2. Set output central pixel color to be red (2)
5.  Fill all other pixels in the output with color value white (0).
"""

import numpy as np

def count_pixels_by_color(grid, color):
    return np.sum(grid == color)

def get_center_subgrid(grid, subgrid_height, subgrid_width):
    grid_height, grid_width = grid.shape
    center_row = grid_height // 2
    center_col = grid_width // 2
    
    row_start = center_row - subgrid_height // 2
    row_end = row_start + subgrid_height
    col_start = center_col - subgrid_width // 2
    col_end = col_start + subgrid_width
    
    return grid[row_start:row_end, col_start:col_end]
    

def transform(input_grid):
    # Initialize a 3x3 output grid filled with white (0)
    output_grid = np.zeros((3, 3), dtype=int)

    # Count blue pixels in input
    blue_count = count_pixels_by_color(input_grid, 1)

    # Determine center color.
    if blue_count > 2:
       output_grid[1, 1] = 2
    
    return output_grid
```
