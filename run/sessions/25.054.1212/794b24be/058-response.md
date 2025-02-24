# 794b24be • 058 • refine_coder

---
```python
"""
1.  **Identify Seed Pixels:** Find all blue pixels (value 1) on the first row (row index 0) of the input grid.
2.  **Horizontal Propagation:** If any seed pixels are found, change all pixels on the first row to red (value 2), starting from the leftmost seed pixel position, and filling completely the first row.
3.  **Vertical Propagation**: If there is any blue pixel directly below blue seed pixel, changed to red.
4.  **All Other Pixels:** All other pixels that are not transformed to red above remains unchanged.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # get dimensions of grid
    rows, cols = output_grid.shape

    # 1. Identify Seed Pixels
    seed_pixels = []
    for j in range(cols):
        if input_grid[0, j] == 1:
            seed_pixels.append((0, j))

    # 2. Horizontal Propagation
    if seed_pixels:
        for j in range(cols):
            output_grid[0, j] = 2

    # 3. Vertical Propagation
        for r, c in seed_pixels:
           if r+1 < rows and input_grid[r+1,c] == 1:
               output_grid[r+1,c] = 2

    return output_grid
```
