# 5614dbcf • 008 • example_2 • investigate_coder

---
```python
"""
The input grid is reduced to a 3x3 output grid. The central color of significant colored regions (red and orange 3x3 blocks) from the input are placed in the output grid, preserving their relative positions. Other colors (grey) and background (white) are mostly ignored, with the output background remaining white.
"""

import numpy as np

def find_central_color(grid, region_top_left, region_size):
    """Finds the central color of a square region."""
    center_row = region_top_left[0] + region_size // 2
    center_col = region_top_left[1] + region_size // 2
    return grid[center_row, center_col]

def find_colored_regions(grid, region_size):
    """Identifies regions of size `region_size` with uniform color and returns their top-left coordinates and color."""
    regions = []
    rows, cols = grid.shape
    for i in range(rows - region_size + 1):
        for j in range(cols - region_size + 1):
            subgrid = grid[i:i+region_size, j:j+region_size]
            unique_colors = np.unique(subgrid)
            if len(unique_colors) == 1 and unique_colors[0] != 0:  # Ignore background color
                regions.append(((i, j), unique_colors[0]))
    return regions

def transform(input_grid):
    # Initialize output_grid as 3x3 with all zeros (white)
    output_grid = np.zeros((3, 3), dtype=int)

    # Find 3x3 colored regions in the input grid
    regions = find_colored_regions(input_grid, 3)

    # Place the central color of each identified region into the output grid
    for (top_left, color) in regions:
        # Calculate relative position in the output grid (top-center, bottom-center, etc.)
        #  Crude relative positioning based on input grid center.  This assumes
        #  that there will be at most one region per third of input vertically.
        rows, _ = input_grid.shape
        region_row = top_left[0]
        if region_row < rows / 3:
          output_row = 0 #top
        elif region_row < 2 * rows / 3:
          output_row = 1 #middle
        else:
          output_row = 2      # Bottom
        output_grid[output_row, 1] = color

    return output_grid
```
