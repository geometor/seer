# 1-3aa6fb7a • 004 • example_2 - CODE

---
Okay, I've analyzed both examples and I think I've identified a consistent pattern. Here's the breakdown:

**YAML Block: Observations (Combined)**

```yaml
input_grids:
  example_1:
    objects:
      - color: 8 (azure)
        positions: [(1, 1), (2, 1), (2, 2), (3, 4), (3, 5), (4, 5)]
        shape: Two separate L-shapes (one inverted)
  example_2:
     objects:
      - color: 8
        positions: [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5, 4), (6, 3), (6, 4)]
        shape: Three L-shapes
output_grids:
  example_1:
      objects:
    - color: 8 (azure)
      positions: [(1, 1), (2, 1), (2, 2), (3, 4), (3, 5), (4, 5)]
    - color: 1 (blue)
      positions: [(1,2), (4,4)]
  example_2:
    objects:
    - color: 8
      positions:  [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5, 4), (6, 3), (6, 4)]
    - color: 1
      positions: [(1,4), (2,3), (5,3)]
```

**Natural Language Program: Transformation Rule (Generalized)**

1.  **Identify Azure Objects:** Find all connected regions (objects) of color 8 (azure) in the input grid.  The examples suggest these are always L-shaped and consist of 3 cells.

2.  **Categorize Azure Objects:**  The placement of the blue cells (1) depends on the relative position of the azure (8) objects. We need to identify them consistently. Sorting them by the row and then column of their top-most cell seems to provide a consistent categorization. We consider three possible cases:

    *   **"Top-Left/First" Object:** If a white cell (0) exists immediately to the *right* of the *topmost* cell of this object, change it to blue (1).
    *   **"Bottom-Right/Last" Object:** If a white cell (0) exists immediately to the *left* of the *bottommost* cell of this object, change it to blue (1).
    *  **"Middle" Object:** If the above two are not enough to describe all the changes (as in the second example), and if any of the above conditions are not met, find the "middle" object.
     * if the previous cases are not met, change the white cell(0) to the *left* of the *top-most* cell of the object to blue(1).

3.  **Preservation:** All other cells remain unchanged.

**Informal predicates and actions**

*   **Predicates:**
    *   `is_azure(cell)`: Checks if a cell is colored azure (8).
    *   `is_white(cell)`: Checks if a cell is colored white (0).
    *  `top_cell(object)`: Returns the highest cell of object.
    *  `bottom_cell(object)`: Returns the lowest cell of object.
    *   `to_the_right_of(cell1, cell2)`: Checks if `cell2` is directly to the right of `cell1`.
    *   `to_the_left_of(cell1, cell2)`: Checks if `cell2` is directly to the left of `cell1`.

*   **Actions:**
    *   `change_color(cell, new_color)`: Changes the color of a cell.
    *   `find_objects(grid, color)`: Returns a list of cells composing an object of a specific color.
    *  `sort_objects(objects)`: Sort the objects, first by row number, then by column number.

```python
"""
The transformation rule identifies all azure (8) L-shaped objects in the input grid.
It then changes the color of specific white (0) cells to blue (1) based on their position relative to these azure objects.

- For the "top-left/first" azure object (when sorted by top cell row, then column),
  it changes the white cell to the right of its topmost cell to blue.

- For the "bottom-right/last" azure object,
  it changes the white cell to the left of its bottommost cell to blue.
- If the two rules don't apply to an object:
  - For a "middle" object,
      change the cell to the left of the top-most cell.

All other cells remain unchanged.
"""

import numpy as np

def find_objects(grid, color):
    """Finds connected regions of the specified color."""
    visited = np.zeros_like(grid, dtype=bool)
    objects = []

    def dfs(row, col, current_object):
        """Depth-first search to find connected cells."""
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != color
        ):
            return
        visited[row, col] = True
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def get_top_cell(obj):
    """Returns the cell with the smallest row value (top-most)."""
    return min(obj, key=lambda cell: cell[0])

def get_bottom_cell(obj):
    """Returns the cell with the largest row value."""
    return max(obj, key=lambda cell: cell[0])

def sort_objects(objects):
     """Sorts objects based on top-left corner's row, then column."""
     return sorted(objects, key=lambda obj: (get_top_cell(obj)[0], get_top_cell(obj)[1]))

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)
    sorted_azure_objects = sort_objects(azure_objects)

    for i, obj in enumerate(sorted_azure_objects):
        top_cell = get_top_cell(obj)
        bottom_cell = get_bottom_cell(obj)
        changed = False #flag

        # "Top-Left/First" object rule
        if i == 0:
            right_of_top = (top_cell[0], top_cell[1] + 1)
            if (
                0 <= right_of_top[0] < output_grid.shape[0]
                and 0 <= right_of_top[1] < output_grid.shape[1]
                and output_grid[right_of_top] == 0
            ):
                output_grid[right_of_top] = 1
                changed = True

        # "Bottom-Right/Last" object rule
        if i == len(sorted_azure_objects) - 1:
            left_of_bottom = (bottom_cell[0], bottom_cell[1] - 1)
            if (
                0 <= left_of_bottom[0] < output_grid.shape[0]
                and 0 <= left_of_bottom[1] < output_grid.shape[1]
                and output_grid[left_of_bottom] == 0
            ):
                output_grid[left_of_bottom] = 1
                changed = True

        # "Middle Object"
        if (not changed):
             left_of_top = (top_cell[0], top_cell[1] - 1)
             if (
                0 <= left_of_top[0] < output_grid.shape[0]
                and 0 <= left_of_top[1] < output_grid.shape[1]
                and output_grid[left_of_top] == 0
            ):
                output_grid[left_of_top] = 1


    return output_grid
```

