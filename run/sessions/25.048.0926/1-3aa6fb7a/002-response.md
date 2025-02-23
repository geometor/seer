# 1-3aa6fb7a • 002 • Response

---

*text:*

```python
"""
The transformation rule can be described as follows:

Locate any azure (8) L-shaped object, find its up-right and down-left corner, and change the color to blue(1).
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specific color in the grid.
    Returns a list of coordinates for each L-shape.
    """
    l_shapes = []
    rows, cols = grid.shape
    for i in range(rows - 1):
        for j in range(cols - 1):
            # Check for 2x2 block
            block = grid[i:i+2, j:j+2]
            if np.count_nonzero(block == color) == 3:
                # Determine the missing corner to identify L-shape orientation
                if block[0, 0] != color:
                    #up-left missing
                    positions = [(i,j+1), (i+1, j), (i+1, j+1)]
                    corner = (i, j)
                    l_shapes.append((positions, corner, "up-left"))

                elif block[0, 1] != color:
                    # up-right missing
                    positions = [(i, j), (i+1, j), (i+1, j+1)]
                    corner = (i, j+1)
                    l_shapes.append((positions, corner, "up-right"))
                elif block[1, 0] != color:
                    # down-left missing
                    positions =  [(i, j), (i, j+1), (i+1, j+1)]
                    corner = (i+1, j)
                    l_shapes.append((positions, corner, "down-left"))
                else:
                    #down-right missing
                    positions = [(i, j), (i, j+1), (i+1, j)]
                    corner = (i+1, j+1)
                    l_shapes.append((positions, corner, "down-right"))
    return l_shapes

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Locate azure (8) L-shaped objects, change color to blue(1).
    """
    output_grid = np.copy(input_grid)
    l_shapes = find_l_shapes(output_grid, 8)

    # Change color in output
    for l_shape in l_shapes:
        positions, corner, missing = l_shape

        if missing == "up-right":
            output_grid[corner] = 1
        if missing == "down-left":
            output_grid[corner] = 1

    return output_grid
```
