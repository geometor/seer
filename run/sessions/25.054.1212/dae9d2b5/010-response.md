# dae9d2b5 • 010 • refine_coder

---
```python
"""
The input is a 3x6 grid, and the output is a 3x3 grid. The transformation reduces the input grid column-wise. Each pair of adjacent input columns (columns 1 & 2, 3 & 4, 5 & 6) is combined to form a single output column (columns 1, 2, 3, respectively). For each row, compare the pixels in the two corresponding input columns. If *either* pixel is not white (0), the corresponding output pixel in that row is magenta (6). If *both* pixels are white (0), the output pixel is white (0).
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid with dimensions 3x3, filled with white (0)
    output_grid = np.zeros((3, 3), dtype=int)

    # Iterate through columns of the output grid
    for out_col in range(3):
        # Corresponding columns in the input grid
        in_col1 = out_col * 2
        in_col2 = out_col * 2 + 1

        # Iterate through rows
        for row in range(3):
            # Check if either corresponding input pixel is non-white using OR
            if (input_grid[row, in_col1] != 0) or (input_grid[row, in_col2] != 0):
                output_grid[row, out_col] = 6  # Set output pixel to magenta (6)
            # Otherwise, the output pixel remains white (0), which is the default.

    return output_grid
```

