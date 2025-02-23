# 3-1e0a9b12 • 006 • example_3 - CODE

---

**input**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7017B29F90F0>

**output**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7017B29FB040>

*text:*
Okay, let's analyze the transformation from the input grid to the output grid.

**Observations in YAML Format**

```yaml
input_grid:
  size: 4x4
  objects:
    - color: 4 (yellow)
      positions: [(0, 1), (2, 1)]
    - color: 9 (maroon)
      positions: [(0, 3)]
    - color: 6 (magenta)
      positions: [(2, 2)]
    - color: 1 (blue)
      positions: [(3, 0)]
    - color: 0 (white)
      positions: All other cells

output_grid:
  size: 4x4
  objects:
    - color: 4 (yellow)
      positions: [(2,1), (3, 1)]
    - color: 9 (maroon)
      positions: [(3, 3)]
    - color: 6 (magenta)
      positions: [(3, 2)]
    - color: 1 (blue)
      positions: [(3, 0)]
    - color: 0 (white)
      positions: All other cells
```

**Natural Language Program Description**

1.  **Identify Non-White Objects:** Locate all cells in the input grid that are not white (color 0).

2.  **Move Objects:** The non-white objects are moved/translated to the bottom row of the output grid.

3.    **Preserve Order:** Specifically, the non-white objects present maintain their relative horizontal order when moved.
    *   The leftmost non-white object in the input (blue, color 1) becomes the leftmost in the bottom row of the output.
    *   The second non-white object (yellow color 4) stays the second.
    *   The next yellow object is moved down.
    *   The magenta and maroon objects maintain their order as well.

4. **Clear other Cells.** All cells that are not part of the final positions of the copied objects are set to color 0.

In summary, the transformation involves moving all non-white cells to the last row, preserving their original horizontal order, and setting all other cells to white.


*text:*
```python
"""
Moves all non-white cells to the last row, preserving their original horizontal order, and setting all other cells to white.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving non-white objects to the bottom row,
    preserving their horizontal order.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Find non-white cells and their column indices
    non_white_cells = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                non_white_cells.append((c, input_grid[r, c]))

    # Sort non-white cells by their column index (original horizontal order)
    non_white_cells.sort()

    # Place non-white cells in the last row of the output grid
    for i, (col, color) in enumerate(non_white_cells):
        output_grid[rows - 1, i] = color

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

<PIL.Image.Image image mode=RGB size=384x384 at 0x7017B29FA140>

**output**
```
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
4 0 0 0 0 0
4 0 7 8 0 0
4 0 7 8 0 9
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x7017B29FBD00>

*text:*
Okay, let's analyze the transformation from the input grid to the output grid in this second example.

**Observations in YAML Format**

```yaml
input_grid:
  size: 6x6
  objects:
    - color: 9 (maroon)
      positions: [(0, 5)]
    - color: 8 (azure)
      positions: [(1, 3), (4, 3)]
    - color: 4 (yellow)
      positions: [(3, 0), (4, 0), (5, 0)]
    - color: 7 (orange)
      positions: [(4, 2), (5, 2)]
    - color: 0 (white)
      positions: All other cells

output_grid:
  size: 6x6
  objects:
    - color: 9 (maroon)
      positions: [(5, 5)]
    - color: 8 (azure)
      positions: [(4, 3), (5,3)]
    - color: 4 (yellow)
      positions: [(3, 0), (4, 0), (5, 0)]
    - color: 7 (orange)
      positions: [(4, 2), (5, 2)]
    - color: 0 (white)
      positions: All other cells
```

**Natural Language Program Description**

1.  **Identify Non-White Objects:** First, we identify all the cells in the input grid that contain a color other than white (0).

2.  **Move Objects to the bottom:** We observe that all the non-white objects are moved down to the last row, if not present, objects are kept in the rows where they already are.

