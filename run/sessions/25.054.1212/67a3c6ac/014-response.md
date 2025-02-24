# 67a3c6ac • 014 • example_3 • investigate_coder

---
```python
"""
The input grid is transformed to the output grid by swapping cells across the main diagonal but in reverse.
In more detail:
- The cell at `input[row][col]` swaps with `output[5-col][5-row]`
- iterate through all rows from 0 to 5.
- inside of each row, iterate through all cols from 0 to 5
- swap each `input[row][col]` with `input[5-col][5-row]`
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by swapping cells across a diagonal axis.
    """
    # Create a copy of the input grid to serve as the output grid.
    output_grid = np.copy(input_grid)
    
    # Get the dimensions of the grid.
    rows, cols = input_grid.shape
    
    # Iterate through the grid, swapping elements across the anti-diagonal.
    for i in range(rows):
        for j in range(cols):
            output_grid[i, j] = input_grid[cols - 1 - j, rows - 1 - i]

    return output_grid
```
