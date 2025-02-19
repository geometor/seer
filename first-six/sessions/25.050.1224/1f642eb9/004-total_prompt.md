# 1f642eb9 • 004 • example_2 - CODE

---

**input**
```
0 0 0 0 9 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 8 8 0 0 0 0
0 0 0 0 8 8 0 0 0 0
0 0 0 0 8 8 0 0 0 0
6 0 0 0 8 8 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 4 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x79CABA17AD10>

**output**
```
0 0 0 0 9 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 9 8 0 0 0 0
0 0 0 0 8 8 0 0 0 0
0 0 0 0 8 8 0 0 0 0
6 0 0 0 6 4 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 4 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x79CABA17ABC0>
Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Description of Observations**

```yaml
input_grid:
  size: 10x10
  objects:
    - color: 9
      shape: single cell
      position: (0, 4)
    - color: 8
      shape: 2x3 rectangle
      position: (3, 4)
    - color: 6
      shape: single cell
      position: (6, 0)
    - color: 4
      shape: single cell
      position: (9, 5)

output_grid:
  size: 10x10
  objects:
    - color: 9
      shape: single cell, and a 1x2 vertical rectangle
      position: original (0, 4), adjacent (3,4)
    - color: 8
      shape: 2x2 square, and single cell
      position: original (4,4), adjacent (3,5)
    - color: 6
      shape: single cell, and single cell
      position: original (6, 0), adjacent (6,4)
    - color: 4
      shape: single cell, and single cell
      position: original (9, 5), adjacent (6,5)
```

**Natural Language Program: Transformation Rule**

1.  **Identify Objects:** Locate all distinct objects in the input grid. We have four single-color cells (9, 6, and 4, one each) and the rectangle made with color 8.

2.  **Move 9**: The cell with color 9 combines with the 8 object. Specifically, color 9 moves to the top of the closest 8 object. This creates an object with 9 on top and 8 at the bottom.

3.  **Move 6:** The cell with color 6 moves to the bottom left side of the closest color 8, but at the level of the bottom row of the 8 rectangle.

4. **Move 8:** We use the top left corner of the 8 to find a cell to separate from the rectangle, at (3,5).

5.  **Move 4:** The cell with color 4 moves near the object made of color 8, maintaining the column, but getting as close as possible to the object.

**Summary**
Each single color cell targets the 8 object. Each one takes a different position. Number 9 takes the upper one, number 4 takes the center one and number 6 takes the left-bottom one. The 8 object loses one cell.

```python
"""
Each single color cell targets the 8 object. Each one takes a different position. Number 9 takes the upper one, number 4 takes the center one and number 6 takes the left-bottom one. The 8 object loses one cell.
"""

import numpy as np

def find_objects(grid):
    """Finds contiguous regions of the same color."""
    objects = {}
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, color, obj_coords):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1]
                or visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        obj_coords.append((row, col))
        dfs(row + 1, col, color, obj_coords)
        dfs(row - 1, col, color, obj_coords)
        dfs(row, col + 1, color, obj_coords)
        dfs(row, col - 1, color, obj_coords)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col] and grid[row,col] != 0:
                color = grid[row, col]
                obj_coords = []
                dfs(row, col, color, obj_coords)
                if color not in objects:
                    objects[color] = []
                objects[color].append(obj_coords)

    return objects

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = input_grid.copy()

    # Find objects in the input grid
    objects = find_objects(input_grid)

    # Find the '8' object (assuming there's only one)
    eight_object = objects.get(8)[0]  # List of coordinates of the '8' object
    
    # Get top left corner of the eight_object
    eight_object_rows = [coord[0] for coord in eight_object]
    eight_object_cols = [coord[1] for coord in eight_object]
    eight_top_row = min(eight_object_rows)
    eight_left_col = min(eight_object_cols)
    eight_bottom_row = max(eight_object_rows)

    # Move '9'
    nine_coords = objects.get(9)[0][0]
    output_grid[nine_coords] = 0
    output_grid[eight_top_row -1, eight_left_col] = 9

    # Move '6'
    six_coords = objects.get(6)[0][0]
    output_grid[six_coords] = 0
    output_grid[eight_bottom_row, eight_left_col -1] = 6

    # Move '8'
    output_grid[eight_top_row, eight_left_col+1] = 0
    
    #Move 4
    four_coords = objects.get(4)[0][0]
    output_grid[four_coords] = 0
    output_grid[eight_bottom_row, eight_left_col ] = 4

    return output_grid
```

