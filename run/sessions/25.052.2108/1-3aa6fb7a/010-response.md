# 1-3aa6fb7a • 010 • refine_code - CODE

---
```python
"""
1.  Identify Azure Pixels: Examine each pixel in the input grid. Identify pixels that have the color azure (8).

2.  Check for Isolation: For each azure pixel, determine if it is "isolated". An azure pixel is isolated if it does *not* touch any other azure pixel, including diagonally. This check must be performed against the original `input_grid`.

3.  Change Color of Isolated Pixels: If an azure pixel is determined to be isolated (based on the original input grid), change its color to blue (1) in the `output_grid`.

4.  Preserve Other Pixels:** All other pixels (non-isolated azure pixels, and pixels of any other color) retain their original color in the `output_grid`.
"""

import numpy as np

def is_alone(grid, i, j, color):
    """
    Checks if a pixel at (i, j) of a given color is "alone," meaning it doesn't
    touch any other pixel of the same color, even diagonally.
    """
    rows, cols = grid.shape
    for x in range(max(0, i - 1), min(rows, i + 2)):
        for y in range(max(0, j - 1), min(cols, j + 2)):
            if (x != i or y != j) and grid[x, y] == color:
                return False  # Found a neighbor of the same color
    return True

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through the grid to find azure pixels
    for i in range(rows):
        for j in range(cols):
            if input_grid[i, j] == 8:  # Check if the pixel is azure in input_grid
                if is_alone(input_grid, i, j, 8): # Use input_grid for isolation check
                    output_grid[i, j] = 1

    return output_grid
```
