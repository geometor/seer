# d037b0a7 • 016 • refine_coder

---
```python
"""
1.  Iterate through the input grid to find a yellow pixel (value 4).
2.  If a yellow pixel is found, copy it to the cell directly below it, *if it exists*. If that cell doesn't exist (at image boundary), do not modify.
3.  Iterate through the input grid to find a red pixel (value 2).
4.  If a red pixel is found, copy it to the cell directly below it, *if it exists*. If that cell doesn't exist (at image boundary), do not modify.
5. All other pixels remain unchanged.
6. The maximum extent of the rows should not exceed the original number of input grid rows, and each object has a bound equal to the count -1.
"""

import numpy as np

def find_pixel(grid, color_value):
    """Finds the coordinates of a pixel with a specific color value."""
    for r_idx, row in enumerate(grid):
        for c_idx, pixel in enumerate(row):
            if pixel == color_value:
                return r_idx, c_idx
    return None, None

def transform(input_grid):
    """Transforms the input grid according to the specified rules."""

    output_grid = np.copy(input_grid)  # Initialize output_grid as a copy of the input_grid
    rows, cols = output_grid.shape

    # Find and duplicate yellow pixel
    yellow_row, yellow_col = find_pixel(input_grid, 4)
    if yellow_row is not None and yellow_row + 1 < rows:
        output_grid[yellow_row + 1, yellow_col] = 4

    # Find and duplicate red pixel
    red_row, red_col = find_pixel(input_grid, 2)
    if red_row is not None and red_row + 1 < rows:
        output_grid[red_row + 1, red_col] = 2

    return output_grid
```
