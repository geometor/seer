# 1b2d62fb • 016 • refine_coder

---
```python
"""
1.  **Identify Target Column:** Locate the column in the input grid that is completely filled with blue (1) pixels. Record its index.
2.  Change the color of the blue pixels to azure (8).
3.  Build output grid including the columns left and right of the original blue
    column, and place them to the left and right of the new azure column.
4. Maintain color and spatial relationships for all columns.
"""

import numpy as np

def find_blue_column(grid):
    for j in range(grid.shape[1]):
        if np.all(grid[:, j] == 1):
            return j
    return -1

def transform(input_grid):
    # Find the index of the blue column
    blue_column_index = find_blue_column(input_grid)

    if blue_column_index == -1:
        return None

    # Initialize the output grid with the correct dimensions
    output_grid = np.zeros((input_grid.shape[0], 3), dtype=int)

    # Fill the center column with azure (8)
    output_grid[:, 1] = 8

    # Handle left side
    if blue_column_index > 0:
        output_grid[:, 0] = input_grid[:, blue_column_index - 1]

    # Handle right side.
    if blue_column_index < input_grid.shape[1] - 1:
        output_grid[:, 2] = input_grid[:, blue_column_index + 1]
        
    return output_grid
```
