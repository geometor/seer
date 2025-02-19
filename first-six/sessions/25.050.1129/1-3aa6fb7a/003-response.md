# 1-3aa6fb7a • 003 • example_2 - NLP

---
Okay, let's analyze the second example of the transformation.

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      positions: [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5, 4), (6, 3), (6, 4)]
      shape: Three separate azure objects: 2x1, 2x1 and 1x2, 2x1.
output_grid:
  objects:
    - color: 8 (azure)
      positions:  [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5, 4), (6, 3), (6, 4)]
      shape: Three separate azure objects: 2x1, 2x1 and 1x2, 2x1.
    - color: 1 (blue)
      positions: [(1, 4), (2, 3), (5,3)]
      shape: single-pixel.
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Azure Objects:** The input grid has three distinct azure (color 8) objects.

2.  **Detect corner/border (object 1):**  A blue pixel replaces the cell to the left of the top-most pixel of the top, leftmost azure object.

3.  **Detect corner/border (object 2):** A blue pixel replaces the cell to the right of the top-most pixel of the second azure object (middle object).

4. **Detect corner/border (object 3):**  A blue pixel replaces the cell to the left of the top-most pixel of the third azure object.

5.  **Preserve Other Pixels:** All other pixels remain unchanged.

```python
"""
The transformation preserves three azure (color 8) objects from the input grid to the output grid.
It adds a blue pixel (color 1) to mark specific corners on those objects.
"""

import numpy as np

def find_objects(grid, color):
    """Finds objects of a specific color in the grid."""
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        """Depth-first search to find contiguous regions."""
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
    """Transforms the input grid according to the specified rule."""
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    # Sort objects based on their topmost and then leftmost coordinate
    azure_objects.sort(key=lambda obj: (min(r for r, c in obj), min(c for r, c in obj)))

    #process objects
    
    if len(azure_objects) >= 1:
        first_object = azure_objects[0]
        topmost_pixel = min(first_object, key=lambda p: p[0])
        if topmost_pixel[1] > 0: #only if it's possible
          output_grid[topmost_pixel[0], topmost_pixel[1] - 1] = 1

    if len(azure_objects) >= 2:
        second_object = azure_objects[1]
        topmost_pixel = min(second_object, key=lambda p: p[0])
        if topmost_pixel[1]< output_grid.shape[1]-1: #check boundaries
            output_grid[topmost_pixel[0], topmost_pixel[1] + 1] = 1

    if len(azure_objects) >= 3:
        third_object = azure_objects[2]
        topmost_pixel = min(third_object, key=lambda p: p[0])
        if topmost_pixel[1] > 0:
          output_grid[topmost_pixel[0], topmost_pixel[1] -1] = 1
          
    return output_grid
```

