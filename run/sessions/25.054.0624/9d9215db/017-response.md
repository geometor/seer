# 9d9215db • 017 • refine_coder

---
```python
"""
1.  **Identify Objects:** The objects are the non-zero pixels in the input grid.
2.  **Horizontal Extension:** For each non-zero pixel, extend its color horizontally to the left and right.
3. **Boundaries**: The extension stops when it encounters the edge of the grid
   or another non-zero pixel (of any color).
4. **Additive Output**: The output is the sum of the results of each
   extension. An extension should write over only zeros in the grid.
"""

import numpy as np

def get_nonzero_pixels(grid):
    """Finds the coordinates and colors of non-zero pixels in a grid."""
    nonzero_pixels = []
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value != 0:
                nonzero_pixels.append(((r, c), value))
    return nonzero_pixels

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = np.zeros((rows, cols), dtype=int)

    # Get non-zero pixels
    nonzero_pixels = get_nonzero_pixels(input_grid)

    # Horizontal Extension for each non-zero pixel
    for (row, col), value in nonzero_pixels:
        # Extend to the right
        for c in range(col, cols):
            if input_grid[row, c] == 0 or c == col:  # only overwrite if it's zero in input or is original position
                output_grid[row, c] = value
            else:
                break # stop if non zero

        # Extend to the left
        for c in range(col - 1, -1, -1):
            if input_grid[row, c] == 0:  # only overwrite if zero in input
                output_grid[row, c] = value
            else:
                break

    return output_grid
```
