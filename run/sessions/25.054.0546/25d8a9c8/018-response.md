# 25d8a9c8 • 018 • refine_coder

---
```python
"""
The output grid is the same size as the input grid (3x3).  The following color transformations occur:

*   If a pixel is yellow (4), red (2), orange(7) or maroon(9) in the input grid, it becomes black/white(0).
*   If a pixel is blue(1), gray (6) in the input grid, it is changed to grey(5)
*   If a pixel is green(3) in the input grid, it becomes black/white(0).
*    Otherwise, the pixel's color remains unchanged.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)

    # Iterate through each pixel of the input grid.
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Apply the color transformation rules.
            if input_grid[i, j] in [4, 2, 9, 7]:  # Yellow, Red, Maroon, Orange
                output_grid[i, j] = 0  # white
            elif input_grid[i, j] in [1, 6]:  # Blue, Gray
                output_grid[i, j] = 5  # Gray
            elif input_grid[i, j] == 3: #green
                output_grid[i,j] = 0

    return output_grid
```
