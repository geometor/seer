# 1-3aa6fb7a • 002 • Response

---

*text:*

```python
"""
The transformation rule is: Find the upper-left azure pixel of each "L" shape and switch the azure pixel to blue.
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specific color in the grid.
    Returns a list of corner coordinates.
    """
    objects = []
    visited = set()

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))

        neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for nr, nc in neighbors:
            dfs(nr, nc, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                if len(current_object) > 2:

                  #find corner
                  min_r, min_c = float('inf'), float('inf')
                  for cell_r,cell_c in current_object:
                    if cell_r < min_r:
                      min_r = cell_r
                    if cell_c < min_c:
                      min_c = cell_c

                  objects.append((min_r, min_c))
    return objects

def transform(input_grid):
    """
    Transforms the input grid by finding L-shaped objects of color 8,
    and changing their upper-left pixel color to 1.
    """
    output_grid = np.copy(input_grid)
    l_shapes = find_l_shapes(input_grid, 8)

    # Change the color of the identified corners
    for r, c in l_shapes:
        output_grid[r, c] = 1

    return output_grid
```