**input**
```
0 0 0 0 7 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
6 0 0 8 8 8 0 0 0 0
0 0 0 8 8 8 0 0 0 0
0 0 0 8 8 8 0 0 0 2
0 0 0 8 8 8 0 0 0 0
3 0 0 8 8 8 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x79CABAB06380>

**output**
```
0 0 0 0 7 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
6 0 0 6 7 8 0 0 0 0
0 0 0 8 8 8 0 0 0 0
0 0 0 8 8 2 0 0 0 2
0 0 0 8 8 8 0 0 0 0
3 0 0 3 8 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x79CABB63BA60>
Okay, let's analyze the second transformation.

**YAML Description of Observations**

```yaml
input_grid:
  size: 10x10
  objects:
    - color: 7
      shape: single cell
      position: (0, 4)
    - color: 8
      shape: 3x4 rectangle
      position: (3, 3)
    - color: 6
      shape: single cell
      position: (3, 0)
    - color: 2
      shape: single cell
      position: (5, 9)
    - color: 3
      shape: single cell
      position: (7, 0)
    - color: 1
      shape: single cell
      position: (9, 5)

output_grid:
  size: 10x10
  objects:
    - color: 7
      shape: single cell
      position: (3, 4)
    - color: 8
      shape: 3x3 rectangle, and a 1x1
      position: (3,3) and (3,5)
    - color: 6
      shape: single cell, and a 1x1
      position: (3, 0) and (3,3)
    - color: 2
      shape: single cell, and a 1x1
      position: (5, 9) and (5,5)
    - color: 3
      shape: single cell, and a 1x1
      position: (7, 0) and (7,3)
     - color: 1
      shape: single cell, and a 1x1
      position: (9, 5) and (7,5)
```

**Natural Language Program: Transformation Rule**

1.  **Identify Objects:**  We have four single-color cells (7, 6, 2, 3 and 1) and one larger rectangular object of color 8.

2. **Move the single cells:**
    - Color 7 stays in the same position of the input and adds a new cell in the input, on top of the 8 object.
    - Colors 6, 3, and 1 each combine with the closest object made of color 8, creating new objects made of two cells, each new object made of colors 8 and 6, 3 and 1, respectively.
    - The 8 object loses one of its cells, the one on column 5 and row 3.

3. **Move 8:**
    - The cell at the position (3,5) on the object with color 8 is removed and it is placed to the right side of number 2, at the same row.

4.  **Summary**: Number 7 adds a cell to the top of the main object. The rest of the numbers combines with 8 on the left side of it. Number 2 combines with the cell that was removed.

```python
"""
Number 7 adds a cell to the top of the main object. The rest of the numbers combines with 8 on the left side of it. Number 2 combines with the cell that was removed.
"""

import numpy as np

def find_objects(grid):
    """Finds contiguous regions of the same color."""
    objects = {}
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, color, obj_coords):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1]
                or visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        obj_coords.append((row, col))
        dfs(row + 1, col, color, obj_coords)
        dfs(row - 1, col, color, obj_coords)
        dfs(row, col + 1, color, obj_coords)
        dfs(row, col - 1, color, obj_coords)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col] and grid[row,col] != 0:
                color = grid[row, col]
                obj_coords = []
                dfs(row, col, color, obj_coords)
                if color not in objects:
                    objects[color] = []
                objects[color].append(obj_coords)

    return objects

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = input_grid.copy()

    # Find objects in the input grid
    objects = find_objects(input_grid)

    # Find the '8' object (assuming there's only one)
    eight_object = objects.get(8)[0]  # List of coordinates of the '8' object
    
    # Get top left corner of the eight_object
    eight_object_rows = [coord[0] for coord in eight_object]
    eight_object_cols = [coord[1] for coord in eight_object]
    
    eight_top_row = min(eight_object_rows)
    eight_left_col = min(eight_object_cols)
    eight_bottom_row = max(eight_object_rows)

    # Move '7'
    output_grid[eight_top_row, eight_left_col ] = 7

    # Move '6'
    six_coords = objects.get(6)[0][0]
    output_grid[eight_top_row, eight_left_col-1] = 6
    
    #Move 3
    three_coords = objects.get(3)[0][0]
    output_grid[eight_bottom_row, eight_left_col -1] = 3

    # Move '2'
    two_coords = objects.get(2)[0][0]
    output_grid[two_coords[0], eight_left_col + 2] = 2    

    #Move 1
    one_coords = objects.get(1)[0][0]
    output_grid[eight_bottom_row, eight_left_col+1] = 1    
    
    # Move '8'
    output_grid[eight_top_row, eight_left_col+2] = 0

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
