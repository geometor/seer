# 1-3aa6fb7a • 004 • example_2 - CODE

---
```python
"""
The transformation rule involves adding a blue (1) pixel adjacent to each existing azure (8) object.
Specifically:

1. Identify Objects: Locate all azure (8) objects within the input grid.
2. Determine Placement: For each azure object, find a directly adjacent (non-diagonal) neighbor cell where a blue pixel can be placed.  The relative position matters.
3. Add Blue Pixel: Create a new blue (1) pixel at the determined location.
"""

import numpy as np

def find_objects(grid, color):
    # Find all objects of a specific color in the grid.
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
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(r + dr, c + dc, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    """Transforms the input grid according to the rule: Add a blue (1) pixel
    adjacent to each azure (8) object, considering relative position."""

    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
        # Iterate through cells of the object to determine its overall position.
        # This is a simplified approach; a more robust method might calculate a centroid.
        first_cell = obj[0]

        # Check relative position and add blue pixel accordingly.
        if first_cell[0] <= 2 and first_cell[1] <= 2: # Top-left quadrant or close.
            # Find an empty neighbor to the right.
            for r, c in obj:
                if c + 1 < output_grid.shape[1] and output_grid[r, c + 1] == 0:
                    output_grid[r, c + 1] = 1
                    break  # Place only one blue pixel per object.
        elif first_cell[0] >= 4 and first_cell[1] <= 2: # Bottom, somewhat to the left
             for r, c in obj:
                if c -1 >= 0 and output_grid[r,c-1] == 0:
                    output_grid[r,c-1] = 1
                    break
        elif first_cell[0] <= 2 and first_cell[1] >= 4 : #top-right
            for r, c in obj:
                if c-1 >= 0 and output_grid[r,c-1] == 0:
                    output_grid[r,c-1] = 1
                    break
        elif first_cell[0] >=2 and first_cell[0]<=4 and first_cell[1]<=2: # Center-Left
            for r, c in obj:
                if c + 1 < output_grid.shape[1] and output_grid[r,c+1] == 0:
                    output_grid[r, c+1] = 1
                    break

        elif first_cell[0]>=5 and first_cell[1]>=2 and first_cell[1]<=4: #Bottom-center
            for r, c in obj:
                if c - 1 >= 0 and output_grid[r,c-1] == 0:
                  output_grid[r,c-1] = 1
                  break

        elif first_cell[0] >= 3 and first_cell[1] >= 4:  # Bottom-right quadrant or close.
            # Find an empty neighbor to the left.
            for r, c in obj:
                if c - 1 >= 0 and output_grid[r, c - 1] == 0:
                    output_grid[r, c - 1] = 1
                    break  # Place only one blue pixel per object.



    return output_grid
```

