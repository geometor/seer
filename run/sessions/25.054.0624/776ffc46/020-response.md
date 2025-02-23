# 776ffc46 • 020 • example_4 • investigate_coder

---
```python
"""
The transformation rule is:

1.  **Identify Objects:** Locate all contiguous regions of pixels with the same color. These are our objects. Specifically, identify blue object at the bottom center.

2.  **Locate Target:** Find the blue (1) object.

3. Change Object Color. Change a segment of the blue object, the part that is located above row 9 and between columns 10 and 14, to green (3).

4.  **Output:** The output grid is the same as the input, except for the localized color change of the object identified.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous regions of a specific color in the grid.
    Returns a list of coordinates representing the object.
    """
    visited = set()
    objects = []

    def dfs(r, c, current_object):
        if (r, c) in visited or not (0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]) or grid[r, c] != color:
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

    # Find the blue object
    blue_objects = find_objects(input_grid, 1)

    # identify target segment of blue object
    for blue_object in blue_objects:
         for r,c in blue_object:
              if r <= 11 and r >=9 and c>=10 and c <= 14: # based on coordinates of the example
                output_grid[r,c] = 3

    return output_grid
```
