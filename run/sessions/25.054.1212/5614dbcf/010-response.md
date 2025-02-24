# 5614dbcf • 010 • refine_coder

---
```python
"""
The input grid is reduced to a 3x3 output grid. The central color of significant colored regions (3x3 blocks of uniform color) from the input are placed in the output grid, preserving their relative positions. The output background is white.
"""

import numpy as np

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
        rows, cols = input_grid.shape
        region_row = top_left[0]
        region_col = top_left[1]

        # Determine output row
        if region_row < rows / 3:
            output_row = 0  # top
        elif region_row < 2 * rows / 3:
            output_row = 1  # middle
        else:
            output_row = 2  # Bottom

        # Determine output column
        if region_col < cols / 3:
            output_col = 0 # Left
        elif region_col < 2 * cols / 3:
            output_col = 1 # Center
        else:
            output_col = 2 # Right

        output_grid[output_row, output_col] = color

    return output_grid
```
