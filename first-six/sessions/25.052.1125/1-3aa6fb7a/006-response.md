# 1-3aa6fb7a • 006 • example_2 - CODE

---
```python
"""
The transformation rule involves identifying azure (8) objects and placing blue (1) cells adjacent to specific points on these objects. For horizontal azure objects, a blue cell is placed to the left of the bottom cell. For vertical azure objects, a blue cell is placed to the right of the top cell. For L-shaped azure objects, a blue cell is placed next to the top corner.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        if (r, c) in visited or r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or grid[r, c] != color:
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
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    
    # Find azure (8) objects
    azure_objects = find_objects(input_grid, 8)
    
    # Process each azure object
    for obj in azure_objects:
        # Sort object cells by row and column
        obj.sort(key=lambda x: (x[0], x[1]))
        
        # Vertical line: Place blue to the right of the top
        if obj[0][1] == obj[-1][1] and obj[0][0] < obj[-1][0]:
            top_cell = obj[0]
            output_grid[top_cell[0], top_cell[1] + 1] = 1
            
        # Horizontal line: Place blue below to the left
        elif obj[0][0] == obj[-1][0] and obj[0][1] < obj[-1][1]:
            bottom_cell = obj[-1]
            output_grid[bottom_cell[0], bottom_cell[1] - 1] = 1
        
        # Check for L shape
        elif len(obj) == 3:
            # Find the corner point
            #The corner point appears twice
            
            coords = {}
            for cell in obj:
              if cell in coords.keys():
                coords[cell] += 1
              else:
                coords[cell] = 1
            
            corner_point = None
            for k,v in coords.items():
              if v > 1:
                corner_point = k
                break

            if corner_point is not None:
              # determine corner direction
              if obj[0][0] < obj[-1][0] and obj[0][1] < obj[-1][1]:
                output_grid[corner_point[0]-1, corner_point[1]] = 1
    return output_grid
```

