# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
Locate each 2x1 vertical rectangle of azure color (8). Add a blue cell (1) to the immediate right of both cells that constitute the 2x1 azure object.
"""

import numpy as np

def find_2x1_vertical_rectangles(grid, color):
    """
    Finds the coordinates of 2x1 vertical rectangles of the specified color.
    Returns a list of tuples, where each tuple contains the top and bottom coordinates of a rectangle.
    """
    rectangles = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols):
            if grid[r, c] == color and grid[r + 1, c] == color:
                rectangles.append(((r, c), (r + 1, c)))
    return rectangles

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Locate each 2x1 vertical rectangle of azure color (8).
    Add a blue cell (1) to the immediate right of both cells of the 2x1 azure object.
    """
    output_grid = np.copy(input_grid)
    azure_rectangles = find_2x1_vertical_rectangles(output_grid, 8)

    for top_coord, bottom_coord in azure_rectangles:
        # Add a blue cell to the right of the top cell, if within bounds
        if top_coord[1] + 1 < output_grid.shape[1]:
            output_grid[top_coord[0], top_coord[1] + 1] = 1
        # Add a blue cell to the right of the bottom cell, if within bounds
        if bottom_coord[1] + 1 < output_grid.shape[1]:
            output_grid[bottom_coord[0], bottom_coord[1] + 1] = 1

    return output_grid
```

