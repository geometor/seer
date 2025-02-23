# db93a21d • 010 • refine_coder

---
```python
"""
1.  **Identify Maroon Rectangles:** Find all contiguous regions of color 9 (maroon) and determine their bounding boxes.

2.  **Categorize White Areas:** Divide the white (0) areas into regions based on proximity to maroon rectangles:
    *   Areas directly above and to the left of *left-most* maroon rectangles.
    *   Areas above and to the left of *right-most* maroon rectangle, bounded by the edge of the grid.
    *   Areas that are not directly above and left of any maroon rectangles.

3.  **Fill Green:** Fill the area categorized as being above and to the left of a left-most maroon rectangle with green (3), up to white cells or other colors.

4.  **Fill Blue:** Fill the areas categorized as being above and to the left of the right-most maroon rectangle with blue (1), up to the edges of the grid.

5.  **Remaining Areas:** Leave all other cells unchanged.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, current_object):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
            return

        visited[row, col] = True
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                current_object = []
                dfs(row, col, current_object)
                if current_object:
                    objects.append(current_object)
    return objects

def get_bounding_box(obj):
    min_row = min(p[0] for p in obj)
    max_row = max(p[0] for p in obj)
    min_col = min(p[1] for p in obj)
    max_col = max(p[1] for p in obj)
    return min_row, max_row, min_col, max_col

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    maroon_objects = find_objects(input_grid, 9)

    # Find left-most and right-most maroon objects
    if maroon_objects:
        leftmost_object = min(maroon_objects, key=lambda obj: get_bounding_box(obj)[2])
        rightmost_object = max(maroon_objects, key=lambda obj: get_bounding_box(obj)[3])


    # Fill Green above and left of leftmost maroon object(s)
        min_row, _, min_col, _ = get_bounding_box(leftmost_object)
        for r in range(min_row):
            for c in range(min_col):
                if output_grid[r, c] == 0: # Fill only white cells
                     output_grid[r,c] = 3

    # Fill Blue above rightmost object
    if len(maroon_objects) >1:
        min_row, _, min_col, _ = get_bounding_box(rightmost_object)
        for r in range(min_row):
           for c in range(input_grid.shape[1]):
               if output_grid[r,c] == 0:
                   output_grid[r,c] = 1
    return output_grid
```
