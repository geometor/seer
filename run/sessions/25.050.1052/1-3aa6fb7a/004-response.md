# 1-3aa6fb7a • 004 • example_2 - CODE

---
```python
"""
For each azure L-shape in the input grid:
Find its uppermost and leftmost cell. 
If the L-shape is oriented such that the two other cells are below and to the right of the top-left cell, change the cell immediately to the right of the top-left cell to blue.
If the L-shape is oriented such that the two other cells are below and to the left of the top-left, change the cell immediately below the top-left to blue.
If the L_shape is oriented such that the two other cells are up and to the left, change the cell immediately to the left of the top-left to blue.
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds all L-shaped objects of a specific color and returns the top-left corner coordinates.
    """
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color:
                # Check for all possible L-shape orientations (3 cells)
                if r + 1 < rows and c + 1 < cols and grid[r + 1, c] == color and grid[r, c + 1] == color:
                    l_shapes.append((r, c))  # Down and Right
                elif r + 1 < rows and c -1 >=0 and grid[r + 1, c] == color and grid[r+1, c - 1] == color:
                    l_shapes.append((r, c))  # Down and Left (from Top-Left)
                elif r -1 >= 0  and c -1 >=0 and grid[r - 1, c] == color and grid[r, c - 1] == color:
                    l_shapes.append((r,c))  # Up, Left
                elif r + 1 < rows and c + 1 < cols and grid[r+1, c] == color and grid[r + 1, c + 1] == color:
                     l_shapes.append((r,c)) # Down, Right (from Top-Left)
                elif r +1 < rows and c + 1 < cols and grid[r, c+1] == color and grid[r + 1, c + 1] == color:
                    l_shapes.append((r,c))
    return l_shapes

def transform(input_grid):
    """
    Transforms the input grid based on L-shape orientation and paints an adjacent cell blue.
    """
    output_grid = np.copy(input_grid)
    azure_l_shapes = find_l_shapes(output_grid, 8)

    for r, c in azure_l_shapes:
        # Check L-shape orientation and paint adjacent cell blue
        if r + 1 < output_grid.shape[0] and c + 1 < output_grid.shape[1] and output_grid[r + 1, c] == 8 and output_grid[r, c + 1] == 8:
            output_grid[r, c + 1] = 1  # Down and Right - paint Right
        elif r + 1 < output_grid.shape[0] and c - 1 >= 0 and output_grid[r + 1, c] == 8 and output_grid[r + 1, c -1] == 8 :
            output_grid[r + 1, c] = 1  # Down and Left - paint Down
        elif r -1 >= 0 and c -1 >=0 and  output_grid[r-1,c] == 8 and output_grid[r , c - 1] == 8 :
              output_grid[r, c - 1] = 1 # Up and left - paint left
        elif r + 1 < output_grid.shape[0] and c + 1 < output_grid.shape[1] and output_grid[r+1, c] == 8 and output_grid[r+1, c+1] == 8 :
            output_grid[r + 1, c] = 1 #Down, Right (from top-left)
        elif r+1 < output_grid.shape[0] and c+1 < output_grid.shape[1] and output_grid[r,c+1] == 8 and output_grid[r+1,c+1] == 8 :
            output_grid[r+1,c] = 1 #Down, Right (from top-left)

    return output_grid
```

