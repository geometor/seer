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

![Image](000-example_1_input.png)


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

![Image](000-example_1_output.png)

Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Observation:**

```yaml
observations:
  input_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: L-shape (two instances)
        positions:
          - top-left corner: [1,1] (2x2 block with one cell removed)
          - bottom-right corner: [3,4] (2x2 block with one cell removed)
      - color: 0 (white)
        shape: background
        position: fills the remaining cells
  output_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: L-shape (two instances)
        positions:
          - top-left corner: [1,1] (2x2 block with one cell removed)
          - bottom-right corner: [3,4] (2x2 block with one cell removed)
      - color: 1 (blue)
        shape: single cell
        positions:
          - [1,2] #next to the top object
          - [4,5] #next to the bottom object
      - color: 0 (white)
        shape: background
        position: fills the remaining cells
```

**Natural Language Program:**

1.  **Identify Objects:** Locate all instances of color 8 (azure) objects in the input grid. Note their positions. These objects form an "L" shape, consisting of a 2x2 block with one cell removed.

2.  **Preserve Objects:** Keep every object of color 8 in its original position in the output grid.

3.  **Introduce New Objects:** Add new objects to the grid.
    *    To the right of the top left object 8, introduce a single cell of color 1 (blue) if and only if the cell to the right of the object is color 0.
    *    To the left of the bottom right object 8, introduce a single cell of color 1 (blue) if and only if the cell to the left of the object is color 0.

In summary, the transformation preserves the azure "L" shaped objects and adds a blue cell adjacent to each, based on the initial positions of these shapes, with the added blue cells located on opposite sides.

```python
"""
Preserves the azure "L" shaped objects and adds a blue cell adjacent to each, based on the initial positions of these shapes, with the added blue cells located on opposite sides.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds the coordinates of objects of a specific color.
    An object is defined as a contiguous region of the same color.
    """
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        if (r, c) in visited or r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        # Check all 4 directions
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
        # Sort the coordinates to identify top-left and bottom-right objects
        obj.sort()
        
        if len(obj) == 3: # Check that it is the "L" shape
            # Determine if it's top-left or bottom-right based on coordinates
            # Top-left object: min row and min col
            # Bottom-right object: max row and max col
            # The L-shape objects in question don't follow the top-leftmost or bottom-rightmost logic strictly.
            # Instead, we'll check the relative positions of the azure cells directly

            min_row = min(r for r, c in obj)
            min_col = min(c for r, c in obj)
            max_row = max(r for r, c in obj)
            max_col = max(c for r, c in obj)

            # Assuming that the orientation is deterministic, it is not needed to be adaptive to new orientations.
            if obj == sorted([(min_row,min_col), (min_row, min_col+1), (min_row+1, min_col)]): #top-left
                # Add blue cell to the right
              if min_row >= 0 and min_row < output_grid.shape[0] and min_col + 2 >= 0 and min_col + 2 < output_grid.shape[1]:
                if output_grid[min_row, min_col + 2] == 0:
                  output_grid[min_row, min_col + 2] = 1

            elif obj == sorted([(max_row-1, max_col), (max_row, max_col-1), (max_row, max_col)]): # bottom-right
                # Add blue cell to the left
              if max_row >= 0 and max_row < output_grid.shape[0] and max_col-2 >=0 and max_col-2 < output_grid.shape[1]:
                if output_grid[max_row, max_col - 2] == 0:
                    output_grid[max_row, max_col - 2] = 1

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

![Image](002-example_2_input.png)


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

![Image](002-example_2_output.png)

Okay, let's analyze the transformation from the input grid to the output grid in the second example.

**YAML Observation:**

```yaml
observations:
  input_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: L-shape (two instances)
        positions:
          - top-right corner: [0,4] (2x2 block with one cell removed)
          - middle-left: [2,2] (2x2 block with one cell removed)
          - bottom-right: [5,4]
        notes: The L-shape objects appear in different places compared with the first example.
      - color: 0 (white)
        shape: background
        position: fills the remaining cells
  output_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: L-shape (three instances)
        positions:
          - top-right corner: [0,4] (2x2 block with one cell removed)
          - middle-left: [2,2] (2x2 block with one cell removed)
          - bottom-right: [5,4]
        notes: The objects remain in the same position as the input.
      - color: 1 (blue)
        shape: single cell
        positions:
          - [1,5] #next to the top-right object
          - [2,3] #next to the middle-left object
          - [5,3] #next to the bottom-right object.
        notes: A blue cell is added next to object 8.
      - color: 0 (white)
        shape: background
        position: fills the remaining cells
```

**Natural Language Program:**

1.  **Identify Objects:** Locate all instances of color 8 (azure) objects in the input grid. These objects form an "L" shape, consisting of a 2x2 block with one cell removed.

2.  **Preserve Objects:** Maintain every object of color 8 in its original position in the output grid.

3.  **Introduce New Objects:** Add new objects to the grid:
    *   To the right of the top right object 8, introduce a single cell of color 1 (blue) if the cell to the right of the object is 0.
    *   To the left of the middle left object 8, introduce a single cell of color 1 (blue) if the cell to the left of the object is 0.
    *   To the left of the bottom right object 8, introduce a single cell of color 1 (blue) if the cell to the left of the object is 0.

In essence, the transformation keeps the positions of the azure "L" shaped objects unchanged and adds a blue cell adjacent to some of them, depending on the relative position, specifically to the left or right.

The python implementation is the same.

```python
"""
Preserves the azure "L" shaped objects and adds a blue cell adjacent to each, based on the initial positions of these shapes, with the added blue cells located on opposite sides.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds the coordinates of objects of a specific color.
    An object is defined as a contiguous region of the same color.
    """
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        if (r, c) in visited or r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        # Check all 4 directions
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
        # Sort the coordinates to identify top-left and bottom-right objects
        obj.sort()
        
        if len(obj) == 3: # Check that it is the "L" shape
            # Determine if it's top-left or bottom-right based on coordinates
            # Top-left object: min row and min col
            # Bottom-right object: max row and max col
            # The L-shape objects in question don't follow the top-leftmost or bottom-rightmost logic strictly.
            # Instead, we'll check the relative positions of the azure cells directly

            min_row = min(r for r, c in obj)
            min_col = min(c for r, c in obj)
            max_row = max(r for r, c in obj)
            max_col = max(c for r, c in obj)

            # Assuming that the orientation is deterministic, it is not needed to be adaptive to new orientations.
            if obj == sorted([(min_row,min_col), (min_row, min_col+1), (min_row+1, min_col)]): #top-left
                # Add blue cell to the right
              if min_row >= 0 and min_row < output_grid.shape[0] and min_col + 2 >= 0 and min_col + 2 < output_grid.shape[1]:
                if output_grid[min_row, min_col + 2] == 0:
                  output_grid[min_row, min_col + 2] = 1

            elif obj == sorted([(max_row-1, max_col), (max_row, max_col-1), (max_row, max_col)]): # bottom-right
                # Add blue cell to the left
              if max_row >= 0 and max_row < output_grid.shape[0] and max_col-2 >=0 and max_col-2 < output_grid.shape[1]:
                if output_grid[max_row, max_col - 2] == 0:
                    output_grid[max_row, max_col - 2] = 1

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
