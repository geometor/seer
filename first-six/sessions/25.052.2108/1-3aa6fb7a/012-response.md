# 1-3aa6fb7a • 012 • refine_code - CODE

---
```python
"""
1.  Initialization: Create a copy of the input grid. This copy will become the output grid.
2.  Azure Pixel Identification: Iterate through each pixel of the *input* grid.
3.  Isolation Check: For each pixel in the *input* grid, check if it is azure (8). If it is, determine if it's isolated using the `is_alone` function, and using the *original* `input_grid`.
4.  Conditional Color Change:
    - If a pixel is azure *and* determined to be isolated (based on input), change the corresponding pixel in the `output_grid` to blue (1).
    - Otherwise, make *no change* to the `output_grid`, keeping the original pixel value.
5.  Output: After iterating through all pixels, the `output_grid` now represents the transformed grid.
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
            # Check if the pixel is azure in the input_grid
            if input_grid[i, j] == 8:
                # Check if the azure pixel is isolated in the input_grid
                if is_alone(input_grid, i, j, 8):
                    # Change the color of the isolated azure pixel to blue in the output_grid
                    output_grid[i, j] = 1

    return output_grid
```
