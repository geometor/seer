# 1-3aa6fb7a • 006 • example_2 - CODE

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

![Image](001-example_1_input.png)


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

![Image](001-example_1_output.png)

Okay, let's analyze the transformation between the input and output grids.

**YAML Description of Observations**

```yaml
input_observations:
  objects:
    - color: 8 (azure)
      shape: Two separate 2x1 vertical rectangles
      positions:
        - Top rectangle: (1,1)  # Using (row, col) 0-indexed
        - Bottom rectangle: (3,5)
    - color: 0 (white)
      shape: Background
      positions:
        - All other cells

output_observations:
  objects:
    - color: 8 (azure)
      shape: Two separate 2x1 vertical rectangles
      positions:
        - Top rectangle: (1,1)
        - Bottom rectangle: (3,5)
    - color: 1 (blue)
      shape: Two single cells
      positions:
        - Next to top rectangle: (1,2)
        - Next to bottom rectangle: (4,5)

    - color: 0 (white)
      shape: Background
      positions:
        - All other cells
```

**Natural Language Program: Step-by-step Transformation**

1.  **Identify Objects:** In the input grid, we have two distinct objects made of color 8 (azure). Each object is a 2x1 vertical rectangle. There are also background cells that are color 0.

2.  **Locate Key Positions:**
    *   The first azure rectangle starts at row 1, column 1.
    *   The second azure rectangle starts at row 3, column 5.

3. **Observe changes:** The azure rectangles remain unchanged. Two blue cells are added next to each of them.

4.  **Transformation Rule:** For each of the two azure (8) colored 2x1 rectangles, add the value '1' to the right of the top cell of the vertical rectangle and another one '1' before the bottom cell of the rectangle.

In summary, the rule involves keeping the existing 2 x 1 azure rectangles and adding new blue (1) cell to the right of their top cells, and a blue (1) cell before their bottom cell.

```python
"""
The transformation rule involves keeping the existing 2x1 azure rectangles and adding a new blue (1) cell to the right of their top cells, and a blue (1) cell before their bottom cell.
"""

import numpy as np

def find_objects(grid):
    """
    Finds contiguous regions of the same color and returns them as a list of objects.
    Each object is a dictionary with 'color' and 'positions' (list of (row, col) tuples).
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def dfs(row, col, color, positions):
        if (row, col) in visited or not (0 <= row < rows and 0 <= col < cols) or grid[row, col] != color:
            return
        visited.add((row, col))
        positions.append((row, col))
        dfs(row + 1, col, color, positions)
        dfs(row - 1, col, color, positions)
        dfs(row, col + 1, color, positions)
        dfs(row, col - 1, color, positions)

    for row in range(rows):
        for col in range(cols):
            if (row, col) not in visited:
                color = grid[row, col]
                positions = []
                dfs(row, col, color, positions)
                if positions:
                    objects.append({'color': color, 'positions': positions})
    return objects

def is_2x1_vertical_rectangle(positions):
    """
    Checks if the given positions form a 2x1 vertical rectangle.
    """
    if len(positions) != 2:
        return False
    row1, col1 = positions[0]
    row2, col2 = positions[1]
    return (col1 == col2) and (abs(row1 - row2) == 1)

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    For each 2x1 azure rectangle, add a blue (1) cell to the
    right of its top cell, and before its bottom cell.
    """
    output_grid = np.copy(input_grid)
    objects = find_objects(input_grid)

    for obj in objects:
        if obj['color'] == 8 and is_2x1_vertical_rectangle(obj['positions']):
            # Sort positions to ensure we get top and bottom cells correctly
            positions = sorted(obj['positions'])
            top_row, top_col = positions[0]
            bottom_row, bottom_col = positions[1]

            # Add blue cell to the right of the top cell
            if top_col + 1 < output_grid.shape[1]:
                output_grid[top_row, top_col + 1] = 1

            # Add blue cell before the bottom cell
            if bottom_col -1 >=0:
                 if bottom_row+1 == output_grid.shape[0]:
                    output_grid[bottom_row, bottom_col - 1] = 1
                 else:
                    output_grid[bottom_row, bottom_col-1] = 1
            elif bottom_col>=0 :
                if bottom_row+1 == output_grid.shape[0]:
                    output_grid[bottom_row, bottom_col] = 1
                else:
                    output_grid[bottom_row, bottom_col] = 1

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

![Image](005-example_2_input.png)


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

![Image](005-example_2_output.png)

Okay, let's analyze the transformation between the input and output grids for the second example.

**YAML Description of Observations**

```yaml
input_observations:
  objects:
    - color: 8 (azure)
      shape: Three separate 2x1 vertical rectangles and one 1x2 horizontal rectangle.
      positions:
        - Top right rectangle: (0,5)
        - Middle left rectangle: (2,2)
        - Bottom right rectangle: (5,5)
        - Bottom left rectangle: (6,3)
    - color: 0 (white)
      shape: Background
      positions:
        - All other cells

