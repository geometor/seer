# 1-3aa6fb7a • 013 • refine_code - CODE

---
```python
"""
Finds all azure (color 8) objects in the input grid. For each azure object,
it adds a single blue (color 1) pixel adjacent to it in the following order
of priority: left, right, down, up. The blue pixel is added to the first
available blank (color 0) space found in that order.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = set()

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    # find azure objects
    azure_objects = find_objects(input_grid, 8)

    for azure_object in azure_objects:
        added = False
        # Priority 1: Left
        for r, c in sorted(azure_object):
          if c > 0 and output_grid[r, c - 1] == 0:
            output_grid[r, c - 1] = 1
            added = True
            break  # Stop after adding one blue pixel
        if added:
          continue
        
        # Priority 2: Right
        for r, c in sorted(azure_object):
           if c + 1 < output_grid.shape[1] and output_grid[r, c + 1] == 0:
             output_grid[r,c+1] = 1
             added = True
             break
        if added:
          continue
        
        # Priority 3: Down
        for r, c in sorted(azure_object):
           if r + 1 < output_grid.shape[0] and output_grid[r+1, c] == 0:
             output_grid[r+1,c] = 1
             added = True
             break
        if added:
          continue
        
        # Priority 4: Up
        for r, c in sorted(azure_object):
           if r - 1 >= 0 and output_grid[r-1, c] == 0:
             output_grid[r-1,c] = 1
             added = True
             break
        if added:
          continue


    return output_grid
```

