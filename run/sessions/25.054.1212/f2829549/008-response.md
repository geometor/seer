# f2829549 • 008 • example_2 • investigate_coder

---
```python
"""
Transforms an input grid by extracting a solid-color vertical column, changing its color to green (3),
placing it as the rightmost column of the output grid, and filling the rest of the output grid with white (0).
"""

import numpy as np

def find_solid_color_column(grid):
    """Finds the first solid-color vertical column in a grid."""
    rows, cols = grid.shape
    for j in range(cols):
        first_color = grid[0, j]
        is_solid = True
        for i in range(1, rows):
            if grid[i, j] != first_color:
                is_solid = False
                break
        if is_solid:
            return j, first_color
    return None, None

def transform(input_grid):
    """Transforms the input grid according to the defined rule."""
    rows, cols = input_grid.shape

    # Find the solid-color column and its color
    column_index, column_color = find_solid_color_column(input_grid)

    # Initialize the output grid with white (0)
    output_grid = np.zeros((rows, rows), dtype=int)
    
    # if no solid column, return all 0
    if column_index is None:
        return output_grid

    # Fill the rightmost column with green (3)
    for i in range(rows):
        output_grid[i, -1] = 3

    return output_grid
```
