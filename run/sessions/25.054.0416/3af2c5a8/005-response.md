# 3af2c5a8 • 005 • refine_coder

---
```python
"""
The input grid's rows and columns are duplicated to double the size of the output grid. The original input appears in the top-left quadrant of the output, mirrored horizontally and vertically and also in diagonal.
"""

import numpy as np

def transform(input_grid):
    # Create a mirrored copy of the input grid horizontally
    input_horizontal_mirror = np.fliplr(input_grid)
    # Create a mirrored copy of the input grid vertically
    input_vertical_mirror = np.flipud(input_grid)
    # Create a mirrored copy of the input grid diagonally (180 degree rotation)
    input_diagonal_mirror = np.rot90(input_grid, 2)

    # Combine the original and horizontally mirrored grids
    top_row = np.hstack((input_grid, input_horizontal_mirror))
    # Combine the vertically and diagonally mirrored grids
    bottom_row = np.hstack((input_vertical_mirror, input_diagonal_mirror))
    # Combine the two rows to create output
    output_grid = np.vstack((top_row, bottom_row))
    
    return output_grid
```
