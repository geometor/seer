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

<PIL.Image.Image image mode=RGB size=448x448 at 0x74D3F3511D20>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x74D3F3512AD0>
Okay, let's analyze the transformation between the input and output grids.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      positions: [(1,1), (2,1), (2,2), (3,4), (3,5), (4,5)]
      shape: Two separate L-shaped objects.
  dimensions: 7x7

output_grid:
  objects:
    - color: 8 (azure)
      positions: [(1,1), (2,1), (2,2), (3,4), (3,5), (4,5)]
      shape:  Two separate L-shaped objects. Same as input.
    - color: 1 (blue)
      positions: [(1,2), (4,4)]
      shape: Two single-cell objects.
  dimensions: 7x7
```

**Natural Language Program: Transformation Rule**

1.  **Identify Objects:** In the input grid, we can identify two distinct L-shaped objects of color 8 (azure).
2.  **Preservation:** The two azure L-shaped structures from the input are kept unchanged in the output.
3. **Change Detection:** Now we look for changes:
    *   The cell at (1, 2) is now a blue cell. In the input it was a white cell (color 0).
    *   The cell at (4, 4) is now a blue cell. In the input it was a white cell (color 0).
4. **Find the changed cells**: Check the cells that are to the immediate right (neighbor) of the top left corner of the azure objects. If those cells has color 0 (white), change those cells to have color 1 (blue).

**Step-by-step description in simple terms**:

The rule seems to change the color of cells to the right the top-left-corner of color 8 (azure) "L" shapes.
- The cell to the right of the uppermost-leftmost azure cell, is changed to blue.
- The cell to the right of the other L-shape uppermost-leftmost azure cell is changed to blue.


```python
"""
The transformation rule preserves two L-shaped azure objects and changes the color of the cells immediately to the right of their top-left corners from white (0) to blue (1).
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds connected regions of the specified color and returns a list of their coordinates.
    Uses a simple flood-fill algorithm.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def flood_fill(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            flood_fill(r + dr, c + dc, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                flood_fill(r, c, current_object)
                objects.append(current_object)

    return objects
def get_top_left(obj):
    """
    Gets the top-left coordinate of an object.
    """
    min_row = float('inf')
    min_col = float('inf')

    for r, c in obj:
        if r < min_row:
            min_row = r
        if c < min_col:
          min_col = c
    return min_row,min_col
def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    1.  Identify azure (color 8) L-shaped objects.
    2.  Preserve their structure.
    3. Change to blue the cells to the right of the top-left-corner
    of each object, from white (color 0)
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    # Iterate through the azure objects
    for obj in azure_objects:
      #find top-left corner
      top_left_r, top_left_c = get_top_left(obj)
      #check if the cell to the right exists and it is color 0
      if top_left_c + 1 < output_grid.shape[1] and output_grid[top_left_r,top_left_c + 1] == 0:
        output_grid[top_left_r, top_left_c + 1] = 1
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

<PIL.Image.Image image mode=RGB size=448x448 at 0x74D3F35127D0>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x74D3F3512050>
Okay, let's analyze the second example provided.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      positions: [(0,4), (0,5), (1,5), (2,2), (3,2), (3,3), (5,4), (6,4),(6,3)]
      shape: Three separate L-shaped objects.
  dimensions: 7x7

output_grid:
  objects:
    - color: 8 (azure)
      positions:  [(0,4), (0,5), (1,5), (2,2), (3,2), (3,3), (5,4), (6,4),(6,3)]
      shape:  Three separate L-shaped objects. Same as input.
    - color: 1 (blue)
      positions: [(1,4), (2,3), (5,3)]
      shape: Three single-cell objects.
  dimensions: 7x7
```

**Natural Language Program: Transformation Rule**

1.  **Identify Objects:** In the input grid, we can identify three distinct L-shaped objects of color 8 (azure).
2.  **Preservation:** The three azure L-shaped structures from the input are kept unchanged in the output.
3. **Change Detection:** Now we look for changes:
    *   The cell at (1, 4) is now a blue cell. In the input it was a white cell (color 0).
    *   The cell at (2, 3) is now a blue cell. In the input it was a white cell (color 0).
    *   The cell at (5, 3) is now a blue cell. In the input it was a white cell (color 0).
4. **Find the changed cells**: Check the cells that are to the immediate left (neighbor) of the top right corner of the azure objects. If those cells has color 0 (white), change those cells to have color 1 (blue).

**Step-by-step description in simple terms**:

The rule seems to change the color of cells to the *left* the top-*right*-corner of color 8 (azure) "L" shapes.

- The cell to the left of the uppermost-rightmost azure cell of each L-shape, is changed to blue.

```python
"""
The transformation rule preserves three L-shaped azure objects and changes the color of the cells immediately to the left of their top-right corners from white (0) to blue (1).
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds connected regions of the specified color and returns a list of their coordinates.
    Uses a simple flood-fill algorithm.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def flood_fill(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            flood_fill(r + dr, c + dc, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                flood_fill(r, c, current_object)
                objects.append(current_object)

    return objects
def get_top_right(obj):
    """
    Gets the top-right coordinate of an object.
    """
    min_row = float('inf')
    max_col = float('-inf')

    for r, c in obj:
        if r < min_row:
            min_row = r
        if c > max_col:
          max_col = c
    return min_row,max_col
def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    1.  Identify azure (color 8) L-shaped objects.
    2.  Preserve their structure.
    3. Change to blue the cells to the left of the top-right-corner
    of each object, from white (color 0)
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    # Iterate through the azure objects
    for obj in azure_objects:
      #find top-right corner
      top_right_r, top_right_c = get_top_right(obj)
      #check if the cell to the left exists and it is color 0
      if top_right_c - 1 >= 0  and output_grid[top_right_r,top_right_c - 1] == 0:
        output_grid[top_right_r, top_right_c - 1] = 1
    return output_grid
```

**Evaluation and Refinement**

The first example had to do with the top-left corner.

I've changed now `get_top_left` to `get_top_right` and `min_col` to `max_col`, because this time we must look at the top-right corner.
Also, I have changed  `if top_left_c + 1 < output_grid.shape[1] and output_grid[top_left_r,top_left_c + 1] == 0:` to `if top_right_c - 1 >= 0  and output_grid[top_right_r,top_right_c - 1] == 0:` because now we check if the cell at the *left* exists, not at the right.

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