3.  **Preserve Horizontal Order:** The relative horizontal order of these non-white objects is preserved.
    *   Yellow (4) objects, which are leftmost, remain in their original rows and columns,
    *   Orange (7) objects stay in their relative positions and rows,
    * Azure and Maroon Objects are moved to the bottom keeping their relative position

4. **Clear Other Cells:** Any cell not occupied by one of the moved/copied objects in the output is set to white (0).

In essence, this transformation rule involves identifying all non-white objects, moving them to their respective position based on the previous example, and keeping the horizontal order.


*text:*
*text:*
```python
"""
Moves non-white cells to the last row if they are not already in the rows where non-white objects are present,
preserving their original horizontal order, and setting all other cells to white. Objects that are in rows containing
non-white objects should maintain position.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving non-white objects to the bottom row,
    preserving their horizontal order, or keeping them in existing rows if non-white
    objects are already present.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Find non-white cells and their column indices
    non_white_cells = []
    rows_with_non_white = set()

    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                non_white_cells.append((r, c, input_grid[r, c]))
                rows_with_non_white.add(r)


    # copy objects in rows with existing colors
    for r in rows_with_non_white:
        for c in range(cols):
            if input_grid[r,c] != 0:
               output_grid[r,c]= input_grid[r,c]

    # Sort non-white cells by their column index (original horizontal order)
    non_white_cells_to_move = []

    for r, c, color in non_white_cells:
      if  not any(input_grid[r,i]!=0 for i in range(cols)  if r!= rows-1):
          non_white_cells_to_move.append( (c, color) )

    non_white_cells_to_move.sort()


    # Place non-white cells in the last row of the output grid
    current_col = 0
    for _, color in non_white_cells_to_move:
        while(output_grid[rows-1, current_col]!=0):
          current_col = current_col + 1
        output_grid[rows - 1, current_col] = color

    return output_grid.tolist()
```


**input**
```
0 0 0 1 0
0 3 0 0 0
0 3 0 1 2
6 0 0 0 0
0 3 0 0 0
```

<PIL.Image.Image image mode=RGB size=320x320 at 0x7017B1F8CBB0>

**output**
```
0 0 0 0 0
0 0 0 0 0
0 3 0 0 0
0 3 0 1 0
6 3 0 1 2
```

<PIL.Image.Image image mode=RGB size=320x320 at 0x7017B1F8CEE0>

*text:*
Okay, let's analyze the transformation from the input grid to the output grid in this third example.

**Observations in YAML Format**

```yaml
input_grid:
  size: 5x5
  objects:
    - color: 1 (blue)
      positions: [(0, 3), (2, 3)]
    - color: 3 (green)
      positions: [(1, 1), (2, 1), (4, 1)]
    - color: 2 (red)
      positions: [(2, 4)]
    - color: 6 (magenta)
      positions: [(3, 0)]
    - color: 0 (white)
      positions: All other cells

output_grid:
  size: 5x5
  objects:
    - color: 1 (blue)
      positions: [(3, 3), (4,3)]
    - color: 3 (green)
      positions: [(2, 1), (3, 1), (4,1)]
    - color: 2 (red)
      positions: [(4, 4)]
    - color: 6 (magenta)
      positions: [(4, 0)]
    - color: 0 (white)
      positions: All other cells
```

**Natural Language Program Description**

1.  **Identify Non-White Objects:** First, we identify all cells in the input grid that are not white (color 0).

2.  **Move Objects to the bottom:** We observe that all the non-white objects are moved down to the last row, if not present, objects are kept in the rows where they already are.

3.  **Preserve Horizontal Order:** The relative horizontal order of these non-white objects is preserved.
    *   Magenta (6) object, which is leftmost, remains in their original rows and columns,
    *   Green (3) objects stay in their relative positions and rows,
    * Blue and Red Objects are moved to the bottom keeping their relative position

4. **Clear Other Cells:** Any cell not occupied by one of the moved/copied objects in the output is set to white (0).

In essence, this transformation rule involves identifying all non-white objects, moving them to their respective position based on the previous example, and keeping the horizontal order.

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
