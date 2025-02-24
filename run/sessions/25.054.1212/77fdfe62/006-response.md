# 77fdfe62 • 006 • refine_coder

---
```python
"""
Extracts the colors from the four corners of the input grid (excluding a uniform colored border) and places those colors in the corresponding corners of a smaller output grid. The output grid dimensions are half that of the input grid after removing the border, rounded down. If the inner grid has dimensions greater than 2x2, the corner colors are replicated to form 2x2 blocks in the output.
"""

import numpy as np

def get_inner_grid(input_grid):
    """
    Removes the outer border of the input grid, assuming it's a uniform color.
    """
    rows, cols = input_grid.shape
    border_color = input_grid[0, 0]

    # Find the inner boundaries by checking for the border color.
    top = 0
    while top < rows and all(input_grid[top, :] == border_color):
        top += 1
    bottom = rows - 1
    while bottom >= 0 and all(input_grid[bottom, :] == border_color):
        bottom -= 1
    left = 0
    while left < cols and all(input_grid[:, left] == border_color):
        left += 1
    right = cols - 1
    while right >= 0 and all(input_grid[:, right] == border_color):
        right -= 1
        
    # Ensure that the indices define a valid inner grid
    if top > bottom or left > right:
      return np.array([])

    return input_grid[top:bottom+1, left:right+1]

def transform(input_grid):
    """
    Transforms the input grid to the output grid based on corner color extraction,
    border removal, and conditional replication.
    """

    # Remove the border to get the inner grid.
    inner_grid = get_inner_grid(input_grid)
    if inner_grid.size == 0:
      return np.zeros((0,0), dtype=int)
      

    # Get the dimensions of the inner grid.
    inner_rows, inner_cols = inner_grid.shape

    # Determine output grid dimensions.
    output_rows = inner_rows // 2
    output_cols = inner_cols // 2
    output_grid = np.zeros((output_rows, output_cols), dtype=int)

    # Extract the colors from the four corners of the inner grid.
    top_left_corner = inner_grid[0, 0]
    top_right_corner = inner_grid[0, inner_cols - 1]
    bottom_left_corner = inner_grid[inner_rows - 1, 0]
    bottom_right_corner = inner_grid[inner_rows - 1, inner_cols - 1]

    # Populate the corresponding corners of the output grid.
    output_grid[0, 0] = top_left_corner
    output_grid[0, output_cols - 1] = top_right_corner
    output_grid[output_rows - 1, 0] = bottom_left_corner
    output_grid[output_rows - 1, output_cols - 1] = bottom_right_corner

    # Replicate corner colors if the inner grid is larger than 2x2.
    if inner_rows > 2 and inner_cols > 2:
        if output_rows > 1:
            output_grid[1, 0] = top_left_corner
        if output_cols > 1:
            output_grid[0, 1] = top_left_corner
        if output_rows > 1 and output_cols > 1:    
            output_grid[1, 1] = top_left_corner

        if (output_rows-2) >=0 and (output_cols -1) >=0:
          output_grid[output_rows-2, output_cols - 1] = top_right_corner
        if (output_rows-1) >=0 and (output_cols -2) >=0:
          output_grid[output_rows - 1, output_cols - 2] = bottom_right_corner

        if (output_rows-2) >=0 and (output_cols -2) >=0:
          output_grid[output_rows-2, output_cols-2] = bottom_right_corner

    return output_grid
```
