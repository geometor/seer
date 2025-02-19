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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7739DE52EE90>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7739DE52E440>
Okay, let's analyze the transformation between the input and output grids.

**YAML Observation:**

```yaml
input_grid:
  dimensions: [7, 7]
  objects:
    - color: 8
      positions: [[1, 1], [2, 1], [2, 2], [4, 4], [4, 5], [5,4]]
      shape: "Two separate 2x1 and 1x2 azure (8) colored rectangles."
    - color: 0
      positions: "All other cells that don't have color 8"
      shape: "background"
output_grid:
  dimensions: [7, 7]
  objects:
     - color: 8
       positions: [[1, 1], [2, 1], [2, 2], [4, 4], [4, 5], [5,4]]
       shape: "Two separate 2x1 and 1x2 azure (8) colored rectangles."
     - color: 1
       positions: [[1,2], [5,4]]
       shape: "Two isolated blue (1) colored cells."
     - color: 0
       positions: "All other cells that don't have color 1 or 8"
       shape: "background"

```

**Natural Language Program:**

Here's a step-by-step description of the transformation rule:

1.  **Identify Objects:** The input grid consists of two distinct azure (color 8) objects and the white background (color 0).
    *    Object 1: A 2x1 rectangle at the top-left.
    *    Object 2: A 1x2 rectangle at the bottom-right.

2.  **Detect corner cell in the objects:**
    *  Object 1 has cell [1,1] as part of a vertical line.
    *  Object 2 has cell [5,4] as part of a horizontal line

3.  **Change cells:** Change the azure (8) color of those cells in each object by the blue color (1).

4.  **Preserve:** All the other cells keep the original color.

In summary, the rule involves identifying azure objects, finding the corner cell in the biggest rectangle of the object, and turning to blue this cell. Other cells remain the same.

```python
"""
The transformation rule identifies azure (color 8) objects in the input grid. 
For each azure object, it locates specific corner:
- if the corner is part of a vertical line selects the top cell.
- if the corner is part of a horizontal line selects the left cell.
Then, changes that identified cell's color to blue (color 1). All other cells remain unchanged.
"""

import numpy as np

def get_objects(grid, color):
    """
    Finds contiguous regions of the specified color in the grid.
    Returns a list of lists of coordinates.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(r + dr, c + dc, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def find_corner_cell(obj):
    """
    Finds the corner cell of an object. It considers the cell part of the longest
    rectangle side.

    """
    min_row = min(cell[0] for cell in obj)
    #max_row = max(cell[0] for cell in obj)
    min_col = min(cell[1] for cell in obj)
    #max_col = max(cell[1] for cell in obj)

    top_left = (min_row, min_col)

    is_vertical = False
    for cell in obj:
      if cell[0] == min_row + 1 and cell[1] == min_col:
        is_vertical = True
        break

    if is_vertical:
      return top_left
    else:
      return top_left
      
def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Get azure (color 8) objects
    azure_objects = get_objects(output_grid, 8)
    
    # Iterate through each azure object
    for obj in azure_objects:
        # Find the corner cell of the object
        corner_cell = find_corner_cell(obj)

        # Change the corner cell's color to blue (color 1)
        output_grid[corner_cell[0], corner_cell[1]] = 1

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7739DE521BD0>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7739DE520820>
Okay, let's analyze the second example.

**YAML Observation:**

```yaml
input_grid:
  dimensions: [7, 7]
  objects:
    - color: 8
      positions: [[0, 4], [0, 5], [1, 5], [2, 2], [3, 2], [3, 3], [5, 4], [6, 3], [6, 4]]
      shape: "Three separate azure (8) colored objects: two lines and one square."
    - color: 0
      positions: "All other cells not colored 8"
      shape: "Background"

output_grid:
  dimensions: [7, 7]
  objects:
    - color: 8
      positions: [[0, 4], [0, 5], [1, 5], [2, 2], [3, 2], [3, 3], [5, 4], [6, 3], [6, 4]]
      shape: "Three separate azure (8) colored objects: two lines and one square, same as the input."
    - color: 1
      positions: [[1, 4], [2,3], [5,3]]
      shape: "Three single cells colored blue in different positions."
    - color: 0
      positions: "All other cells not colored with 8 or 1."
      shape: "Background"
```

**Natural Language Program:**

Here's a step-by-step description of the transformation rule:

1.  **Identify Objects:** The input grid has three distinct azure (color 8) objects.

    *   Object 1: A 1x2 horizontal line at the top.
    *   Object 2: A 2x2 square in the center-left.
    *   Object 3: A bent shape on the bottom-right.

2.  **Detect corner cell in the objects:**
    *   Object 1 has cell [0,4] as part of a horizontal line.
    *   Object 2 has cell [2,2] as part of a vertical line.
    *   Object 3 has cell [5,4] as part of a vertical line.

3.  **Change cell color:** The azure cell at the top-left "corner" of each object changes its color to blue (1). The selection criteria is:
    *   Select left-most for horizontal line
    *   Select upper-most for vertical line

4.  **Preserve:** All other cells maintain their original colors.

The core rule is the same as the first case. It is necessary to identify objects colored in azure (8). In each object find the corner cell: leftmost if is part of a horizontal line and uppermost if is part of a vertical line. Change to blue the cells identified in this way.

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
