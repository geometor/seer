# 5-150deff5 • 006 • Response

---

*text:*

```python
"""
This program takes an input grid and transforms it based on the following rules:
1. Identifies a single connected object of color 5 (gray).
2. Divides the gray object into two regions: "inner" and "outer".
   - The "outer" region consists of gray pixels (color 5) that have at least one neighbor of color 0.
   - The "inner" region consists of the remaining gray pixels (color 5).
3. Recolors the inner region to color 8 (azure).
4. Recolors the outer region to color 2 (red).
5. Keeps the background (color 0) unchanged.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """Returns the coordinates of the neighbors of a cell."""
    rows, cols = grid.shape
    neighbors = []
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i, j) != (row, col):
                neighbors.append((i, j))
    return neighbors

def find_object(grid, color):
    """Finds the coordinates of all cells belonging to the object of a given color."""
    object_cells = []
    for r in range(grid.shape[0]):
      for c in range(grid.shape[1]):
        if grid[r,c] == color:
          object_cells.append((r,c))

    return object_cells
    

def segment_object(grid, object_cells):
    """Segments the object into inner and outer regions."""
    inner_region = []
    outer_region = []

    for row, col in object_cells:
        neighbors = get_neighbors(grid, row, col)
        is_outer = False
        for n_row, n_col in neighbors:
            if grid[n_row, n_col] == 0:
                is_outer = True
                break
        if is_outer:
            outer_region.append((row, col))
        else:
            inner_region.append((row, col))

    return inner_region, outer_region

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    # Initialize output_grid with the same dimensions and background color as the input.
    output_grid = np.zeros_like(input_grid)

    # Find the object with color 5 (gray).
    object_cells = find_object(input_grid, 5)
    
    # Check that we have one object
    if not object_cells:
        return output_grid

    # Segment the object into inner and outer regions.
    inner_region, outer_region = segment_object(input_grid, object_cells)

    # Recolor the inner region to color 8 (azure).
    for row, col in inner_region:
        output_grid[row, col] = 8

    # Recolor the outer region to color 2 (red).
    for row, col in outer_region:
        output_grid[row, col] = 2

    return output_grid
```

