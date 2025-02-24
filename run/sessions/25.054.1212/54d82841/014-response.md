# 54d82841 • 014 • example_3 • investigate_coder

---
```python
"""
The entire input grid is copied to the output grid. A new row is added at the bottom of the output grid. For each cell in the newly created row (starting from the left):
    *   If the cell above it, two rows up in the original row 3, is not 0, and it is the first cell in the output with this condition, then the new cell value is set to 4.
    *   If the cell, two rows up in original row 3 is not 0, and a previous cell in the output in the new row is 4, skip to the next one, unti a new cell with color not 0 is reached, set this to 4.
    *  If the cell above and two rows up is 0, then the new cell's value is set to 0.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    new_row = np.zeros(input_grid.shape[1], dtype=int)
    output_grid = np.vstack([output_grid, new_row])

    # change output pixels
    rows, cols = input_grid.shape
    found_first = False
    for j in range(cols):
        if input_grid[rows - 2, j] != 0:
          if not found_first:
             output_grid[rows,j] = 4
             found_first = input_grid[rows-2,j]
          elif input_grid[rows - 2,j] != found_first:
             output_grid[rows,j] = 4
             found_first = input_grid[rows-2,j]
          else:
            continue

        else:
          output_grid[rows, j] = 0


    return output_grid
```
