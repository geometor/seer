# 1-3aa6fb7a • 004 • Response

---

*text:*

```python
"""
Transformation Rule:

1. **Identify Objects:** In the input grid, identify L-shaped objects of color 8 (azure).
2. **Detect Changes**: The corner cell of each L-shape with color 8 generates a blue cell one row before and one column before. The cell at the corner of input changes to blue one up and one to the left.
3. **Transformation:** Copy all cells. Change the upper left of identified corner to blue.
"""

import numpy as np

def find_l_shapes(grid):
    """
    Finds L-shaped objects of color 8 in the grid.
    Returns a list of coordinates representing the corner of each L-shape.
    """
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 8:
                # Check for the four possible L-shape orientations
                if r + 1 < rows and c + 1 < cols and grid[r + 1, c] == 8 and grid[r, c + 1] == 8 :
                    l_shapes.append((r, c))
                elif r+1 < rows and c-1 >= 0 and grid[r+1,c] == 8 and grid[r, c-1] == 8:
                     l_shapes.append((r,c))
                elif r-1 >= 0 and c-1 >= 0 and grid[r-1,c] == 8 and grid[r, c-1] == 8:
                     l_shapes.append((r,c))
                elif r-1 >= 0 and c+1 < cols and grid[r-1,c] == 8 and grid[r, c+1] == 8:
                     l_shapes.append((r,c))

    return l_shapes

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    - Finds L-shaped objects of color 8.
    - Changes the color of the cell at (r-1, c-1) for each L-shape corner (r, c) to 1 (blue).
    """
    output_grid = np.copy(input_grid)
    l_shapes = find_l_shapes(input_grid)

    # Change the color of the cell one row and one column before the corner to blue (1)
    for r, c in l_shapes:
        if r > 0 and c > 0:
            output_grid[r - 1, c - 1] = 1

    return output_grid
```

