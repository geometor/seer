# 794b24be • 030 • refine_coder

---
```python
"""
Identify the smallest rectangle encompassing all blue pixels in the input grid.
Change all of the original blue pixels within the rectangle to red.
Set all other non-zero pixels that are not red to zero.
"""

import numpy as np

def find_bounding_box(grid):
    """Finds the bounding box of blue pixels in the grid."""
    blue_pixels = np.where(grid == 1)
    if len(blue_pixels[0]) == 0:  # Handle the case with no blue pixels
        return None  # Or return a default bounding box, e.g., ((0, 0), (0, 0))

    min_row, min_col = np.min(blue_pixels[0]), np.min(blue_pixels[1])
    max_row, max_col = np.max(blue_pixels[0]), np.max(blue_pixels[1])
    return (min_row, min_col), (max_row, max_col)

def transform(input_grid):
    """
    Transforms the input grid by finding the bounding box of blue pixels,
    filling the original blue pixel locations with red, and setting other non-zero pixels to zero.
    """
    output_grid = np.copy(input_grid)
    bounding_box = find_bounding_box(input_grid)

    if bounding_box:
        (min_row, min_col), (max_row, max_col) = bounding_box

        # change original blue cells to red
        blue_pixels = np.where(output_grid == 1)
        output_grid[blue_pixels] = 2

    # Zero out other non-zero pixels.
    output_grid[(output_grid != 0) & (output_grid != 2)] = 0
    return output_grid
```
