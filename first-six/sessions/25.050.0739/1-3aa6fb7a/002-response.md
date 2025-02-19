# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
The input contains some disconnected azure (8) colored cells that are part of a larger object. All of these isolated single azure cells become blue(1).
"""

import numpy as np

def find_objects(grid):
    """
    Finds objects in the grid.
    An object is a set of connected cells with the same color.
    """
    visited = set()
    objects = []

    def is_valid(pos):
        return 0 <= pos[0] < grid.shape[0] and 0 <= pos[1] < grid.shape[1]

    def dfs(row, col, color, current_object):
        if (row, col) in visited or not is_valid((row, col)) or grid[row, col] != color:
            return
        visited.add((row, col))
        current_object.append((row, col))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(row + dr, col + dc, color, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if (row, col) not in visited:
                color = grid[row, col]
                if color != 0:
                  current_object = []
                  dfs(row, col, color, current_object)
                  objects.append((color, current_object))
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Isolated azure (8) colored cells that are part of larger objects become blue (1).
    """
    # initialize output_grid
    output_grid = np.copy(input_grid)
    objects = find_objects(input_grid)

    # change output pixels
    for color, cells in objects:
        if color == 8:
          for cell in cells:
              row,col = cell
              neighbors = 0
              for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                  nr, nc = row + dr, col + dc
                  if 0 <= nr < input_grid.shape[0] and 0 <= nc < input_grid.shape[1] and input_grid[nr,nc] == 8:
                      neighbors +=1

              if neighbors == 0:
                  output_grid[row,col] = 1

    return output_grid
```
