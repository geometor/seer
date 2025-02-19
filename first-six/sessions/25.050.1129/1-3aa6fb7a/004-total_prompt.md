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

<PIL.Image.Image image mode=RGB size=448x448 at 0x79D121213070>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x79D121212CE0>
Okay, let's analyze the transformation between the input and output grids.

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      positions: [(1, 1), (2, 1), (2, 2), (4, 4), (4, 5), (5, 4)]
      shape: Two separate 2x1 and 1x2 azure objects.

output_grid:
  objects:
    - color: 8 (azure)
      positions: [(1, 1), (2, 1), (2, 2), (4, 4), (4, 5), (5, 4)]
      shape: Two separate 2x1 and 1x2 azure objects.
    - color: 1 (blue)
      positions: [(1,2), (5,5)]
      shape: single-pixel.
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Azure Objects:** In the input grid, we have two distinct azure (color 8) objects. One is a 2x1 vertical block on the left, and another is a 1x2 object at the right.

2.  **Detect corner/border:** We find the pixel to the right of the top-most pixel of the first object and replace it with a blue pixel.

3.  **Detect corner/border:** We find the pixel to the left the bottom-most pixel of the second object and replace it with a blue pixel.

4.  **Preserve Other Pixels:** All other pixels, remain unchanged.

In summary, the azure objects are preserved with blue (1) markers identifying corners defined according to the rules.

```python
"""
The transformation preserves two azure (color 8) objects from the input grid to the output grid.
It adds a blue pixel (color 1) to the right of the top-most pixel of the leftmost azure object, and another blue pixel to the left of the bottom-most pixel of the rightmost azure object.
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

    # Sort objects based on their leftmost coordinate
    azure_objects.sort(key=lambda obj: min(c for r, c in obj))

    #process first/leftmost object
    if len(azure_objects) >= 1:
        first_object = azure_objects[0]
        topmost_pixel = min(first_object, key=lambda p: p[0])
        output_grid[topmost_pixel[0], topmost_pixel[1] + 1] = 1

    # Process the second/rightmost object.
    if len(azure_objects) >= 2:
        second_object = azure_objects[1]
        bottommost_pixel = max(second_object, key=lambda p: p[0])
        output_grid[bottommost_pixel[0], bottommost_pixel[1] -1] = 1
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

<PIL.Image.Image image mode=RGB size=448x448 at 0x79D121213EB0>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x79D1212133D0>
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
