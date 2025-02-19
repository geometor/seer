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

<PIL.Image.Image image mode=RGB size=448x448 at 0x754BCA23AE00>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x754BCA23B310>
Okay, I'm ready to analyze the transformation between the input and output grids. Here's my breakdown:

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      positions: [(1, 1), (2, 1), (2, 2), (3, 4), (3, 5), (4, 5)]
      shape: "Two separate L-shaped structures, one mirrored."
  dimensions: [7, 7]

output_grid:
  objects:
    - color: 8 (azure)
      positions: [(1, 1), (2, 1), (2, 2), (3, 4), (3, 5), (4, 5)]
      shape: "Two separate L-shaped structures, one mirrored."
    - color: 1 (blue)
      positions: [(1,2), (4,4)]
      shape: "Two single cells that replace one cell of the color 8 shapes"
  dimensions: [7, 7]
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** In the input grid, we have two distinct L-shaped objects made of azure (color 8) cells.

2.  **Locate Upper-Right and Lower-Left Corners**:
    *   Find the upper-right corner of the top-left L shape.
    *   Find the lower-left corner of the bottom-right L shape.

3.  **Change cell to color 1**:
    *   Replace the upper-right cell with color 1 (blue).
    *   Replace the lower-left cell with color 1 (blue).

4.  **Preserve other parts**: All other cells keep the original colors.

**Transformation Rule Summary**
The input azure L-shapes had their upper-right and lower-left corner pixels changed to blue.

```python
"""
The input azure L-shapes had their upper-right and lower-left corner pixels changed to blue.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous regions of the specified color.
    Returns a list of coordinates.
    """
    objects = []
    visited = set()

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

def find_corners(object_coords):
    """
    Finds the upper-right and lower-left corner of an L-shaped object.
    It receives the object coordinates assuming the object is L-shaped.
    It returns None values if can't define the corners.
    """
    if not object_coords:
      return None, None
    
    # Find min and max row, and min and max col
    min_row = min(r for r, c in object_coords)
    max_row = max(r for r, c in object_coords)
    min_col = min(c for r, c in object_coords)
    max_col = max(c for r, c in object_coords)
    
    # Create a set for faster lookup
    coords_set = set(object_coords)
    
    # Infer corners based on the L shape
    upper_right = None
    lower_left = None

    if (min_row, max_col) in coords_set:
      upper_right = (min_row, max_col)
    if (max_row, min_col) in coords_set:
      lower_left = (max_row, min_col)    

    return upper_right, lower_left

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    The input azure L-shapes had their upper-right and lower-left corner pixels changed to blue.
    """
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find objects of color 8 (azure)
    azure_objects = find_objects(input_grid, 8)
    
    corners = []

    # Find and store the corners of each object in a list
    for obj in azure_objects:
        upper_right, lower_left = find_corners(obj)
        if upper_right:
          corners.append(upper_right)
        if lower_left:
          corners.append(lower_left)
    
    # Change the identified corner pixels to color 1 (blue)
    for corner in corners:
      output_grid[corner] = 1    

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x754BCA2298D0>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x754BCA228550>
Okay, let's analyze the second example.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      positions: [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5, 4), (6, 4), (6, 3)]
      shape: "Three L-shaped structures, two of them rotated."
  dimensions: [7, 7]

output_grid:
  objects:
    - color: 8 (azure)
      positions:  [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5, 4), (6, 4), (6, 3)]
      shape: "Three L-shaped structures, two of them rotated."
    - color: 1 (blue)
      positions: [(1, 4), (2, 3), (5,3)]
      shape: "Three single cells that replaces one cell of each color 8 shape."
  dimensions: [7, 7]
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** In the input grid, we can find three distinct "L-shaped" objects made of azure (color 8) cells.

2.  **Locate inner corner**:
    * Find the 'inner corner' of each L shape, where it forms the right angle of the "L" shape.

3.  **Change cell to color 1**:
     * Replace the corner cell identified in the previous step of each L-shaped structure by color 1 (blue)

4.  **Preserve all other cells**:

**Transformation Rule Summary**
The 'inner-corner' of each of the three azure L-shapes is changed to blue.

```python
"""
The 'inner-corner' of each of the three azure L-shapes is changed to blue.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous regions of the specified color.
    Returns a list of coordinates.
    """
    objects = []
    visited = set()

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

def find_inner_corner(object_coords):
    """
    Finds the inner corner pixel of the L-shaped figures.
    """

    rows = [r for r, c in object_coords]
    cols = [c for r, c in object_coords]
    
    for r in sorted(rows):
        for c in sorted(cols):
          if (r+1,c) in object_coords and (r,c+1) in object_coords:
              return (r,c)
          if (r-1,c) in object_coords and (r,c+1) in object_coords:
              return (r,c)          
          if (r+1,c) in object_coords and (r,c-1) in object_coords:
              return (r,c)
          if (r-1,c) in object_coords and (r,c-1) in object_coords:
              return (r,c)

    return None

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    The 'inner-corner' of each of the three azure L-shapes is changed to blue.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    corners = []
    for obj in azure_objects:
      inner_corner = find_inner_corner(obj)
      if inner_corner:
          corners.append(inner_corner)
    
    for corner in corners:
      output_grid[corner]=1

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
