# 1-3aa6fb7a • 008 • example_2 - CODE

---
```python
"""
The core transformation rule is consistent: one specific azure pixel in each *L-shaped* object is changed to blue. The selection of *which* azure pixel is based on a consistent 'second pixel' rule, but the direction considered for 'second' depends on the orientation of the L shape itself.
"""

import numpy as np

def find_objects(grid):
    """
    Identifies distinct objects in the grid.
    Returns a list of objects, where each object is a list of (row, col) coordinates.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] == 0:
            return
        visited.add((r, c))
        current_object.append((r, c))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(r + dr, c + dc, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0 and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    One azure pixel changes to blue in each L-shaped object.
    The specific pixel depends on the L-shape's orientation.
    """
    output_grid = np.copy(input_grid)
    objects = find_objects(input_grid)

    for obj in objects:
        if len(obj) == 3:  # Consider only L-shaped objects (3 pixels)
            # Different sorting strategies based on L-shape orientation
            sorted_obj_top_right = sorted(obj, key=lambda x: (-x[0], x[1])) # Top-right to bottom-left
            sorted_obj_vertical = sorted(obj, key=lambda x: x[0])         # Top to bottom
            sorted_obj_horizontal = sorted(obj, key=lambda x: x[1])   #left to right
            sorted_obj_rev_horizontal = sorted(obj, key=lambda x: -x[1])


            # Try different orientations and select the second pixel accordingly
            if all(sorted_obj_top_right[i][0] <= sorted_obj_top_right[i+1][0] and sorted_obj_top_right[i][1] >= sorted_obj_top_right[i+1][1] for i in range(len(sorted_obj_top_right)-1)):
              r, c = sorted_obj_top_right[1]
              output_grid[r,c] = 1
            elif all(sorted_obj_vertical[i][1] == sorted_obj_vertical[0][1] for i in range(1,len(sorted_obj_vertical))):
                r, c = sorted_obj_vertical[1] #second pixel from top to bottom
                output_grid[r, c] = 1
            elif all(sorted_obj_rev_horizontal[i][0] == sorted_obj_rev_horizontal[0][0] for i in range(1, len(sorted_obj_rev_horizontal))):
                r, c = sorted_obj_rev_horizontal[1]
                output_grid[r, c] = 1

            elif all(sorted_obj_horizontal[i][0] == sorted_obj_horizontal[0][0] for i in range(1, len(sorted_obj_horizontal))):
                r,c = sorted_obj_horizontal[1]
                output_grid[r,c] = 1

    return output_grid
```

