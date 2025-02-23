# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
Identifies two mirrored "L"-shaped azure objects in the input grid. 
For the top-left shape, it inserts a blue pixel below the uppermost azure pixel.
For the bottom-right shape, it inserts a blue pixel left-adjacent to the rightmost azure pixel.
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specified color in the grid.
    Returns a list of coordinates representing the corner pixel of each L-shape.
    """
    rows, cols = grid.shape
    l_corners = []

    for r in range(rows - 1):
        for c in range(cols - 1):
            if grid[r, c] == color:
                # Check for top-left L shape
                if grid[r + 1, c] == color and grid[r, c + 1] == color:
                    l_corners.append((r, c))
                #check for bottom-right L shape
                elif grid[r-1,c] == color and grid[r,c-1] == color:
                    l_corners.append((r,c))

    return l_corners

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    output_grid = np.copy(input_grid)
    azure = 8
    blue = 1

    # Find the corner coordinates of all azure L-shapes
    l_corners = find_l_shapes(input_grid, azure)

    # Insert blue pixels based on L-shape orientation
    for r, c in l_corners:
        # Check the orientation and place blue pixel
        if input_grid[r+1,c] == 8:
          output_grid[r + 1, c + 1] = blue  # Top-left L
        else:
          output_grid[r - 1, c - 1] = blue
    return output_grid
```
