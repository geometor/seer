# 1-3aa6fb7a • 002 • Response

---

*text:*

```python
"""
Transformation Rule:

1. **Identify Objects:** In the input grid, identify L-shaped objects of color 8 (azure).
2. **Detect Changes**: The corner cell of each L-shape with color 8 changes to color 1 (blue).
3. **Transformation:** Copy all cells. Change the corner of identified shapes.
"""

import numpy as np

def find_l_shapes(grid):
    """
    Finds L-shaped objects of color 8 in the grid.
    Returns a list of coordinates representing the corner of each L-shape.
    """
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            if grid[r, c] == 8:
                # Check for the four possible L-shape orientations
                if grid[r + 1, c] == 8 and grid[r, c + 1] == 8 :
                    l_shapes.append((r, c))
                elif grid[r+1,c] == 8 and grid[r, c-1] == 8:
                     l_shapes.append((r,c))
                elif grid[r-1,c] == 8 and grid[r, c-1] == 8:
                     l_shapes.append((r,c))
                elif grid[r-1,c] == 8 and grid[r, c+1] == 8:
                     l_shapes.append((r,c))

    return l_shapes

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    - Finds L-shaped objects of color 8.
    - Changes the color of the corner cell of each L-shape to 1 (blue).
    """
    output_grid = np.copy(input_grid)
    l_shapes = find_l_shapes(output_grid)

    # Change the color of the identified corner cells to blue (1)
    for r, c in l_shapes:
        output_grid[r, c] = 1

    return output_grid
```
