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

<PIL.Image.Image image mode=RGB size=448x448 at 0x786650B0A320>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x786650B0A890>
Okay, let's analyze the transformation between the input and output grids.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      positions: [(1, 1), (2, 1), (2, 2), (4, 4), (4, 5), (5, 4)]
      shape: Two separate 2x1 and 1x2 azure-colored components and an isolated azure pixel.

output_grid:
  objects:
    - color: 8 (azure)
      positions: [(1, 1), (2, 1), (2, 2), (4, 4), (4, 5), (5, 4)]
      shape: Identical to input, Two separate 2x1 and 1x2 azure-colored components and an isolated azure pixel.
    - color: 1 (blue)
      positions: [(1,2), (5,5)]
      shape: single pixel
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Azure Objects:** In the input grid, we have two distinct shapes components made of azure (color 8) and a single azure pixel. The first is a vertical 2x1 rectangle at the upper left and a horizontal 1x2 shape. The isolated azure pixel is near the bottom right.

2.  **Introduce Blue Pixel**: We pain blue (color 1) the pixel on the right of any azure (color 8) pixel which has no pixel on its right.

**Transformation Rule**
The transformation consists in painting in blue (color 1) the pixels at the right of those azure pixels (color 8) at the right edge of azure shapes.

```python
"""
The transformation consists in painting in blue (color 1) the pixels at the right of those azure pixels (color 8) at the right edge of azure shapes.
"""

import numpy as np

def get_objects(grid):
    """
    Identify contiguous regions of the same color as separate objects.
    """
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, color, obj):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        obj.append((row, col))
        dfs(row + 1, col, color, obj)
        dfs(row - 1, col, color, obj)
        dfs(row, col + 1, color, obj)
        dfs(row, col - 1, color, obj)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col] and grid[row,col]!=0:
                color = grid[row, col]
                obj = []
                dfs(row, col, color, obj)
                objects.append((color, obj))
    return objects
def transform(input_grid):
   """
    Transforms the input grid according to the rule: 
    Paint in blue (color 1) the pixels at the right of those azure pixels (color 8) at the right edge of azure shapes.
   """
   output_grid = np.copy(input_grid)
   objects = get_objects(input_grid)

   # Iterate and paint
   for color, obj in objects:
    if color == 8:
      for row,col in obj:
        if col+1 < input_grid.shape[1] and input_grid[row,col+1] == 0:
            is_right_edge = True
            for r,c in obj:
              if r==row and c == col+1:
                is_right_edge=False
                break
            if is_right_edge:
              output_grid[row,col+1] = 1

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x786650B0AA40>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x786650B0B0A0>
Okay, let's analyze the second example.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      positions: [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5, 4), (6, 3), (6, 4)]
      shape: Several azure components of various shapes and sizes.

output_grid:
  objects:
    - color: 8 (azure)
      positions: [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5, 4), (6, 3), (6, 4)]
      shape: Identical to the input grid.
    - color: 1 (blue)
      positions: [(1, 4), (2, 3), (5,3)]
      shape: single pixel
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Azure Objects:** The input grid contains multiple azure (color 8) colored pixels, forming various disconnected shapes.

2.  **Introduce Blue Pixel:** For each azure pixel, we check the cell immediately to its right. If that cell is empty (color 0) AND it's not part of azure object, a blue pixel (color 1) is placed in the empty cell.

**Transformation Rule**
The transformation consists in painting in blue (color 1) the pixels at the right of those azure pixels (color 8) at the right edge of azure shapes.

The provided Python code should perform correctly since this logic is the same for both input/output examples.

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
