# 1b2d62fb • 010 • refine_coder

---
```python
"""
1.  **Identify Blue Pixels:** Find all pixels in the input grid that are blue (color code 1).
2.  **Determine Cropping Region:**
    *   Find the leftmost column containing any blue pixel.
    *   The cropped region starts one column to the left of this leftmost blue pixel's column.
    *   The cropped region extends three columns wide.
    *   The cropped region's height is the same as the input grid's height.
3.  **Crop:** Extract the defined cropped region from the input grid.
4.  **Transform Colors:**
    *   Within the cropped region, change all blue pixels (color code 1) to azure (color code 8).
    * Set all the other pixels in the cropped region to black (color code 0)
"""

import numpy as np

def find_blue_pixels(grid):
    # Find coordinates of all blue pixels.
    blue_pixels = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 1:
                blue_pixels.append((r, c))
    return blue_pixels

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape

    # Find all blue pixels
    blue_pixels = find_blue_pixels(input_grid)

    # Determine cropping region
    if not blue_pixels:
        return np.zeros((rows, 3), dtype=int).tolist()  # Return black 3-wide grid if no blue pixels

    leftmost_col = min(c for r, c in blue_pixels)
    start_col = max(0, leftmost_col - 1)
    end_col = min(cols, start_col + 3)  # Corrected end_col calculation
    cropped_grid = input_grid[:, start_col:end_col]
    
    output_grid = np.zeros_like(cropped_grid)

    # change output pixels in the cropped region
    cropped_rows, cropped_cols = cropped_grid.shape
    for r in range (cropped_rows):
        for c in range(cropped_cols):
            original_col = start_col + c  # Map cropped column back to the original grid's column index.
            if (r, original_col) in [(br, bc) for br, bc in blue_pixels]: # Check against original blue pixel coordinates.
                output_grid[r,c] = 8
            else:
                output_grid[r,c] = 0

    return output_grid.tolist()
```
