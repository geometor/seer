# 1-3aa6fb7a • 003 • example_2 - NLP

---

**input**
```
0 0 0 0 0 0 0
0 8 0 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=448x448 at 0x7AB4D7C1AD10>

**output**
```
0 0 0 0 0 0 0
0 8 1 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=448x448 at 0x7AB4D7C1BA30>

*text:*
Okay, let's analyze the transformation between the input and output grids.

**YAML Description**

```yaml
input_grid:
  objects:
    - color: 8
      positions: [(1, 1), (2, 1), (2, 2), (4, 4), (4, 5), (5, 4)]
      shape: "Two separate 2x1 vertical shapes and one L shape"
  size: (7,7)

output_grid:
  objects:
    - color: 8
      positions: [(1, 1), (2, 1), (2, 2), (4, 4), (4, 5), (5, 4)]
      shape: "Two separate 2x1 vertical shapes and one L shape"
    - color: 1
      positions: [(1,2), (5,3)]
      shape: "Two, 1x1 isolated pixels"
  size: (7,7)
```

**Natural Language Program**

Here's a step-by-step description of the transformation rule, focusing on objects, predicates, and actions:

1.  **Identify Objects:** In the input grid, we can observe azure (color 8) objects.

2.  **Detect Azure to Blue Changes**: Some of the azure pixels change to blue pixels (color 1).

3. **Determine Rule**: The rule for changing color is: the top-right corner pixel, when the object looks like an 'L', changes to blue (color 1).

4. **Apply transformation**:
    *   In the first object, the top-right corner is at (1,2) changes from 8 to 1.
    *   In the second object, the top-right corner is at (5,3), relative to the top-left corner, changes from 8 to 1.

**Summary**

The transformation identifies "L"-shaped azure (8) objects and change to blue (color 1) its upper-right corner.


*text:*
```python
"""
The transformation identifies "L"-shaped azure (8) objects and changes to blue (color 1) its upper-right corner.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def is_valid(x, y):
        return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]

    def dfs(x, y, current_object):
        if not is_valid(x, y) or visited[x, y] or grid[x, y] != color:
            return
        visited[x, y] = True
        current_object.append((x, y))
        dfs(x + 1, y, current_object)
        dfs(x - 1, y, current_object)
        dfs(x, y + 1, current_object)
        dfs(x, y - 1, current_object)

    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x, y] == color and not visited[x, y]:
                current_object = []
                dfs(x, y, current_object)
                objects.append(current_object)
    return objects

def is_l_shape(object_coords):
    if len(object_coords) != 3:
        return False, None
    
    xs = [coord[0] for coord in object_coords]
    ys = [coord[1] for coord in object_coords]

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    
    if max_x - min_x > 1 or max_y - min_y > 1:
        return False, None

    if len(set(xs)) == 2 and len(set(ys)) == 2:
        #find top-left corner
        top_left_x = min_x
        top_left_y = min_y

        # find top-right corner
        xs.sort()
        ys.sort()
      
        if (xs[0] == xs[1] and ys[1] == ys[2]) :
          top_right_corner = (xs[0],ys[2])
          return True, top_right_corner
        elif (ys[0] == ys[1] and xs[1] == xs[2]):
          top_right_corner = (xs[2], ys[0])
          return True, top_right_corner
        else:
           return False, None

    return False, None

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    # find azure objects
    azure_objects = find_objects(input_grid, 8)

    # change output pixels
    for obj in azure_objects:
        is_L, top_right_corner = is_l_shape(obj)
        if is_L:
            output_grid[top_right_corner] = 1

    return output_grid
```

**input**
```
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 8 0 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 0 8 0 0
0 0 0 8 8 0 0
```

<PIL.Image.Image image mode=RGB size=448x448 at 0x7AB4D7C1A7D0>

**output**
```
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 8 1 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 1 8 0 0
0 0 0 8 8 0 0
```

<PIL.Image.Image image mode=RGB size=448x448 at 0x7AB4D7C1A290>
**Instructions**

- Describe in natural language the step-by-step transformation observed between the input and output grids.
- Focus on identifying objects, their properties (predicates), and the actions performed on them.
- Be as clear and concise as possible, providing a complete description of the transformation rule.
