# 1-3aa6fb7a • 004 • refine_coder

---
```python
"""
Iterate through all pixels in the input grid. If a pixel is azure (value 8),
determine if it is the top or bottom of a contiguous vertical line of azure
pixels. If it is, change its color to blue (value 1).  All other pixels remain
unchanged.
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid with the same dimensions and values as the input grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    def is_azure(grid, r, c):
        """Helper function to check if a pixel is azure."""
        return 0 <= r < rows and 0 <= c < cols and grid[r, c] == 8

    def find_top(grid, r, c):
        """Helper function to find the top of a vertical azure line."""
        while is_azure(grid, r - 1, c):
            r -= 1
        return r

    def find_bottom(grid, r, c):
        """Helper function to find the bottom of a vertical azure line."""
        while is_azure(grid, r + 1, c):
            r += 1
        return r

    # Iterate through all pixels
    for r in range(rows):
        for c in range(cols):
            # Check if the current pixel is azure
            if is_azure(output_grid, r, c):
                # Find the top and bottom of the vertical line
                top_row = find_top(output_grid, r, c)
                bottom_row = find_bottom(output_grid, r, c)

                # Apply the color change rule
                if r == top_row:
                    output_grid[r, c] = 1
                elif r == bottom_row:
                    output_grid[r,c] = 1
                # optimized to only check top or bottom - not whether to change the middle
                # elif r != top_row or r != bottom_row: # if not the top, could be any pixel below until the bottom
                #   pass # do nothing keep it azure

    return output_grid
```
