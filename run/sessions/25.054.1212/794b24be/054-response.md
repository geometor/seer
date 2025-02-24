# 794b24be • 054 • refine_coder

---
```python
"""
Identifies blue (1) pixels in the input grid. Changes those pixels to red (2)
in both input and output grids. Propagates the red color horizontally and
vertically from the original blue pixel locations, replacing white (0) pixels
with red (2) until a non-white pixel or grid boundary is reached.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    input_grid_copy = np.copy(input_grid) # work with a copy

    # Get the dimensions of the grid.
    rows, cols = output_grid.shape

    # Iterate through each cell of the INPUT grid (important for propagation)
    for r in range(rows):
        for c in range(cols):
            if input_grid_copy[r, c] == 1:  # Found a blue pixel in the *original* input
                # Change the blue pixel to red in *both* grids
                output_grid[r, c] = 2
                input_grid_copy[r,c] = 2


                # Propagate Up
                current_row = r - 1
                while current_row >= 0 and output_grid[current_row, c] == 0:
                    output_grid[current_row, c] = 2
                    current_row -= 1

                # Propagate Down
                current_row = r + 1
                while current_row < rows and output_grid[current_row, c] == 0:
                    output_grid[current_row, c] = 2
                    current_row += 1

                # Propagate Left
                current_col = c - 1
                while current_col >= 0 and output_grid[r, current_col] == 0:
                    output_grid[r, current_col] = 2
                    current_col -= 1

                # Propagate Right
                current_col = c + 1
                while current_col < cols and output_grid[r, current_col] == 0:
                    output_grid[r, current_col] = 2
                    current_col += 1

    return output_grid
```
