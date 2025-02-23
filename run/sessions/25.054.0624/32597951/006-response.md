# 32597951 • 006 • refine_coder

---
```python
"""
1.  **Identify Azure Region:** Locate all azure (8) pixels in the input grid. This forms the azure region.

2.  **Determine Vertical Bounds:** Find the minimum and maximum row indices of the azure region.

3.  **Conditional Transformation**: Iterate through each pixel. If a pixel is blue (1), check two things:
    *   Is the pixel *adjacent* (horizontally, vertically, or diagonally) to *any* pixel in the azure region?
    *   Does the blue pixel's row index fall *within* the vertical bounds (inclusive) of the azure region?

4.  **Transformation Rule:** If *either* of the above conditions is true, change the blue pixel's color to green (3). If neither condition is true, keep the pixel's original color.

5.  **Bounds Check:** When determining if a pixel is adjacent to the azure region, be sure that the adjacent pixel is inside the grid - not outside the bounds of the grid.
"""

import numpy as np

def get_azure_region(grid):
    """Finds the coordinates of all azure (8) pixels."""
    return np.argwhere(grid == 8)

def get_vertical_bounds(azure_region):
    """Determines the minimum and maximum row indices of the azure region."""
    rows = azure_region[:, 0]
    return np.min(rows), np.max(rows)

def is_adjacent(coord1, coord2, grid_shape):
    """Checks if two coordinates are adjacent (horizontally, vertically, or diagonally) and within grid bounds."""
    row_diff = abs(coord1[0] - coord2[0])
    col_diff = abs(coord1[1] - coord2[1])
    within_bounds = (0 <= coord2[0] < grid_shape[0]) and (0 <= coord2[1] < grid_shape[1])
    return within_bounds and (row_diff <= 1) and (col_diff <= 1)

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    output_grid = np.copy(input_grid)
    azure_region = get_azure_region(input_grid)
    min_row, max_row = get_vertical_bounds(azure_region)

    # Iterate through all pixels
    for r in range(input_grid.shape[0]):
        for c in range(input_grid.shape[1]):
            if input_grid[r, c] == 1:  # Check if it's a blue pixel
                is_adjacent_to_azure = False
                within_vertical_bounds = min_row <= r <= max_row

                for azure_coord in azure_region:
                    if is_adjacent((r, c), azure_coord, input_grid.shape):
                        is_adjacent_to_azure = True
                        break  # Optimization: Exit inner loop once adjacency is found

                if is_adjacent_to_azure or within_vertical_bounds:
                    output_grid[r, c] = 3  # Change to green

    return output_grid
```
