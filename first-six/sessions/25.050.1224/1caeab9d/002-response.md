# 1caeab9d • 002 • example_1 - CODE

---
```python
"""
The transformation involves identifying three 2x2 squares (red, yellow, and blue) in the input grid and repositioning them vertically. The red square moves down one row, the yellow square moves up one row, and the blue square remains in its original row, resulting in all three squares being aligned in the second row.
"""

import numpy as np

def find_objects(grid):
    """Finds 2x2 square objects in the grid."""
    objects = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            square = grid[r:r+2, c:c+2]
            if np.all(square == square[0,0]) and square[0,0] != 0:
                objects.append({'color': square[0,0], 'position': (r, c)})
    return objects

def transform(input_grid):
    """
    Transforms the input grid by moving the three 2x2 squares to the second row.
    """
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find the 2x2 square objects
    objects = find_objects(input_grid)

    # Clear the original positions of the squares in the output grid
    for obj in objects:
        r, c = obj['position']
        output_grid[r:r+2, c:c+2] = 0

    # Move each object to the second row (row index 1)
    for obj in objects:
        color = obj['color']
        r, c = obj['position']
        
        # Determine the new row based on the original row
        if color == 2: #red
            new_row = 1
        elif color == 4: #yellow
            new_row = 1
        elif color == 1: #blue
            new_row = 1
        
        output_grid[new_row:new_row+2, c:c+2] = color

    return output_grid
```

