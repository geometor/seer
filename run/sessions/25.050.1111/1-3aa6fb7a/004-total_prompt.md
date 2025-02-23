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

<PIL.Image.Image image mode=RGB size=448x448 at 0x76B4C2415D80>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x76B4C24167A0>
Okay, let's analyze the transformation between the input and output grids.

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      shape: two L-shaped structures
      positions:
        - top-left corner of the first 'L': (1,1) # (row, col)
        - top-left corner of the second 'L': (3,4)
    - color: 0 (white)
      shape: background
      positions:
        - all other cells

output_grid:
  objects:
    - color: 8 (azure)
      shape: two L-shaped structures (same as input)
      positions:
        - top-left corner of the first 'L': (1,1)
        - top-left corner of the second 'L': (3,4)
      
    - color: 1 (blue)
      shape: single cells
      positions:
        - (1,2)
        - (4,5)
    - color: 0 (white)
      shape: background
      positions:
        - all other cells

```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** In the input grid, we observe two "L"-shaped objects of color 8 (azure) against a background of color 0 (white).

2.  **Detect Change:**
    -   Locate the uppermost and leftmost azure (8) cell of the first L-shaped object.
    -   Locate the uppermost and leftmost cell of the second L-shaped object.
    - The top-left cell is detected by finding the azure cell with the smallest row number. Among cells, the top-left is the one with the smallest column number.

3.  **Apply Transformation:**
    *   Change the color of the cell immediately to the right of the uppermost and leftmost cell of the first L shape to color 1(blue)
    *   Change the color of cell immediately above of the bottom-most azure (8) of the second L shape to color 1(blue)

**Transformation Rule Summary**

The transformation preserves the azure (8) L-shaped objects. It adds blue cells adjacent to specific parts of the azure objects: A blue color 1 cell is placed immediately right of uppermost, leftmost cell of the first azure L, and a blue 1 is placed above the bottom most cell of the second azure L.

```python
"""
The transformation preserves the azure (8) L-shaped objects. It adds blue cells adjacent to specific parts of the azure objects: A blue color 1 cell is placed immediately right of uppermost, leftmost cell of the first azure L, and a blue 1 is placed above the bottom most cell of the second azure L.
"""

import numpy as np

def find_top_left_cell(grid, color):
    """Finds the uppermost and leftmost cell of a given color."""
    rows, cols = np.where(grid == color)
    if len(rows) == 0:
        return None
    min_row_index = np.argmin(rows)
    min_col_index = np.argmin(cols)

    min_row = rows[min_row_index]
    indices = np.where(rows == min_row)[0]
    min_col = cols[indices[np.argmin(cols[indices])]]
    return min_row, min_col

def find_bottom_most_cell(grid, color):
    """Finds the bottom-most cell of given color"""
    rows, cols = np.where(grid == color)
    if len(rows) == 0:
        return None
    max_row_index = np.argmax(rows)

    max_row = rows[max_row_index]
    return max_row

def get_l_objects(grid,color):
    """ Get all separated L shaped objects """
    objects = []
    visited = set()
    rows, cols = grid.shape
    
    def is_valid(r,c):
        return 0 <= r < rows and 0 <= c < cols
    
    def dfs(r,c, current_object):
        if (r,c) in visited or not is_valid(r,c) or grid[r,c] != color:
            return
        visited.add((r,c))
        current_object.append((r,c))
        
        dfs(r+1,c,current_object)
        dfs(r-1,c,current_object)
        dfs(r,c+1, current_object)
        dfs(r,c-1,current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r,c] == color and (r,c) not in visited:
                current_object = []
                dfs(r,c,current_object)
                objects.append(current_object)
    return objects
        

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    objects = get_l_objects(input_grid,8)
    
    if len(objects) >= 2:
        first_l = objects[0]
        second_l = objects[1]

    # Find top-left of first L
        first_l_rows = [r for r, _ in first_l]
        first_l_cols = [c for _, c in first_l]

        min_row_index = np.argmin(first_l_rows)
        min_row = first_l_rows[min_row_index]

        indices = np.where(np.array(first_l_rows) == min_row)[0]
        min_col = first_l_cols[indices[np.argmin(np.array(first_l_cols)[indices])]]
        top_left_first_l = (min_row, min_col)

      # Place blue cell to the right of the top-left of the first L
        if top_left_first_l[1] + 1 < output_grid.shape[1]:
          output_grid[top_left_first_l[0], top_left_first_l[1] + 1] = 1

        # Find bottom-most cell of second L.

        second_l_rows = [r for r,_ in second_l]
        second_l_cols = [c for _,c in second_l]

        max_row = np.max(second_l_rows)


      # Place blue cell above the bottom-most cell of the second L
        if max_row -1 >= 0:
          output_grid[max_row - 1, second_l_cols[np.where(np.array(second_l_rows) == max_row)[0][0]]] = 1
    

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x76B4C249F9A0>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x76B4C2416620>
Okay, let's analyze the second example.

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      shape: three L-shaped structures and one single cell
      positions:
        - top-left corner of the first 'L': (0, 4)
        - top-left corner of the second 'L': (2, 2)
        - top-left corner of the third 'L': (6,3)
        - single cell: (5,5)
    - color: 0 (white)
      shape: background
      positions:
        - all other cells

