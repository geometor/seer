# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
The input grid has two azure (color 8) L-shaped objects. Add a blue (color 1) pixel to fill the empty corner of each L-shape, thus forming 2x2 squares.
"""

import numpy as np

def find_l_shape_corner(grid, color):
    """
    Finds the missing corner of an L-shaped object.
    """
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            subgrid = grid[r:r+2, c:c+2]
            if np.count_nonzero(subgrid == color) == 3:
                # Find the empty corner
                for i in range(2):
                    for j in range(2):
                        if subgrid[i, j] == 0:
                            return (r + i, c + j)
    return None

def transform(input_grid):
    """
    Transforms the input grid by filling the empty corner of each L-shape with blue pixel.
    """
    output_grid = np.copy(input_grid)
    
    # Find the missing corner of the first L-shape (top-left)
    corner1 = find_l_shape_corner(output_grid, 8)
    if corner1:
        output_grid[corner1] = 1

     # Iterate in the reverse order to find the second L-shape (bottom-right). This helps avoid finding the top L a second time
    rows,cols = output_grid.shape
    for r in reversed(range(rows - 1)):
        for c in reversed(range(cols - 1)):
             subgrid = output_grid[r:r+2, c:c+2]
             if np.count_nonzero(subgrid == 8) == 3:
                for i in range(2):
                    for j in range(2):
                        if subgrid[i,j] == 0:
                            output_grid[r + i, c+ j] = 1
                            break
                    else:
                      continue
                    break
        else:
            continue
        break


    return output_grid
```

