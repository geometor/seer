# 7b6016b9 • 002 • example_1 • investigate_coder

---
```python
"""
The transformation involves identifying azure shapes, filling their interiors with red, and changing the white background to green.
"""

import numpy as np

def get_objects(grid, color):
    """
    Finds objects of a specific color in the grid.

    Args:
        grid: The input grid (NumPy array).
        color: The color of the objects to find.

    Returns:
        A list of objects, where each object is a set of (row, col) coordinates.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def dfs(row, col, current_object):
        if (
            row < 0
            or row >= rows
            or col < 0
            or col >= cols
            or grid[row, col] != color
            or (row, col) in visited
        ):
            return
        visited.add((row, col))
        current_object.add((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(rows):
        for col in range(cols):
            if grid[row, col] == color and (row, col) not in visited:
                current_object = set()
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def fill_interior(grid, objects, fill_color):
    """
    Fills the interior of the objects with the specified color.
    """
    rows, cols = grid.shape
    output_grid = np.copy(grid)

    for obj in objects:
        #find bounding box
        min_row = min(r for r, c in obj)
        max_row = max(r for r, c in obj)
        min_col = min(c for r, c in obj)
        max_col = max(c for r, c in obj)

        for r in range(min_row + 1, max_row):
          for c in range(min_col+1,max_col):
            #check if cell is inside object
            if (r,c) not in obj: #must be interior
               #check all neighbors, if all neighbors exists and either are the object color or the fill, then fill
                neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                valid_neighbors = all(0 <= nr < rows and 0 <= nc < cols for nr, nc in neighbors)

                if valid_neighbors:
                  neighbor_colors = [output_grid[nr,nc] for nr, nc in neighbors]
                  if all(color == 8 or color == 2 for color in neighbor_colors):
                    output_grid[r,c] = fill_color
    return output_grid

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # change white background to green
    output_grid[output_grid == 0] = 3

    # Find azure shapes
    azure_objects = get_objects(input_grid, 8)

    # Fill interiors of azure objects with red
    output_grid = fill_interior(output_grid, azure_objects, 2)



    return output_grid
```
