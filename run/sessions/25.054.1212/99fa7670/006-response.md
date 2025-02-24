# 99fa7670 • 006 • refine_coder

---
```python
"""
Identifies non-white pixels in the input grid and expands them to the right and down, filling their respective rows and columns in the output grid. Expansion stops at either another non-white pixel or the edge of the grid.
"""

import numpy as np

def get_non_white_pixels(grid):
    """Finds coordinates of all non-white pixels in the grid."""
    non_white_pixels = []
    for row_index, row in enumerate(grid):
        for col_index, pixel_value in enumerate(row):
            if pixel_value != 0:
                non_white_pixels.append((row_index, col_index, pixel_value))
    return non_white_pixels

def transform(input_grid):
    """Transforms the input grid by expanding non-white pixels to the right and down, with blocking."""
    output_grid = np.zeros_like(input_grid)
    non_white_pixels = get_non_white_pixels(input_grid)

    for row, col, value in non_white_pixels:
        # Row Expansion (Right)
        for c in range(col, input_grid.shape[1]):
            if output_grid[row, c] != 0 and (row,c,output_grid[row,c]) not in non_white_pixels:
                break  # Stop at another non-white pixel
            if input_grid[row,c] != 0 and (row, c) != (row, col):
                break

            output_grid[row, c] = value

        # Column Expansion (Down)
        for r in range(row, input_grid.shape[0]):
            if output_grid[r, col] != 0 and (r,col, output_grid[r,col]) not in non_white_pixels:
                break  # Stop at another non-white pixel
            if input_grid[r, col] != 0 and (r, col) != (row, col):
                break
            output_grid[r, col] = value

    return output_grid
```