output_observations:
  objects:
    - color: 8 (azure)
      shape: Three separate 2x1 vertical rectangles and one 1x2 horizontal rectangle.
      positions:
        - Top right rectangle: (0,5)
        - Middle left rectangle: (2,2)
        - Bottom right rectangle: (5,5)
        - Bottom left rectangle: (6,3)
    - color: 1 (blue)
      shape: Three single cells.
      positions:
        - Next to top right rectangle: (1,5)
        - Next to middle left rectangle: (2,3)
        - Next to bottom right rectangle: (5,4)
    - color: 0 (white)
      shape: Background
      positions:
        - All other cells
```

**Natural Language Program: Step-by-step Transformation**

1.  **Identify Objects:** In the input grid, we have four distinct objects made of color 8 (azure). Three objects are 2x1 vertical rectangles and one object is a 1 x 2 horizontal rectangle. There are also background cells that are color 0.

2.  **Locate Key Positions:**

    *   The first azure rectangle starts at row 0, column 5.
    *   The second azure rectangle starts at row 2, column 2.
    *  The third azure rectangle starts at row 5, column 5.
    *   The forth azure rectangle starts at row 6, column 3.

3.  **Observe changes:** The azure rectangles remain unchanged. Three blue cells are added next to some of them.

4.  **Transformation Rule:** For each of the three azure (8) colored 2x1 vertical rectangles, add the value '1' to the right of the top cell of the vertical rectangle or to the left of the bottom cell of the rectangle. The 1 x 2 horizontal rectangle remains unchanged.

In summary, the rule involves keeping the existing 2x1 azure vertical rectangles and the 1x2 horizontal rectangle, and adding a new blue (1) cell to the right of the top cell of each vertical rectangle, or a blue cell to the left of the bottom cells.

```python
"""
The transformation rule involves keeping the existing 2x1 azure vertical rectangles and adding a new blue (1) cell to the right of their top cells, and a blue (1) cell before their bottom cell.
"""

import numpy as np

def find_objects(grid):
    """
    Finds contiguous regions of the same color and returns them as a list of objects.
    Each object is a dictionary with 'color' and 'positions' (list of (row, col) tuples).
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def dfs(row, col, color, positions):
        if (row, col) in visited or not (0 <= row < rows and 0 <= col < cols) or grid[row, col] != color:
            return
        visited.add((row, col))
        positions.append((row, col))
        dfs(row + 1, col, color, positions)
        dfs(row - 1, col, color, positions)
        dfs(row, col + 1, color, positions)
        dfs(row, col - 1, color, positions)

    for row in range(rows):
        for col in range(cols):
            if (row, col) not in visited:
                color = grid[row, col]
                positions = []
                dfs(row, col, color, positions)
                if positions:
                    objects.append({'color': color, 'positions': positions})
    return objects

def is_2x1_vertical_rectangle(positions):
    """
    Checks if the given positions form a 2x1 vertical rectangle.
    """
    if len(positions) != 2:
        return False
    row1, col1 = positions[0]
    row2, col2 = positions[1]
    return (col1 == col2) and (abs(row1 - row2) == 1)

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    For each 2x1 azure rectangle, add a blue (1) cell to the
    right of its top cell, and before its bottom cell.
    """
    output_grid = np.copy(input_grid)
    objects = find_objects(input_grid)

    for obj in objects:
        if obj['color'] == 8 and is_2x1_vertical_rectangle(obj['positions']):
            # Sort positions to ensure we get top and bottom cells correctly
            positions = sorted(obj['positions'])
            top_row, top_col = positions[0]
            bottom_row, bottom_col = positions[1]

            # Add blue cell to the right of the top cell
            if top_col + 1 < output_grid.shape[1]:
                output_grid[top_row, top_col + 1] = 1

            # Add blue cell before the bottom cell
            if bottom_col -1 >=0:
                 if bottom_row+1 == output_grid.shape[0]:
                    output_grid[bottom_row, bottom_col - 1] = 1
                 else:
                    output_grid[bottom_row, bottom_col-1] = 1
            elif bottom_col>=0 :
                if bottom_row+1 == output_grid.shape[0]:
                    output_grid[bottom_row, bottom_col] = 1
                else:
                    output_grid[bottom_row, bottom_col] = 1

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
