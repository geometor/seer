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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7137F1A15FC0>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7137F1A16E30>

*text:*
Okay, let's analyze the transformation between the input and output grids.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      positions: [(1,1), (2,1), (2,2), (3,4), (3,5), (4,5)]
      shape: Two separate L-shaped objects (one mirrored)
      size: Each L-shape consists of 3 cells.

output_grid:
  objects:
    - color: 8 (azure)
      positions: [(1,1), (2,1), (2,2), (3,4), (3,5), (4,5)]
      shape: Two L-shaped objects
      size: Each L-shape has size 3
    - color: 1 (blue)
      positions: [(1,2), (4,4)]
      shape: single cells.
      size: 1
```

**Natural Language Program: Step-by-step Transformation**

1.  **Identify Objects:** In the input grid, we can identify two distinct L-shaped objects made of color 8 (azure).

2.  **Locate Replacement Points:** Observe that the "internal corner" or "elbow" of the L shapes (azure color).

3. **Color Insertion**: Change the color of the corner in each L-shape object from azure (8) to color blue (1).

4. **No change otherwise**: All other cells are unchanged.

**Transformation Rule in Natural Language**

The transformation identifies all the azure (8) colored L-shaped objects (made of 3 cells of color 8) in the input grid. Then, changes to blue (1) the internal corner of those L-shaped objects.


*text:*
```python
"""
The transformation identifies all the azure (8) colored L-shaped objects (made of 3 cells of color 8) in the input grid. Then, changes to blue (1) the internal corner of those L-shaped objects.
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specific color in the grid.
    Returns a list of (row, col) tuples representing the "corner" of each L-shape.
    """
    rows, cols = grid.shape
    corners = []

    for r in range(rows - 1):
        for c in range(cols - 1):
            # Check for L shape (normal and rotations)
            if grid[r, c] == color:
                # normal L
                if grid[r + 1, c] == color and grid[r, c + 1] == color:
                    corners.append((r, c))
                # rotated 90
                if grid[r, c+1] == color and grid[r+1, c+1] == color:
                    corners.append((r,c+1))
                # rotated 180
                if grid[r+1, c] == color and grid[r + 1, c + 1] == color:
                    corners.append((r+1,c))
                # rotated -90
                if grid[r,c] == color and grid[r+1,c-1] == color:
                    corners.append((r,c))
            # mirrored L
            if grid[r,c] == color:
                if grid[r+1,c] == color and grid[r,c-1] == color:
                    corners.append((r,c))

    return corners

def transform(input_grid):
    """
    Transforms the input grid by identifying L-shaped objects of color 8,
    and changing the color of their internal corner to 1.
    """
    output_grid = np.copy(input_grid)
    l_corners = find_l_shapes(output_grid, 8)

    # Change the color of the identified corners
    for r, c in l_corners:
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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7137F1A16860>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7137F1A17100>

*text:*
Okay, let's analyze the second example of the transformation.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      positions: [(0,4), (0,5), (1,5), (2,2), (3,2), (3,3), (5,4), (6,3),(6,4)]
      shape: Three separate L-shaped objects
      size: Each L-shape consists of 3 cells.

output_grid:
  objects:
    - color: 8 (azure)
      positions:  [(0,4), (0,5), (1,5), (2,2), (3,2), (3,3), (5,4), (6,3),(6,4)]
      shape: Three L-shaped objects
      size: Each L-shape has size 3
    - color: 1 (blue)
      positions: [(1,4), (2,3), (5,3)]
      shape: single cells.
      size: 1
```

**Natural Language Program: Step-by-step Transformation**

1.  **Identify Objects:** The input grid contains three distinct L-shaped objects of color 8 (azure).

2.  **Locate Replacement Points:** The "internal corner" of each L-shape is targeted for modification.

3.  **Color Insertion**: Change the color of each corner from 8 (azure) to 1 (blue).

4. **No change otherwise**: All other cells are unchanged.

**Transformation Rule in Natural Language**

The transformation rule is identical to the previous example. It identifies azure (8) colored L-shaped objects (of 3 cells) and changes the color of their internal corner cell to blue (1).

The Python code provided previously should be correct because this rule generalizes across both examples.

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
