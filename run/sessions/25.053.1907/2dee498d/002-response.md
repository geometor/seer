# 2dee498d • 002 • example_1 - CODE

---
```python
"""
The transformation extracts the top-left 3x3 subgrid from the input grid.  The output grid is always 3x3. The program takes the input grid, and creates a new grid, by copying the value from the cell to a corresponding output cell from [0,0] to [2,2].
"""

import numpy as np

def transform(input_grid):
    """
    Extracts the top-left 3x3 subgrid from the input grid.
    """
    # Initialize the output grid as a 3x3 array.
    output_grid = np.zeros((3, 3), dtype=int)

    # Iterate through the rows and columns of the output grid.
    for row in range(3):
        for col in range(3):
            # Copy the corresponding value from the input grid to the output grid.
            # Check if row and col are within the bounds of input_grid
            if row < input_grid.shape[0] and col < input_grid.shape[1]:
                output_grid[row, col] = input_grid[row, col]
            else:
                output_grid[row,col] = 0 # assign a default of white (0) if out of bounds
    return output_grid
```
