# 32597951 • 008 • example_2 • investigate_coder

---
```python
"""
The input is a 17x17 grid. A contiguous region of '8' (azure) pixels is identified.  Within this region, specific '8' pixels are changed to '3' (green) based on their relative position within the '8' region.  Pixels with values '0' (white) and '1' (blue) are preserved.
"""

import numpy as np

def find_contiguous_region(grid, value):
    # Find the coordinates of all cells with the specified value.
    coords = np.argwhere(grid == value)
    if coords.size == 0:
        return None, None

    # Find top-left and bottom-right using min/max of the coordinates
    min_row = coords[:, 0].min()
    max_row = coords[:, 0].max()
    min_col = coords[:, 1].min()
    max_col = coords[:, 1].max()

    return (min_row, min_col), (max_row, max_col)

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    input_grid_np = np.array(input_grid)

    # Find the contiguous region of '8's
    top_left, bottom_right = find_contiguous_region(input_grid_np, 8)

    if top_left is None :
      return output_grid

    # Define the relative positions to change to '3'
    relative_positions_to_change = [
      (1,2),(2,1),(2,2),(2,3),(3,1), (3,2) , (3,3)
    ]

    # Iterate through the relative positions and change '8' to '3' in the output grid
    for rel_row, rel_col in relative_positions_to_change:
        row = top_left[0] + rel_row
        col = top_left[1] + rel_col

        #Check if the position to change is within the 8 region and inside the limits.
        if 0 <= row < output_grid.shape[0] and 0 <= col < output_grid.shape[1] and output_grid[row,col] == 8:
              output_grid[row, col] = 3


    return output_grid.tolist()
```
