# 32597951 • 004 • refine_coder

---
```python
"""
1.  **Identify Azure Region:** Find all pixels with the color azure (8) in the input grid. This contiguous block constitutes the "azure region."

2.  **Determine Vertical Bounds:** Calculate the minimum and maximum row indices occupied by the azure region.

3.  **Conditional Transformation:** Iterate through each pixel in the input grid.
    *   If a pixel is blue (1):
        *   Check if it is *adjacent* (horizontally, vertically, or diagonally) to *any* pixel within the azure region.
        *   Check if the blue pixel's row index falls *within* the vertical bounds (inclusive) of the azure region (min_row <= row <= max_row).
        * If *both* conditions are true, change the pixel's color to green (3).

4.  **Preservation:** All pixels that do not meet the transformation criteria retain their original color values.
"""

import numpy as np

def get_azure_region(grid):
    """Finds the coordinates of all azure (8) pixels."""
    return np.argwhere(grid == 8)

def get_vertical_bounds(azure_region):
    """Determines the minimum and maximum row indices of the azure region."""
    rows = azure_region[:, 0]
    return np.min(rows), np.max(rows)

def is_adjacent(coord1, coord2):
    """Checks if two coordinates are adjacent (horizontally, vertically, or diagonally)."""
    return abs(coord1[0] - coord2[0]) <= 1 and abs(coord1[1] - coord2[1]) <= 1

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
                for azure_coord in azure_region:
                    if is_adjacent((r, c), azure_coord): #check adjacent
                        if min_row <= r <= max_row: # Check within vertical bounds
                            is_adjacent_to_azure = True
                            break
                if is_adjacent_to_azure:
                    output_grid[r, c] = 3  # Change to green

    return output_grid
```
