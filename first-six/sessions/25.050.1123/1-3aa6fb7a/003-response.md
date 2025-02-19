# 1-3aa6fb7a • 003 • example_2 - NLP

---
Okay, let's analyze the second example provided.

**YAML Description**

```yaml
input_grid:
  objects:
    - color: 8
      positions: [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5,4), (6,4), (6,5)]
      shape: "Three separate L shapes"
  background_color: 0

output_grid:
  objects:
    - color: 8
      positions:  [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5,4), (6,4), (6,5)]
      shape: "Three separate L shapes"
    - color: 1
      positions: [(1, 4), (2, 3), (5,3)]
      shape: "single pixels inside the L shapes"
  background_color: 0
```

**Natural Language Program**

1.  **Identify Objects:** The input grid contains three distinct "L" shaped objects of color 8 (azure).

2.  **Locate Insertion Points:** Similar to the previous example, we look for the "inner corner" of each "L" shape.

3.  **Color Changing:** Within each "L" shape, place a color 1 (blue) pixel at the inner corner of L.

**Step-by-step transformation description**
The input azure L shapes are preserved. Three blue pixels are added inside the azure shapes at locations that depend on the shape orientation.

The python implementation is the same.
```python
"""
The input azure L shapes are preserved. Two blue pixels are added inside the azure shapes,
one cell down and one cell to the right from the top-left pixel of the "L" shape, 
and respectively, one cell up of the bottom-right pixel.
"""

import numpy as np

def find_objects(grid, color):
    # Find contiguous regions of the given color
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

def find_l_shapes(obj):
    #rule to detect 2x2 L shapes from the object
    if len(obj) != 3: return []
    obj.sort()
    if (obj[1][0] == obj[0][0]+1 and obj[1][1] == obj[0][1] and
        obj[2][0] == obj[1][0] and obj[2][1] == obj[1][1]+1) or \
       (obj[1][0] == obj[0][0] and obj[1][1] == obj[0][1]+1 and
        obj[2][0] == obj[1][0]+1 and obj[2][1] == obj[1][1]):
            return obj
    else: return []

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)

    # Find objects of color 8 (azure)
    azure_objects = find_objects(input_grid, 8)
    
    #detect L shapes
    l_shapes = []
    for obj in azure_objects:
      l = find_l_shapes(obj)
      if len(l) > 0: l_shapes.append(l)

    # Place blue (1) pixels inside detected "L" shapes
    for l_shape in l_shapes:
        #get coordinates
        l_shape.sort()
        #check the orientation and set the insertion point
        if l_shape[1][0] > l_shape[0][0]:
          output_grid[l_shape[0][0] + 1, l_shape[0][1] + 1] = 1
        else:
          output_grid[l_shape[2][0] -1, l_shape[2][1]-1] = 1  
    return output_grid
```

