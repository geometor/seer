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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7D77B1511BA0>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7D77B1511780>

*text:*
Okay, let's analyze the transformation between the input and output grids.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8
      positions: [(1, 1), (2, 1), (2, 2), (4, 4), (4, 5), (5, 4)]
      shape: Two separate L-shapes.
  dimensions: 7x7

output_grid:
  objects:
    - color: 8
      positions: [(1, 1), (2, 1), (2, 2), (4, 4), (4, 5), (5, 4)]
      shape: Two separate L-shapes.
    - color: 1
      positions: [(1,2), (5,3)]
      shape: single pixels.
  dimensions: 7x7
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** In the input grid, we observe two distinct L-shaped objects formed by color 8 (azure). The rest of the grid is filled with color 0 (white).

2.  **Detect Corner Pixel**: The corner of the object is changed.

3.  **Change Color:** The corner is colored to blue (color 1).

4. **No change**: If a pixel is not part of the L-shape objects, don't change it.

**Transformation Rule Summary**

The transformation rule is: Find the upper-left azure pixel of each "L" shape and switch the azure pixel to blue.


*text:*
```python
"""
The transformation rule is: Find the upper-left azure pixel of each "L" shape and switch the azure pixel to blue.
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specific color in the grid.
    Returns a list of corner coordinates.
    """
    objects = []
    visited = set()

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))

        neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for nr, nc in neighbors:
            dfs(nr, nc, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                if len(current_object) > 2:

                  #find corner
                  min_r, min_c = float('inf'), float('inf')
                  for cell_r,cell_c in current_object:
                    if cell_r < min_r:
                      min_r = cell_r
                    if cell_c < min_c:
                      min_c = cell_c

                  objects.append((min_r, min_c))
    return objects

def transform(input_grid):
    """
    Transforms the input grid by finding L-shaped objects of color 8,
    and changing their upper-left pixel color to 1.
    """
    output_grid = np.copy(input_grid)
    l_shapes = find_l_shapes(input_grid, 8)

    # Change the color of the identified corners
    for r, c in l_shapes:
        output_grid[r, c] = 1

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7D77B1512B90>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7D77B15125C0>

*text:*
Okay, let's analyze the second example provided.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8
      positions: [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5,4), (6,4), (6,5)]
      shape: Three separate L-shapes (or mirrored L in one case).
  dimensions: 7x7

output_grid:
  objects:
    - color: 8
      positions:  [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5,4), (6,4), (6,5)]
      shape: Three separate L-shapes.
    - color: 1
      positions: [(1,4), (2,3), (5,3)]
      shape: single pixels.
  dimensions: 7x7
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** The input grid contains three L-shaped objects (two regular L-shapes, and one which could be considered a mirrored-L shape, but all consisting of adjacent pixels of color 8).

2.  **Detect Corner Pixel:** The corner of each object is changed.  Specifically, it's the "inner" corner where the two legs of the L meet at a right angle.

3.  **Change Color:** The identified corner pixel of each L-shape is changed to blue (color 1).

4.  **No change:** If a pixel is not the corner of the identified L-shape objects, its color is unchanged.

**Transformation Rule Summary**

The transformation rule is: Find the inner corner pixel of each L-shaped azure (color 8) object and change its color to blue (color 1).

The previous python code I wrote looked for the upper left corner. The correct implementation should look for all corners.

```python
import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specific color in the grid.
    Returns a list of corner coordinates.
    """
    objects = []
    visited = set()

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))

        neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for nr, nc in neighbors:
            dfs(nr, nc, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                if len(current_object) >= 3: #L shapes have at least 3 pixels
                    # Find the corner
                    rows, cols = zip(*current_object)
                    # Count occurrences of each row and col
                    row_counts = {}
                    col_counts = {}

                    for row in rows:
                        row_counts[row] = row_counts.get(row, 0) + 1
                    for col in cols:
                        col_counts[col] = col_counts.get(col, 0) + 1

                    # Corner will have a row and col that occur more than once
                    corner = None
                    for r, c in current_object:
                       if row_counts[r] >1 and col_counts[c] > 1:
                          corner = (r,c)
                          break
                    if corner is not None:
                        objects.append(corner)
    return objects

def transform(input_grid):
    """
    Transforms the input grid by finding L-shaped objects of color 8,
    and changing their corner pixel color to 1.
    """
    output_grid = np.copy(input_grid)
    l_shapes = find_l_shapes(input_grid, 8)

    # Change the color of the identified corners
    for r, c in l_shapes:
        output_grid[r, c] = 1

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
