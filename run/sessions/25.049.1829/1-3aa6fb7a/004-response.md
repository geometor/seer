# 1-3aa6fb7a • 004 • example_2 - CODE

---

*text:*

```python
"""
The transformation identifies all the azure (8) colored L-shaped objects (made of 3 cells of color 8) in the input grid. Then, changes to blue (1) the internal corner of those L-shaped objects.
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specific color in the grid.
    Returns a list of (row, col) tuples representing the "corner" of each L-shape.
    """
    rows, cols = grid.shape
    corners = []

    for r in range(rows - 1):
        for c in range(cols - 1):
            # Check for L shape (normal and rotations)
            if grid[r, c] == color:
                # normal L
                if grid[r + 1, c] == color and grid[r, c + 1] == color:
                    corners.append((r, c))
                # rotated 90
                if grid[r, c+1] == color and grid[r+1, c+1] == color:
                    corners.append((r,c+1))
                # rotated 180
                if grid[r+1, c] == color and grid[r + 1, c + 1] == color:
                    corners.append((r+1,c))
                # rotated -90
                if grid[r,c] == color and grid[r+1,c-1] == color:
                    corners.append((r,c))
            # mirrored L
            if grid[r,c] == color:
                if grid[r+1,c] == color and grid[r,c-1] == color:
                    corners.append((r,c))

    return corners

def transform(input_grid):
    """
    Transforms the input grid by identifying L-shaped objects of color 8,
    and changing the color of their internal corner to 1.
    """
    output_grid = np.copy(input_grid)
    l_corners = find_l_shapes(output_grid, 8)

    # Change the color of the identified corners
    for r, c in l_corners:
        output_grid[r, c] = 1

    return output_grid
```

