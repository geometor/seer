# 1f642eb9 • 006 • example_3 - CODE

---
```python
"""
The 8 object loses one cell. The single cells target the 8 object. Numbers 3 and 6 combine on the sides, while numbers 4 and 7 occupy the upper and lower sides, respectively. Color 2 get the extra cell of 8.
"""

import numpy as np

def find_objects(grid):
    """Finds contiguous regions of the same color."""
    objects = {}
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, color, obj_coords):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1]
                or visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        obj_coords.append((row, col))
        dfs(row + 1, col, color, obj_coords)
        dfs(row - 1, col, color, obj_coords)
        dfs(row, col + 1, color, obj_coords)
        dfs(row, col - 1, color, obj_coords)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col] and grid[row,col] != 0:
                color = grid[row, col]
                obj_coords = []
                dfs(row, col, color, obj_coords)
                if color not in objects:
                    objects[color] = []
                objects[color].append(obj_coords)

    return objects

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = input_grid.copy()

    # Find objects in the input grid
    objects = find_objects(input_grid)

    # Find the '8' object (assuming there's only one)
    eight_object = objects.get(8)[0]  # List of coordinates of the '8' object
    
    # Get top left corner of the eight_object
    eight_object_rows = [coord[0] for coord in eight_object]
    eight_object_cols = [coord[1] for coord in eight_object]
    eight_top_row = min(eight_object_rows)
    eight_left_col = min(eight_object_cols)
    eight_bottom_row = max(eight_object_rows)
    eight_right_col = max(eight_object_cols)

    # Move '4'
    four_coords = objects.get(4)[0][0]
    output_grid[eight_top_row, eight_left_col] = 4

    # Move '6'
    six_coords = objects.get(6)[0][0]
    output_grid[eight_top_row, eight_right_col] = 6
    
    #Move 3
    three_coords = objects.get(3)[0][0]
    output_grid[eight_top_row, eight_left_col -1] = 3

    # Move '2'
    two_coords = objects.get(2)[0][0]
    output_grid[eight_bottom_row, eight_right_col] = 2    

    #Move 7
    seven_coords = objects.get(7)[0][0]
    output_grid[eight_bottom_row, eight_left_col ] = 7
    
    # Move '8'
    output_grid[eight_top_row, eight_left_col+2] = 0

    return output_grid
```

