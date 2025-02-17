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

<PIL.Image.Image image mode=RGB size=448x448 at 0x755FE810ED70>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x755FE810FB80>

*text:*
Okay, let's analyze the transformation between the input and output grids.

**YAML Observation:**

```yaml
input_grid:
  size: 7x7
  objects:
    - color: 8 (azure)
      positions:
        - (1, 1)
        - (2, 1)
        - (2, 2)
        - (3, 4)
        - (3, 5)
        - (4, 5)
      shape: Two separate L-shaped objects.

output_grid:
  size: 7x7
  objects:
    - color: 8 (azure)
      positions:
        - (1, 1)
        - (2, 1)
        - (2, 2)
        - (3, 4)
        - (3, 5)
        - (4, 5)
      shape: Two separate L-shaped objects.
    - color: 1 (blue)
      positions:
        - (1,2)
        - (4,4)

```

**Natural Language Program (Transformation Rule):**

1.  **Identify Objects:** Locate all azure (color 8) colored objects in the input grid. There are two disconnected L-shaped objects.

2.  **Change Color:** Change single azure cell on the right side and the top of each object to color 1.

3. **Preserve:** All other cells, including the azure objects, stay unchanged.

In Essence: The transformation identifies azure objects and paints the topmost and rightmost with blue color, where those pixels make L shape with others.


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

<PIL.Image.Image image mode=RGB size=448x448 at 0x755FE810F520>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x755FE810E4D0>

*text:*
Okay, let's analyze the second example.

**YAML Observation:**

```yaml
input_grid:
  size: 7x7
  objects:
    - color: 8 (azure)
      positions:
        - (0, 4)
        - (0, 5)
        - (1, 5)
        - (2, 2)
        - (3, 2)
        - (3, 3)
        - (5, 4)
        - (6, 4)
        - (6, 3)
      shape: Three separate L-shaped objects.

output_grid:
  size: 7x7
  objects:
     - color: 8 (azure)
       positions:
        - (0, 4)
        - (0, 5)
        - (1, 5)
        - (2, 2)
        - (3, 2)
        - (3, 3)
        - (5, 4)
        - (6, 4)
        - (6, 3)
       shape: Three separate L-shaped objects.
     - color: 1 (blue)
       positions:
        - (1, 4)
        - (2, 3)
        - (5,3)
```

**Natural Language Program (Transformation Rule):**

1.  **Identify Objects:** Find all azure (color 8) colored objects within the input grid. In this instance, we can discern three distinct L-shaped configurations.

2. **Change Color:** Change single azure cell on the right side and the top of each object to color 1.

3.  **Preservation:** The remaining cells, including the unchanged parts of the azure structures, maintain their original colors.

*Essence:* This transformation processes the input grid by pinpointing each azure object and recoloring particular azure elements at the upper and right boundaries to blue.

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
