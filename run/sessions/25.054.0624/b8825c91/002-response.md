# b8825c91 • 002 • example_1 • investigate_coder

---
```python
"""
1.  **Identify the Central Region:** Determine the boundaries of the rectangular (likely square) central region within the input grid. Visual inspection suggests this region covers a significant portion of the grid's center.
2.  **Conditional Color Swap:** Within the *central region only*:
    *   If a pixel is yellow (4), change it to green (3).
    *   If a pixel is magenta (6), change it to blue (1).
    *   If a pixel is azure (8), change it to maroon (9).
3. **Preserve Other Pixels:** All pixels outside the central region, and those within the central region *not* matching the colors above, remain unchanged.
"""

import numpy as np

def find_central_region(grid):
    # Determine the center coordinates of the grid
    rows, cols = grid.shape
    center_row, center_col = rows // 2, cols // 2

    # Define a starting size for the central region (e.g. half the size of the grid)
    region_height = rows // 2
    region_width = cols // 2

    # adjust to be odd dimensions so center has a pixel
    if region_height % 2 == 0:
      region_height += 1
    if region_width % 2 == 0:
      region_width += 1

    # Calculate the top-left and bottom-right coordinates of the region
    top_left_row = center_row - region_height // 2
    top_left_col = center_col - region_width // 2
    bottom_right_row = top_left_row + region_height
    bottom_right_col = top_left_col + region_width

    return top_left_row, top_left_col, bottom_right_row, bottom_right_col

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find the central region
    top_left_row, top_left_col, bottom_right_row, bottom_right_col = find_central_region(input_grid)

    # Iterate through the central region and apply color swap
    for i in range(top_left_row, bottom_right_row):
        for j in range(top_left_col, bottom_right_col):
            if output_grid[i, j] == 4:
                output_grid[i, j] = 3
            elif output_grid[i, j] == 6:
                output_grid[i, j] = 1
            elif output_grid[i, j] == 8:
                output_grid[i, j] = 9

    return output_grid
```
