# 3-1e0a9b12 • 004 • example_2 - CODE

---

**input**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x79B96C7FA770>

**output**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x79B96C7FB9D0>

*text:*
Okay, let's analyze the transformation from the input grid to the output grid.

**Observations in YAML Format**

```yaml
input_grid:
  size: 4x4
  objects:
    - color: 0 (white)
      count: 10
      positions: Most of the grid
    - color: 4 (yellow)
      count: 2
      positions: (0,1), (2,1)
    - color: 9 (maroon)
      count: 1
      position: (0,3)
    - color: 6 (magenta)
      count: 1
      position: (2,2)
    - color: 1 (blue)
      count: 1
      position: (3,0)

output_grid:
  size: 4x4
  objects:
    - color: 0 (white)
      count: 11
      positions: Most of the grid
    - color: 4 (yellow)
      count: 1
      positions: (3,1)
    - color: 1 (blue)
      count: 1
      position: (3, 0)
    - color: 6 (magenta)
      count: 1
      position: (3, 2)
    - color: 9 (maroon)
      count: 1
      position: (3, 3)
```

**Natural Language Program Description**

Here's a step-by-step description of the transformation:

1.  **Identify non-white cells:** Locate all cells in the input grid that do *not* have the color white (0).

2.  **Move to Bottom Row, Preserve Order**: Move a copy of all the non-white cells to the last row of the grid. The order of non-white cells in the input is maintained in the output: The colored cells are arranged in the last row, sorted from left to right, following the column major order in the input.

3. **Remove**: Remove cells that have the same value of an adjacent cell (left, right, up, down).

**Inferred Transformation Rule Summary**

The transformation rule can be summarized as follows:
The colored objects from the input are copied and consolidated/moved into the bottom row of the output grid, maintaining their original order, and removing equal adjacent colored cells. The remaining cells are set to white (0).


*text:*
```python
"""
The transformation rule can be summarized as follows:
The colored objects from the input are copied and consolidated/moved into the bottom row of the output grid, maintaining their original order, and removing equal adjacent colored cells. The remaining cells are set to white (0).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule:
    Colored cells are moved to the last row, maintaining their order,
    and the rest of the grid is filled with white (0).
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # 1. Identify non-white cells and their original order.
    non_white_cells = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                non_white_cells.append((input_grid[r, c], r, c)) # Store color and original position

    # 2. Sort non-white cells to preserve the column-major order in the bottom row
    non_white_cells_sorted = sorted(non_white_cells, key=lambda x: (x[1], x[2]))
     
    # 3. Place the sorted non-white cells in the last row of the output grid.
    last_row_index = 0
    for cell in non_white_cells_sorted:
        output_grid[rows - 1, last_row_index] = cell[0]
        last_row_index += 1

    return output_grid.tolist()
```

**input**
```
0 0 0 0 0 9
0 0 0 8 0 0
0 0 0 0 0 0
4 0 0 0 0 0
4 0 7 8 0 0
4 0 7 0 0 0
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x79B96C7FBEB0>

**output**
```
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
4 0 0 0 0 0
4 0 7 8 0 0
4 0 7 8 0 9
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x79B96C7FA9E0>

*text:*
Okay, let's analyze the transformation from the input grid to the output grid in this second example.

**Observations in YAML Format**

```yaml
input_grid:
  size: 6x6
  objects:
    - color: 0 (white)
      count: 28
      positions: Most of the grid
    - color: 9 (maroon)
      count: 1
      position: (0,5)
    - color: 8 (azure)
      count: 2
      positions: (1,3), (4,3)
    - color: 4 (yellow)
      count: 3
      positions: (3,0), (4,0), (5,0)
    - color: 7 (orange)
      count: 2
      positions: (4,2), (5,2)

output_grid:
  size: 6x6
  objects:
    - color: 0 (white)
      count: 28
      positions: Most of the grid
    - color: 4 (yellow)
      count: 3
      positions: (3,0), (4,0), (5,0)
    - color: 7 (orange)
      count: 2
      positions: (4,2), (5,2)
   - color: 8 (azure)
      count: 1
      positions: (5,3)
    - color: 9 (maroon)
      count: 1
      position: (5,5)
```

**Natural Language Program Description**

Here's a step-by-step description of the transformation:

1.  **Identify non-white cells:** Locate all cells in the input grid that do *not* have the color white (0).

2.  **Move to Bottom Row, Preserve Order**: Move a copy of all the non-white cells to the last row of the grid. The order of non-white cells in the input is maintained in the output. The colored cells are placed from left to right in the bottom row, according to the column-major order of their appearance in the input.

3.  **Remove**: If any adjacent cell has the same color after relocating, only keep the leftmost one, and remove duplicate colors to its right, to avoid having adjacent cells in the last row of output with the same color.
 
**Inferred Transformation Rule Summary**

The transformation rule can be summarized as follows:
The colored objects from the input are copied and consolidated/moved into the bottom row of the output grid, maintaining their original order, and removing equal adjacent colored cells. The remaining cells are set to white (0).

```python
"""
The transformation rule can be summarized as follows:
The colored objects from the input are copied and consolidated/moved into the bottom row of the output grid, maintaining their original order, and removing equal adjacent colored cells. The remaining cells are set to white (0).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule:
    Colored cells are moved to the last row, maintaining their order,
    and the rest of the grid is filled with white (0).
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # 1. Identify non-white cells and their original order.
    non_white_cells = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                non_white_cells.append((input_grid[r, c], r, c)) # Store color and original position

    # 2. Sort non-white cells to preserve the column-major order in the bottom row
    non_white_cells_sorted = sorted(non_white_cells, key=lambda x: (x[1], x[2]))
    # non_white_cells_sorted = sorted(non_white_cells, key=lambda x: (x[2], x[1]))
     
    # 3. Place the sorted non-white cells in the last row of the output grid.
    last_row_index = 0
    for cell in non_white_cells_sorted:
        output_grid[rows - 1, last_row_index] = cell[0]
        last_row_index += 1

    return output_grid.tolist()
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
