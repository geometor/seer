# 1-3aa6fb7a • 005 • refine_code - CODE

---

Previous Code:
```python
import numpy as np

def find_contiguous_objects(grid, color):
    """
    Finds contiguous objects of a given color in the grid.

    Args:
    grid (numpy.ndarray): The input grid.
    color (int): The color to look for.

    Returns:
    list: A list of lists, where each inner list contains (row, col) tuples
          representing a contiguous object.
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
        # Check all 8 neighbors (including diagonals)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                dfs(r + dr, c + dc, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def find_isolated_cells(grid, color):
    """Finds isolated cells of a given color, considering diagonal adjacency."""
    objects = find_contiguous_objects(grid, color)
    isolated_cells = []
    for obj in objects:
        if len(obj) == 1:
            isolated_cells.extend(obj)  # Use extend since obj is a list of tuples
    return isolated_cells

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find isolated azure (color 8) cells
    isolated_azure_cells = find_isolated_cells(input_grid, 8)

    # Sort isolated cells by row to distinguish top and bottom
    isolated_azure_cells.sort()

    # Apply the transformation based on the position of isolated azure cells
    if len(isolated_azure_cells) >= 1:
        # Top isolated azure cell: place blue cell to the right
        top_azure_row, top_azure_col = isolated_azure_cells[0]
        if top_azure_col + 1 < cols:  # Check bounds
            output_grid[top_azure_row, top_azure_col + 1] = 1

    if len(isolated_azure_cells) >= 2:

        # Bottom isolated azure cell: place blue cell to the left
        bottom_azure_row, bottom_azure_col = isolated_azure_cells[-1]
        if bottom_azure_col - 1 >= 0:  # Check bounds
            output_grid[bottom_azure_row, bottom_azure_col - 1] = 1

    return output_grid
```

Train Set Results:

**Example 1:**
Input:
```
0 0 0 0 0 0 0
0 8 0 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```
Expected Output:
```
0 0 0 0 0 0 0
0 8 1 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```
Transformed Output:
```
0 0 0 0 0 0 0
0 8 0 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```
![Transformed Image](003-py_02-train-example_1.png)
Status: False

**Example 2:**
Input:
```
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 8 0 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 0 8 0 0
0 0 0 8 8 0 0
```
Expected Output:
```
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 8 1 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 1 8 0 0
0 0 0 8 8 0 0
```
Transformed Output:
```
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 8 0 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 0 8 0 0
0 0 0 8 8 0 0
```
![Transformed Image](003-py_02-train-example_2.png)
Status: False
Okay, let's analyze the transformation rule based on the provided examples.

**YAML Description of Observations**

```yaml
observations:
  example_1:
    input:
      objects:
        - color: 8 (azure)
          instances:
            - shape: single cell
              position: (1, 1) # row, col
            - shape: L-shape (2x2 block missing one cell)
              position: Top-left corner at (2, 1)
            - shape: L-shape (2x2 block missing one cell)
              position: Top-left corner at (3, 4)
            - shape: single cell
              position: (4, 5)
      
    output:
        objects:
        - color: 8 (azure)
          instances:
            - shape: single cell
              position: (1, 1)
            - shape: L-shape (2x2 block missing one cell)
              position:  Top-left corner at (2, 1)
            - shape: L-shape (2x2 block missing one cell)
              position: Top-left corner at (3, 4)
            - shape: single cell
              position: (4, 5)
        - color: 1 (blue)
          instances:
            - shape: single cell
              position: (1,2)
            - shape: single cell
              position: (4,4)
  example_2:
    input:
      objects:
       - color: 8
         instances:
           - shape: L (two cells)
             position: Top-left at (0, 4)
           - shape: single
             position: (1, 5)
           - shape: single
             position: (2, 2)
           - shape: L (two cells)
             position: Top-left at (3, 2)
           - shape: single
             position: (5, 4)
           - shape: L (two cells)
             position: Top-left at (6,3)
    output:
      objects:
       - color: 8
         instances:
           - shape: L (two cells)
             position: Top-left at (0, 4)
           - shape: single
             position: (1, 5)
           - shape: single
             position: (2, 2)
           - shape: L (two cells)
             position: Top-left at (3, 2)
           - shape: single
             position: (5, 4)
           - shape: L (two cells)
             position: Top-left at (6,3)
       - color: 1
         instances:
           - shape: single
             position: (1, 4)
           - shape: single
             position: (2,3)
           - shape: single
             position: (5,3)
```

**Natural Language Program (Transformation Rule)**

1.  **Identify Isolated Azure Cells:** Locate all isolated azure (color 8) cells in the input grid. An isolated cell is one that has no adjacent cells of the same color, including diagonals.

2.  **Sort by Row:** Sort the identified isolated azure cells by their row number, from top to bottom.

3.  **Topmost Isolated Azure:** For the topmost isolated azure cell, place a blue (color 1) cell directly to its *right*.

4. **All other Isolated Azure:** For every other isolated azure cell, place a blue (color 1) cell directly to the *left*.

5.  **Boundary Conditions:** Ensure that when placing blue cells, we do not exceed the boundaries of the grid. If placing a blue cell would go out of bounds, skip that placement.

The previous code was close but missed key parts of the rule: It only dealt with "Top" and "Bottom", but did not place to the left of *every other* isolated azure object. It also used the last object, instead of placing it relative to each object.

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
{{ natural language description of the transformation rule }}
"""

{{ imports }}

def transform(input_grid):
    # initialize output_grid

    # change output pixels 

    return output_grid

```
