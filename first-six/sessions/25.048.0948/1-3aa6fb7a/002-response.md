# 1-3aa6fb7a • 002 • Response

---

*text:*

```python
"""
The transformation identifies azure objects and paints the topmost and rightmost with blue color, where those pixels make L shape with others.
"""

import numpy as np

def get_objects(grid, color):
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
    # initialize output_grid
    output_grid = np.copy(input_grid)
    objects = get_objects(input_grid, 8)

    # change output pixels
    for obj in objects:
        #find top most
        top_most = min(obj, key=lambda x: x[0])
        #find right most
        right_most = max(obj, key=lambda x: x[1])

        output_grid[top_most[0], top_most[1]] = 1
        output_grid[right_most[0], right_most[1]] = 1

    return output_grid
```
