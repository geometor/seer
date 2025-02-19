# 1fad071e • 006 • example_3 - CODE

---
```python
"""
The transformation consists on:
   - scanning the grid from left to right and from top to bottom.
   - selecting the first two blue objects.
   - extracting the x-coordinates of their cells.
   - removing duplicates,
   - creating a new grid 1 row grid
   - setting its values to 1 when their index exists in the x-coordinates list or 0 otherwise.
"""

import numpy as np

def get_objects(grid, color):
    """
    Find objects of a specific color in the grid.
    Returns a list of lists of coordinates.
    """
    objects = []
    visited = set()

    def is_valid(x, y):
        return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]

    def dfs(x, y, current_object):
        if (x, y) in visited or not is_valid(x, y) or grid[x, y] != color:
            return
        visited.add((x, y))
        current_object.append((x, y))
        
        # Explore adjacent cells
        dfs(x + 1, y, current_object)
        dfs(x - 1, y, current_object)
        dfs(x, y + 1, current_object)
        dfs(x, y - 1, current_object)

    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x, y] == color and (x, y) not in visited:
                current_object = []
                dfs(x, y, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    # Find blue objects
    blue_objects = get_objects(input_grid, 1)

    # Select the first two blue objects
    selected_objects = blue_objects[:2]

    # Extract x-coordinates
    x_coordinates = []
    for obj in selected_objects:
        for x, y in obj:
            x_coordinates.append(y)

    # Remove duplicates and sort
    unique_x_coordinates = sorted(list(set(x_coordinates)))

    #create output grid
    output_length = len(unique_x_coordinates)*2+1
    output_grid = np.zeros(output_length, dtype=int)

    #set 1
    for x in unique_x_coordinates:
      output_grid[x] = 1

    return output_grid.reshape(1,-1)
```

