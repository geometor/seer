# 1-3aa6fb7a • 004 • example_2 - CODE

---
```python
"""
The transformation rule identifies disconnected azure objects, and for each of them, fills one adjacent white cell to blue.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = set()
    rows, cols = grid.shape
    
    def dfs(r, c, current_object):
        if (r, c) in visited or r < 0 or r >= rows or c < 0 or c >= cols or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    
    # Find azure (color 8) objects
    azure_objects = find_objects(input_grid, 8)
    

    # Iterate through each azure object
    for obj in azure_objects:

        # Iterate position by position inside the object
        for r, c in obj:
            # Define adjacent positions
            adjacent_positions = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            
            # Flag to track if a change happened
            changed = False

            # Iterate position by position looking for an empty slot (color 0)
            for nr, nc in adjacent_positions:
                if changed:
                    break # only make one change
                if 0 <= nr < input_grid.shape[0] and 0 <= nc < input_grid.shape[1] and input_grid[nr, nc] == 0:
                    output_grid[nr, nc] = 1  # Change color to blue (1)
                    changed = True # set the flag to stop modifications

    return output_grid
```

