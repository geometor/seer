# 3c9b0459 • 011 • refine_coder

---
```python
"""
The transformation is a 90-degree clockwise rotation of the input grid, followed by a color swap based on the *original* positions of the pixels.  Specifically, the values in each cell of the *original, unrotated* grid are swapped with the values in the cell *diagonally opposite* across the center of the grid.

It is a two step process:
1. Rotate the grid 90 degrees clockwise.
2. Swap colors between original cells `(row, col)` and `(height - 1 - row, width - 1 - col)`.
"""

import numpy as np

def transform(input_grid):
    input_np = np.array(input_grid)
    height, width = input_np.shape

    # 1. Rotate the grid 90 degrees clockwise.
    rotated_grid = np.rot90(input_np, k=-1)
    output_grid = rotated_grid.copy()

    # 2. Swap colors based on original positions.
    for row in range(height):
        for col in range(width):
            # Find the diagonally opposite cell in the original grid.
            opposite_row = height - 1 - row
            opposite_col = width - 1 - col

            # Get the original values at these positions.
            original_val = input_np[row, col]
            opposite_val = input_np[opposite_row, opposite_col]
            
            #find the rotated locations for these
            rotated_row, rotated_col = col, height - 1 - row
            rotated_opposite_row, rotated_opposite_col = opposite_col, height - 1- opposite_row

            # Swap the color values in rotated grid
            output_grid[rotated_row, rotated_col] = opposite_val
            output_grid[rotated_opposite_row, rotated_opposite_col] = original_val
            

    return output_grid.tolist()
```
