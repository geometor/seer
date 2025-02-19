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

<PIL.Image.Image image mode=RGB size=448x448 at 0x796FCD430E80>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x796FCD433220>
Okay, let's analyze the transformation between the input and output grids.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      shape: L-shape (rotated)
      positions: [(1,1), (2,1), (2,2)]
    - color: 8 (azure)
      shape: L-shape
      positions: [(3,4), (3,5), (4,5)]
  dimensions: (7, 7)

output_grid:
  objects:
    - color: 8 (azure)
      shape: L-shape (rotated)
      positions: [(1,1), (2,1), (2,2)]
     - color: 1 (blue)
       shape: single cell
       positions: [(1,2)]
    - color: 8 (azure)
      shape: L-shape
      positions: [(3,4), (3,5), (4,5)]
    - color: 1 (blue)
      shape: single cell
      positions: [(4,4)]
  dimensions: (7, 7)
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** In the input grid, we can identify two distinct L-shaped objects of color 8 (azure).

2.  **Object Persistence:** the two azure L-shaped objects exist in the output grid.

3.  **Detect Change:** The cells to the immediate right of the top-left corner element of each original L-shape are changed from color 0 (background) to color 1 (blue).

**Transformation Rule (In Natural Language)**

The transformation preserves the azure L-shaped objects. The transformation paints blue the cells at the right of the top-left element of each azure L-shape.


```python
"""
The transformation preserves the azure L-shaped objects. The transformation paints blue the cells at the right of the top-left element of each azure L-shape.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, current_object):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def get_top_left(object_coords):
     # Sort by row, then by column, and take the first element
    return sorted(object_coords, key=lambda x: (x[0], x[1]))[0]
    

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Preserves azure L-shaped objects and paints blue the cell to the right
    of the top-left corner of each L-shape.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    # Iterate through each azure object
    for obj in azure_objects:
        # find top-left element
        top_left = get_top_left(obj)

        # Paint the cell to the right of the top-left corner blue
        paint_row = top_left[0]
        paint_col = top_left[1] + 1

        if 0 <= paint_row < output_grid.shape[0] and 0 <= paint_col < output_grid.shape[1]:
             output_grid[paint_row, paint_col] = 1

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x796FCD433100>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x796FCD433880>
Okay, let's analyze the second example provided.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      shape: L-shape
      positions: [(0,4), (0,5), (1,5)]
    - color: 8 (azure)
      shape: L-shape (rotated)
      positions: [(2,2), (3,2), (3,3)]
    - color: 8 (azure)
      shape: L-shape (rotated)
      positions: [ (5,4), (6,4), (6,3)]
  dimensions: (7, 7)

output_grid:
  objects:
    - color: 8 (azure)
      shape: L-shape
      positions: [(0,4), (0,5), (1,5)]
    - color: 1 (blue)
       shape: single cell
       positions: [(1,4)]
    - color: 8 (azure)
      shape: L-shape (rotated)
      positions: [(2,2), (3,2), (3,3)]
    - color: 1 (blue)
      shape: single cell
      positions:  [(2,3)]
    - color: 8 (azure)
      shape: L-shape (rotated)
      positions: [ (5,4), (6,4), (6,3)]
      - color: 1 (blue)
        shape: single cell
        positions: [(5,3)]
  dimensions: (7, 7)
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** In the input grid, we identify three distinct L-shaped objects of color 8 (azure).

2.  **Object Persistence:** All azure L-shaped objects are still present in the output grid, and maintain their original shape and position.

3. **Detect change:** We can see a change of color from color 0 to color 1 on the right of the top-left element of each azure object.

**Transformation Rule (In Natural Language)**

The transformation preserves the azure L-shaped objects. The transformation paints blue the cell immediately to the right of the top-left corner element of each azure L-shape.

The provided Python code and natural language description correctly capture the essence of this transformation. The `find_objects` function identifies azure objects, `get_top_left` extracts each top-left element, and the `transform` function applies the color change to the specified adjacent cell.

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
