# 794b24be • 002 • example_1 • investigate_coder

---
```python
"""
1. Identify the single non-zero pixel in the input grid.
2. Move the pixel to the top-left corner (position 0,0).
3. Change the pixel's value from 1 to 2.
4. Change the color of the pixel from blue to red, and keep all white pixels the same.
"""

import numpy as np

def find_nonzero_pixel(grid):
    # Find the indices of the non-zero elements
    nonzero_indices = np.nonzero(grid)
    # Check if there's exactly one non-zero pixel
    if len(nonzero_indices[0]) == 1:
        return nonzero_indices[0][0], nonzero_indices[1][0]
    else:
        return None

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)

    # Find the non-zero pixel
    pixel_location = find_nonzero_pixel(input_grid)

    # if non zero pixel exists
    if pixel_location:
      # Move pixel to (0,0)
      output_grid[0, 0] = 2    # set value and color

    return output_grid
```
