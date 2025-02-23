# 5-150deff5 • 004 • refine_coder

---
```python
"""
Identifies a gray (5) object in the input grid and segments it into two regions for each row. The region with pixels to the left of the input region's average x coordinate within each row is colored azure (8), while the region with pixels to the right is colored red (2). The rest of the grid (background) remains unchanged.
"""

import numpy as np

def get_object_pixels(grid, color):
    # returns a list of (x,y) coordinates that correspond to the specified color
    return [(x,y) for x,row in enumerate(grid) for y, pixel in enumerate(row) if pixel == color]

def transform(input_grid):
    """Transforms the input grid according to the described rule."""

    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    
    # 1. Identify the Input Shape:
    gray_pixels = get_object_pixels(input_grid, 5)
        
    if not gray_pixels:
       return output_grid

    # 2. Segment the Shape by Row:
    for x, row in enumerate(input_grid):
        # Find gray pixels in the current row
        row_gray_pixels = [(rx, ry) for rx, ry in gray_pixels if rx == x]

        if not row_gray_pixels:
            continue

        # Calculate average x-coordinate for gray pixels in this row
        x_coords = [ry for _, ry in row_gray_pixels]
        avg_x = sum(x_coords) / len(x_coords)

        # 3. Color the Regions based on row average:
        for rx, ry in row_gray_pixels:
            if ry <= avg_x:
                output_grid[rx][ry] = 8  # Azure
            else:
                output_grid[rx][ry] = 2  # Red

    # 4. Preserve Background (already handled by copying the input grid).
    return output_grid
```
