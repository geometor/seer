# ea786f4a • 010 • refine_coder

---
```python
"""
Transforms a grid by inverting a frame of pixels around a central pixel, 
keeping the central pixel unchanged. The inversion changes non-zero pixels
to zero, but leaves zero pixels unchanged.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Identify the center pixel coordinates
    center_row = rows // 2
    center_col = cols // 2

    # Iterate through the grid to process the frame
    for i in range(rows):
        for j in range(cols):
            # Check if the pixel is on the frame (outermost rows and columns)
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                # Exclude the center pixel from the inversion
                if i != center_row or j != center_col:
                    # Invert frame pixels: non-zero becomes 0, 0 remains 0
                    if output_grid[i, j] != 0:
                        output_grid[i, j] = 0
            # copy non-frame pixels
            else:
               output_grid[i,j] = input_grid[i,j]

    return output_grid
```
