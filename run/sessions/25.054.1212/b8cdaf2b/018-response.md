# b8cdaf2b • 018 • refine_coder

---
```python
"""
Copies the bottom n-2 rows of the input grid to the output grid, where n is the number of rows in the input.
Fills the top two rows of the output grid with white pixels (0).
Fills the third row of the output grid with the color of the pixel directly below it in the input.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid with the same dimensions as the input grid
    output_grid = np.zeros_like(input_grid)

    # Get the number of rows in the input grid
    num_rows = input_grid.shape[0]

    # Copy the bottom n-2 rows from input to output
    output_grid[2:] = input_grid[2:]

    # Fill the top two rows with white (0)
    output_grid[:2, :] = 0

    # Fill the third row by copying the color from the fourth row of input
    if num_rows > 3:
      output_grid[2, :] = input_grid[3, :]
    else:
      output_grid[2,:] = 0 #if there is no fourth row, third row is 0

    return output_grid
```
