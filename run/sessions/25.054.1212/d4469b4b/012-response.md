# d4469b4b • 012 • refine_coder

---
```python
"""
The transformation rule involves reducing a 5x5 grid to a 3x3 grid. The central pixel of the input becomes
the central pixel of the output.  Non-zero pixels on the border of the input (excluding the inner 3x3 area) 
cause specific rows or columns of the output to be set to 5 (gray). If a border pixel in the first/last row 
is non-zero, the entire second row of the output is 5. If a border pixel in the first/last column is non-zero, 
the entire second column of the output is 5.  Zero pixels in the input always remain zero in the output.
"""

import numpy as np

def transform(input_grid):
    # Initialize a 3x3 output grid filled with zeros (white).
    output_grid = np.zeros((3, 3), dtype=int)

    # Copy the central pixel
    output_grid[1, 1] = input_grid[2, 2]

    # Check the top and bottom rows (excluding the inner 3x3 part)
    for y in range(5):
        if (y < 1 or y > 3):
            if input_grid[0, y] != 0:
                output_grid[1,:] = 5
            if input_grid[4,y] != 0:
                output_grid[1,:] = 5

    # Check the left and right columns (excluding the inner 3x3 part)
    for x in range(5):
        if ( x < 1 or x > 3):
            if input_grid[x, 0] != 0:
                output_grid[:,1] = 5
            if input_grid[x,4] != 0:
                output_grid[:,1] = 5

    return output_grid
```
