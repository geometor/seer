# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
The transformation preserves the azure (8) colored L-shaped objects. For each L shape, it adds a blue (1) colored pixel to the direct right of the corner of the "L".
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous regions of the specified color in the grid.
    Returns a list of coordinates for each object.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))

        neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
        for nr, nc in neighbors:
            dfs(nr, nc, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def find_l_corner(object_coords):
    """
    Finds the corner cell of an L-shaped object.
    Assumes the object is a 3-cell L-shape.
    """
    x_coords = [coord[0] for coord in object_coords]
    y_coords = [coord[1] for coord in object_coords]

    for coord in object_coords:
      x,y = coord
      #check if it is an "L" corner: two neighbors orthogonally, one diagonally, for a total of three.
      neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
      neighbor_count = 0
      for nx, ny in neighbors:
          if (nx,ny) in object_coords:
              neighbor_count +=1
      if neighbor_count == 2: # This is corner
          return (x,y)
    return None

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    output_grid = np.copy(input_grid)
    objects_8 = find_objects(input_grid, 8)

    for obj in objects_8:
        corner = find_l_corner(obj)
        if corner:
            x, y = corner
            # Check bounds and place the blue pixel to the right
            if y + 1 < output_grid.shape[1]:
                output_grid[x, y + 1] = 1

    return output_grid
```

