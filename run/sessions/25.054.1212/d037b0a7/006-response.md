# d037b0a7 • 006 • refine_coder

---
```python
"""
Iterate through each row of the input grid. For each row, check the second-to-last column's color. If it's not black (0), replace the rightmost column's color with it. Then, propagate this non-black color from the second-to-last column upwards to other rows if they also had a non-black color in their second-to-last column.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each row.
    for i in range(rows):
        # Get the color in the second-to-last column.
        second_to_last_color = output_grid[i, cols - 2]

        # If the color is not black (0), replace the rightmost column's color.
        if second_to_last_color != 0:
            output_grid[i, cols - 1] = second_to_last_color

    # Propagate upwards.
    for i in range(rows - 2, -1, -1):
         if output_grid[i, cols-2] != 0:
            output_grid[i+1, cols-1] = output_grid[i+1, cols-2]

    for i in range(rows):
        if output_grid[i, cols-2] != 0:
             output_grid[i, cols-1] =  output_grid[i, cols-2]


    return output_grid
```
