# ed36ccf7 • 006 • refine_coder

---
```python
"""
The transformation rule involves a conditional swap of the non-zero color and 0. It seems the corner element's are swapped. Specifically:
1. Compare each element of the grid to the element in the opposite corner.
2. If the value of the element is 0, and the opposite corner is not 0, swap the values.
3. If the value of the element is not 0, and the value of the opposite corner is zero, swap the values.
4.  Otherwise, the values remain in their original position.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = [row[:] for row in input_grid]  # Create a deep copy
    rows = len(input_grid)
    cols = len(input_grid[0])


    # Iterate through each element of the grid.
    for i in range(rows):
        for j in range(cols):
            # Find the opposite corner indices.
            opposite_i = rows - 1 - i
            opposite_j = cols - 1 - j

            # Conditional swap.
            if input_grid[i][j] == 0 and input_grid[opposite_i][opposite_j] != 0:
                output_grid[i][j] = input_grid[opposite_i][opposite_j]
                output_grid[opposite_i][opposite_j] = 0
            elif input_grid[i][j] != 0 and input_grid[opposite_i][opposite_j] == 0:
                output_grid[i][j] = 0
                output_grid[opposite_i][opposite_j] = input_grid[i][j]

    return output_grid
```
