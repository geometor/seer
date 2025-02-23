# 1fad071e • 008 • example_2 • investigate_coder

---
```python
"""
Counts the number of disconnected blue (1) regions in the input grid and constructs a 1xN output grid, 
where N is the count of disconnected regions. Fill the output grid with blue (1) pixels with white (0)
at the end.
"""

import numpy as np

def get_objects(grid, color):
    """
    Finds objects (contiguous regions of the specified color) in a grid.
    """
    objects = []
    visited = set()

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            dfs(r + dr, c + dc, current_object)
        

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    # Find disconnected blue regions.
    blue_objects = get_objects(np.array(input_grid), 1)
    num_blue_regions = len(blue_objects)

    # Construct the output grid.
    output_grid_width = num_blue_regions + 1
    output_grid = np.ones((1, output_grid_width), dtype=int)

    output_grid[0, -1] = 0

    return output_grid.tolist()
```