output_grid:
  objects:
    - color: 8 (azure)
      shape: three L-shaped structures and one single cell
      positions:
        - top-left corner of the first 'L': (0, 4)
        - top-left corner of the second 'L': (2, 2)
        - top-left corner of the third 'L': (6,3)
        - single cell: (5,5) # assuming single cells persist

    - color: 1 (blue)
      shape: single cells
      positions:
        - (1, 4)
        - (2, 3)
        - (5,3)
    - color: 0 (white)
      shape: background
      positions:
        - all other cells
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** In the input grid, we see three distinct "L"-shaped objects and one single cell, all of color 8 (azure), against a background of color 0 (white).

2.  **Transformation Rule:** The transformation places a blue cell (color 1) next to specific parts of the azure L-shapes and single azure cell.
    *   For all L shaped objects we change to 1(blue) the cell adjacent to the right or on top of the uppermost-leftmost cell. If the azure cell right next to the uppermost-leftmost is out of the grid, the cell on top is chosen.

3. **Apply Transformation**

**Transformation Rule Summary**
The azure color 8 objects are preserved. A blue (1) cell is placed on top or at the right of uppermost and leftmost azure cell, in each azure L-shaped object. If placing to the right is not within bounds, placing on top is selected.

```python
"""
The azure color 8 objects are preserved. A blue (1) cell is placed on top or at the right of uppermost and leftmost azure cell, in each azure L-shaped object. If placing to the right is not within bounds, placing on top is selected.
"""

import numpy as np

def find_top_left_cell(grid, color):
    """Finds the uppermost and leftmost cell of a given color."""
    rows, cols = np.where(grid == color)
    if len(rows) == 0:
        return None
    min_row_index = np.argmin(rows)
    min_col_index = np.argmin(cols)

    min_row = rows[min_row_index]
    indices = np.where(rows == min_row)[0]
    min_col = cols[indices[np.argmin(cols[indices])]]
    return min_row, min_col

def find_bottom_most_cell(grid, color):
    """Finds the bottom-most cell of given color"""
    rows, cols = np.where(grid == color)
    if len(rows) == 0:
        return None
    max_row_index = np.argmax(rows)

    max_row = rows[max_row_index]
    return max_row

def get_l_objects(grid,color):
    """ Get all separated L shaped objects """
    objects = []
    visited = set()
    rows, cols = grid.shape
    
    def is_valid(r,c):
        return 0 <= r < rows and 0 <= c < cols
    
    def dfs(r,c, current_object):
        if (r,c) in visited or not is_valid(r,c) or grid[r,c] != color:
            return
        visited.add((r,c))
        current_object.append((r,c))
        
        dfs(r+1,c,current_object)
        dfs(r-1,c,current_object)
        dfs(r,c+1, current_object)
        dfs(r,c-1,current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r,c] == color and (r,c) not in visited:
                current_object = []
                dfs(r,c,current_object)
                objects.append(current_object)
    return objects
        

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    objects = get_l_objects(input_grid,8)
    
    for obj in objects:

    # Find top-left of first L
        obj_rows = [r for r, _ in obj]
        obj_cols = [c for _, c in obj]

        min_row_index = np.argmin(obj_rows)
        min_row = obj_rows[min_row_index]

        indices = np.where(np.array(obj_rows) == min_row)[0]
        min_col = obj_cols[indices[np.argmin(np.array(obj_cols)[indices])]]
        top_left = (min_row, min_col)
      # Place blue cell to the right of the top-left of the first L
        if top_left[1] + 1 < output_grid.shape[1]:
          output_grid[top_left[0], top_left[1] + 1] = 1
        elif top_left[0] -1 >= 0:
          output_grid[top_left[0]-1,top_left[1]] = 1

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
