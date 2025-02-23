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

<PIL.Image.Image image mode=RGB size=448x448 at 0x77C389A2CFD0>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x77C389A2F4C0>
Okay, let's analyze the transformation between the input and output grids.

**YAML Block Summary**

```yaml
observations:
  input_grid:
    objects:
      - color: 8
        shape: irregular
        positions: [[1,1], [2,1], [2,2], [4,4], [4,5], [5,4]]
    size: [7, 7]
  output_grid:
    objects:
      - color: 8
        shape: irregular
        positions: [[1,1], [2,1], [2,2], [4,4], [4,5], [5,4]]
      - color: 1
        shape: single_cell
        positions: [[1,2], [5,4]]
    size: [7, 7]
```

**Natural Language Program**

Here's a step-by-step description of the transformation:

1.  **Identify Objects:** In the input grid, we have several objects of color `8` (azure). There are no objects of color different that `0` or `8`.

2.  **Preserve Some, Change Some:**
    The object `8` remains at the same positions, there are 2 pixels of color `8` that changes to color `1`.
    The color of two individual `8` cells are changed to `1` (blue).
    The changed `8` are at positions next to color `8`.

3. **Identify Changing Cells Position:** The cells that are changed are:
    -   The single azure cell in the top left object, adjacent to another azure cell.
    -   One azure cell in the bottom rigth object, adjacent to another azure cell.

**Transformation Rule (In Natural Language)**

The rule can be summarized as follows:

Locate all of `8` colored pixels that forms a group (at least 2). For each group, find the pixel that have another pixel in the group adjacent to it. For all this cases, change color `8` by color `1`. Keep the rest of the grid equal.


```python
"""
Locate all of `8` colored pixels that forms a group (at least 2). For each group, find the pixel that have another pixel in the group adjacent to it. For all this cases, change color `8` by color `1`. Keep the rest of the grid equal.
"""

import numpy as np

def get_neighbors(grid, r, c):
    """
    Returns a list of valid neighbor coordinates for a given cell.
    """
    rows, cols = grid.shape
    neighbors = []
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors.append((nr, nc))
    return neighbors

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Change the color of '8' cells to '1' if they are part of an '8' cluster and next to others '8'.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through the grid to find the position of '8'
    for r in range(rows):
        for c in range(cols):
           if output_grid[r,c]== 8:
                neighbors = get_neighbors(output_grid,r,c)
                for nr,nc in neighbors:
                    if output_grid[nr,nc]==8:
                        output_grid[r,c] = 1
                        break

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x77C389A25B70>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x77C389A24850>
Okay, let's analyze the transformation between the input and output grids in this second example.

**YAML Block Summary**

```yaml
observations:
  input_grid:
    objects:
      - color: 8
        shape: irregular
        positions: [[0, 4], [0, 5], [1, 5], [2, 2], [3, 2], [3, 3], [5, 4], [6, 3], [6, 4]]
    size: [7, 7]
  output_grid:
    objects:
      - color: 8
        shape: irregular
        positions: [[0, 4], [0, 5], [1, 5], [2, 2], [3, 2], [3, 3], [5, 4], [6, 3], [6, 4]]
      - color: 1
        shape: single_cell
        positions: [[1, 4], [2, 3], [5,3]]
    size: [7, 7]
```

**Natural Language Program**

Here's a step-by-step description of the transformation:

1.  **Identify Objects:** In the input grid, we have several objects of color `8` (azure).

2.  **Preserve Some, Change Some:**
    Most of azure color `8` remains at the same positions.
    Some pixels of color `8` changes to color `1`.
    The changed `8` are at positions next to color `8`.

3. **Identify Changing Cells Position:** The cells that are changed are:
    -   The single azure cell in the top object, adjacent to another azure cell.
    -   One azure cell in the center object, adjacent to another azure cell.
    -   One azure cell in the bootom object, adjacent to another azure cell.

**Transformation Rule (In Natural Language)**

The rule can be summarized as follows:

Locate all of `8` colored pixels that forms a group (at least 2). For each group, find the pixel that have another pixel in the group adjacent to it. For all this cases, change color `8` by color `1`. Keep the rest of the grid equal.

This program and the Python code are the same that the previous case.

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
