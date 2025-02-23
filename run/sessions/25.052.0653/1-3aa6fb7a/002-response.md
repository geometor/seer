# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
The input consists of two azure (color 8) L-shaped objects. The output preserves these objects and adds two blue (color 1) cells. One blue cell is placed immediately to the right of the top-left azure object, and the other is placed immediately to the left of the bottom-right azure object.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(r, c, current_object):
        if (r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or
                visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and not visited[r, c]:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find the azure objects
    azure_objects = find_objects(input_grid, 8)

    # Iterate through the found objects
    for obj in azure_objects:
        # Sort the object coordinates to find top-left and bottom-right
        sorted_coords = sorted(obj, key=lambda x: (x[0], x[1]))

        #For the top-left object
        if sorted_coords[0][0] < input_grid.shape[0] // 2: # Check if it's in top half
             #Find the rightmost coordinate of the object to add the blue to the right
            rightmost_coord = max(sorted_coords, key=lambda x: x[1])

            # Add blue cell to the right, if within the grid boundary
            if rightmost_coord[1] + 1 < output_grid.shape[1]:
                output_grid[rightmost_coord[0], rightmost_coord[1] + 1] = 1

         #For the bottom right object
        if sorted_coords[0][0] >= input_grid.shape[0] // 2:  # Check if it is in bottom half
            # Find the leftmost coordinate.
            leftmost_coord = min(sorted_coords, key=lambda x:x[1])

            # Add blue cell to its left, if within the grid boundary.
            if leftmost_coord[1] -1 >= 0:
                output_grid[leftmost_coord[0], leftmost_coord[1] - 1] = 1

    return output_grid
```

