# d4469b4b • 034 • refine_coder

---
```python
"""
The input 5x5 grid is transformed into a 3x3 output grid. The transformation involves checking overlapping 3x3 regions of the input grid. For each 3x3 region centered at (i, j) of the input grid, if any pixel in the region is non-white (not 0), the corresponding pixel (i, j) in the output grid is set to gray (5). Otherwise, it remains white (0).
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.zeros((3, 3), dtype=int)  # Initialize output grid to all white (0)

    # Iterate through the *centers* of the 3x3 overlapping regions, which corresponds to the output grid indices
    for i in range(3):
        for j in range(3):
            # Define the 3x3 region
            row_start = i
            row_end = i + 3
            col_start = j
            col_end = j + 3

            # Extract the 3x3 region from the input grid
            region = input_grid[row_start:row_end, col_start:col_end]

            # Check if any pixel in the region is non-white
            if np.any(region != 0):
                output_grid[i, j] = 5  # Set corresponding output pixel to gray (5)

    return output_grid.tolist()
```
