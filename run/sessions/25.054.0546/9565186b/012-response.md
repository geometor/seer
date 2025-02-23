# 9565186b • 012 • refine_coder

---
```python
"""
Iterate through each pixel of the input grid.

1.  If color 4 is present in the input grid:
    *   If the pixel's color is 1, 2, 3, or 8, change its color to 5 (gray) in the output grid.
    *   If the pixel's color is 4, keep its color as 4 in the output grid.
    *   Otherwise, keep the original color.
2.  If color 4 is *not* present in the input grid:
    *   If the pixel's color is 1, 2, 3, or 8, change its color to 5 (gray) in the output grid.
    *   Otherwise, keep the original color.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape
    has_color_4 = 4 in input_grid

    # Iterate through each pixel in the input grid.
    for i in range(rows):
        for j in range(cols):
            color = input_grid[i, j]

            if has_color_4:
                if color in (1, 2, 3, 8):
                    output_grid[i,j] = 5
                elif color == 4:
                    output_grid[i,j] = 4
                # Otherwise, keep original
            else:
                if color in (1, 2, 3, 8):
                    output_grid[i, j] = 5
                # Otherwise, keep original

    return output_grid
```

