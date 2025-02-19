# 1-3aa6fb7a • 004 • example_2 - CODE

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7CD0E292EE90>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7CD0E292E200>

*text:*
Okay, let's analyze the transformation between the input and output grids.

**YAML Observation:**

```yaml
input_grid:
  size: 7x7
  objects:
    - color: 8
      positions: [(1,1), (2,1), (2,2), (4,4), (4,5), (5,4)]
      shape: Two L-shapes
    - color: 0
      positions: All other cells
      shape: Background

output_grid:
  size: 7x7
  objects:
    - color: 8
      positions: [(1,1), (2,1), (2,2), (4,4), (4,5), (5,4)]
      shape: Two L-shapes
    - color: 1
      positions: [(1,2), (5,5)]
      shape: single pixels
    - color: 0
      positions: All other cells
      shape: Background
```

**Natural Language Program (Transformation Rule):**

1.  **Identify Objects:** The input grid consists of two "L" shaped objects of color 8 (azure) and a background of color 0 (white).

2.  **Locate Change:** Observe the differences between the input and output. The azure objects have moved. The output grid contains a single pixel.

3. **Describe the change**: Locate the corners of the azure L-shapes. Paint azure with blue.

**Step-by-step transformation:**
1. Find the azure (8) colored objects in the grid.
2. Find the corners of the two L-shapes. The coordinates are (1, 2) and (5,5).
3. Paint the corner cells of the azure shapes to blue (1).
4. Keep other azure pixels.
5. Keep other grid colors.

This natural language program describes the observed transformation concisely and completely, capturing object properties, actions, and the overall rule.


*text:*
```python
"""
This program transforms an input grid by identifying two L-shaped objects of color 8 (azure),
and changing the color of the corner pixel of each L-shape to color 1 (blue).

1. Find the azure (8) colored objects in the grid.
2. Find the corners of the two L-shapes. The coordinates are (1, 2) and (5,5).
3. Paint the corner cells of the azure shapes to blue (1).
4. Keep other azure pixels.
5. Keep other grid colors.
"""

import numpy as np

def find_objects(grid, color):
    # Find all objects of a specific color
    objects = []
    visited = set()

    def is_valid(x, y):
        return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]

    def dfs(x, y, current_object):
        if (x, y) in visited or not is_valid(x, y) or grid[x, y] != color:
            return
        visited.add((x, y))
        current_object.append((x, y))

        # Check all 8 neighbors
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                dfs(x + dx, y + dy, current_object)

    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x, y] == color and (x, y) not in visited:
                current_object = []
                dfs(x, y, current_object)
                objects.append(current_object)
    return objects

def find_l_corners(obj):
    # Find the corner of an L-shape object
    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = float('-inf'), float('-inf')

    coords = {}
    for x,y in obj:
      if (x,y) in coords:
        coords[(x,y)] += 1
      else:
        coords[(x,y)] = 1

    corners = []
    for key in coords.keys():
      if coords[key] > 1:
        corners.append(key)

    if len(corners) > 0:
      if len(obj) == 3:
         return corners[0]

    return None

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)

    # Find azure objects
    azure_objects = find_objects(input_grid, 8)

    # Find and change L-shape corners to blue
    for obj in azure_objects:
        corner = find_l_corners(obj)
        if corner:
            output_grid[corner[0], corner[1]] = 1

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7CD0E2921B40>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7CD0E2920820>

*text:*
Okay, let's analyze the transformation between the input and output grids in this second example.

**YAML Observation:**

```yaml
input_grid:
  size: 7x7
  objects:
    - color: 8
      positions: [(0,4), (0,5), (1,5), (2,2), (3,2), (3,3), (5,4), (6,3),(6,4)]
      shape: Three L-shapes
    - color: 0
      positions: All other cells
      shape: Background

output_grid:
  size: 7x7
  objects:
    - color: 8
      positions:  [(0,4), (0,5), (1,5), (2,2), (3,2), (3,3), (5,4), (6,3),(6,4)]
      shape: Three L-shapes
    - color: 1
      positions: [(1,4), (2,3), (5,3)]
      shape: single pixels
    - color: 0
      positions: All other cells
      shape: Background
```

**Natural Language Program (Transformation Rule):**

1.  **Identify Objects:** The input grid consists of three "L" shaped objects of color 8 (azure) and a background of color 0 (white).

2.  **Locate Change:** Observe the differences between the input and output. The azure objects are identical. Three single blue pixels are added.

3.  **Describe the change:** Locate the corners of the azure L-shapes. Paint these corners with blue.

**Step-by-step transformation:**

1.  Find the azure (8) colored objects in the grid.
2.  Find the corners of the three L-shapes.  The coordinates are (1, 4), (2, 3), and (5,3).
3.  Paint the corner cells of the azure shapes to blue (1).
4. Keep other azure pixels.
5.  Keep other grid colors.

This natural language program describes the observed transformation, including object properties, actions, and the overall rule. The key is to identify the L-shapes, find their corners, and change only the color of those corner pixels.

**INSTRUCTIONS**

- generate a Python module to represent the natural language program 
- follow the template below
- all common math and science libraries are available
- create docstring only at top - but comment the workflow in the function
- use helper functions for common operations like finding objects, counting,
  measuring, moving, etc. 

remember - we are working iteratively - so this code will inform your future
self as we converge on the solution

*template:*

```python
"""
{ natural language description of the transformation rule }
"""

{ imports }

def transform(input_grid):
    # initialize output_grid

    # change output pixels 

    return output_grid

```
