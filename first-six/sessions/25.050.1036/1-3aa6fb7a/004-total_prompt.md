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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7C886F63E080>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7C886F63E8F0>
Okay, let's analyze the transformation between the input and output grids.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      positions: [(1, 1), (2, 1), (2, 2), (4, 4), (4, 5), (5,4)]
      shape: Two separate L-shapes. One in the top-left, and one in the bottom-right
  dimensions: 7x7

output_grid:
  objects:
    - color: 8 (azure)
      positions:  [(1, 1), (2, 1), (2, 2), (4, 4), (4, 5), (5,4)]
      shape: Two separate L-shapes. One in the top-left, and one in the bottom-right
    - color: 1 (blue)
      positions: [(1,2), (5,5)]
      shape: single cells
  dimensions: 7x7
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Azure Objects:** Locate all azure (color 8) objects within the input grid. In this case, we have two distinct L-shaped azure objects.

2.  **Identify Single Azure cells action**:
    *   Locate the uppermost, and then leftmost, azure (8) colored cell of the top L-shaped azure object in the top left corner of the grid.
    *   Locate the leftmost, and then uppermost, azure (8) colored cell of the bottom L-shaped azure object in the bottom right corner of the grid.

3.  **Change Color:** Change color to blue (1) of each of the two azure (8) colored cells identified.

4. **Leave the Rest:** Do nothing to all the rest of the azure and other cells.

In essence, the rule identifies the two azure L-shaped objects and paints the uppermost-leftmost cell blue of the top L-shaped object and the leftmost-uppermost blue of the bottom one.

```python
"""
The transformation rule identifies two azure L-shaped objects and paints the uppermost-leftmost cell blue of the top L-shaped object and the leftmost-uppermost blue of the bottom one.
"""

import numpy as np

def get_objects(grid, color):
    """
    Finds objects of a specific color in the grid.

    Args:
        grid: The input grid.
        color: The color to search for.

    Returns:
        A list of lists, where each inner list contains the coordinates of
        contiguous cells of the specified color.
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
    """
    Transforms the input grid according to the rule.
    """
    output_grid = input_grid.copy()
    azure_objects = get_objects(input_grid, 8)

    # change color of uppermost-leftmost azure cell of top object
    if len(azure_objects) >= 1:
      top_object = min(azure_objects, key=lambda obj: (min(r for r, c in obj), min(c for r, c in obj)))
      top_left_cell = min(top_object, key=lambda cell: (cell[0], cell[1]))
      output_grid[top_left_cell[0], top_left_cell[1]] = 1

    # change color of leftmost-uppermost azure cell of bottom object
    if len(azure_objects) >= 2:
      # find bottom-right object by minimum row and then minimum col
      bottom_object = max(azure_objects, key=lambda obj: (min(r for r, c in obj), min(c for r,c in obj)))
      bottom_left_cell = min(bottom_object, key=lambda cell: (cell[0], cell[1]))
      output_grid[bottom_left_cell[0],bottom_left_cell[1]] = 1
    
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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7C886F61C550>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7C886F61C5E0>
Okay, let's analyze the second example.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      positions: [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5, 4), (6, 3), (6, 4)]
      shape: Three separate objects. One in the top-right, one in the center-left, and the last one at the bottom.
  dimensions: 7x7

output_grid:
  objects:
    - color: 8 (azure)
      positions:  [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5, 4), (6, 3), (6, 4)]
      shape: Three separate objects. One in the top-right, one in the center-left, and the last one at the bottom.
    - color: 1 (blue)
      positions: [(1,4), (2, 3), (5,3)]
      shape: single cells
  dimensions: 7x7
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Azure Objects:** Locate all azure (color 8) objects within the input grid. In this case, we have three distinct azure objects.

2.  **Identify Single Azure cells action**:
    *   Locate the uppermost, and then leftmost, azure (8) colored cell of the top azure object.
    *   Locate the leftmost, and then uppermost, azure (8) colored cell of the center azure object.
     *   Locate the leftmost, and then uppermost, azure (8) colored cell of the bottom azure object.

3.  **Change Color:** Change color to blue (1) of each of the three azure (8) colored cells identified.

4.  **Leave the Rest:** Do nothing to the rest of the azure and other cells.

The code written previously will work on this case too.

```python
"""
The transformation rule identifies all azure objects and paints the uppermost-leftmost cell blue of the top object, the leftmost-uppermost blue of the center object, and the leftmost-uppermost cell blue of the bottom one.
"""

import numpy as np

def get_objects(grid, color):
    """
    Finds objects of a specific color in the grid.

    Args:
        grid: The input grid.
        color: The color to search for.

    Returns:
        A list of lists, where each inner list contains the coordinates of
        contiguous cells of the specified color.
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
    """
    Transforms the input grid according to the rule.
    """
    output_grid = input_grid.copy()
    azure_objects = get_objects(input_grid, 8)

    # change color of uppermost-leftmost azure cell of top object
    if len(azure_objects) >= 1:
      top_object = min(azure_objects, key=lambda obj: (min(r for r, c in obj), min(c for r, c in obj)))
      top_left_cell = min(top_object, key=lambda cell: (cell[0], cell[1]))
      output_grid[top_left_cell[0], top_left_cell[1]] = 1

    # change color of leftmost-uppermost azure cell of bottom object
    if len(azure_objects) >= 2:
      # find bottom-right object by minimum row and then minimum col
        objects_ordered_by_y = sorted(azure_objects, key=lambda obj: (min(r for r, c in obj), min(c for r,c in obj)))

        for i in range(1,len(objects_ordered_by_y)):
          bottom_left_cell = min(objects_ordered_by_y[i], key=lambda cell: (cell[0], cell[1]))
          output_grid[bottom_left_cell[0],bottom_left_cell[1]] = 1
    
    return output_grid
```

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
