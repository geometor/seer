# 77fdfe62 • 002 • example_1 • investigate_coder

---
```python
"""
Extracts the colors from the four corners of the input grid (excluding a blue border) and places those colors in the corresponding corners of a smaller output grid. The rest of the output grid is filled with white (0).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid to the output grid based on corner color extraction.
    """
    # Get the dimensions of the input grid.
    rows, cols = input_grid.shape

    # Create a 4x4 output grid filled with white (0).
    output_grid = np.zeros((4, 4), dtype=int)

    # Extract the colors from the four corners of the inner 6x6 grid (excluding the border).
    top_left_corner = input_grid[0, 0]
    top_right_corner = input_grid[0, cols - 1]
    bottom_left_corner = input_grid[rows - 1, 0]
    bottom_right_corner = input_grid[rows - 1, cols - 1]

    # Populate the corresponding corners of the output grid.
    output_grid[0, 0] = top_left_corner
    output_grid[0, 3] = top_right_corner
    output_grid[3, 0] = bottom_left_corner
    output_grid[3, 3] = bottom_right_corner

    # create 2x2 subgrids from each corner color
    output_grid[1,0] = top_left_corner
    output_grid[0,1] = top_left_corner
    output_grid[1,1] = top_left_corner

    output_grid[2,3] = bottom_right_corner
    output_grid[3,2] = bottom_right_corner
    output_grid[2,2] = bottom_right_corner

    return output_grid
```
