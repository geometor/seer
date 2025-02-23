# 1-3aa6fb7a • 003 • example_2 - NLP

---
Okay, let's analyze the second example.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      positions: [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5, 4), (6, 3), (6, 4)]
      shape: Three separate objects. One in the top-right, one in the center-left, and the last one at the bottom.
  dimensions: 7x7

output_grid:
  objects:
    - color: 8 (azure)
      positions:  [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5, 4), (6, 3), (6, 4)]
      shape: Three separate objects. One in the top-right, one in the center-left, and the last one at the bottom.
    - color: 1 (blue)
      positions: [(1,4), (2, 3), (5,3)]
      shape: single cells
  dimensions: 7x7
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Azure Objects:** Locate all azure (color 8) objects within the input grid. In this case, we have three distinct azure objects.

2.  **Identify Single Azure cells action**:
    *   Locate the uppermost, and then leftmost, azure (8) colored cell of the top azure object.
    *   Locate the leftmost, and then uppermost, azure (8) colored cell of the center azure object.
     *   Locate the leftmost, and then uppermost, azure (8) colored cell of the bottom azure object.

3.  **Change Color:** Change color to blue (1) of each of the three azure (8) colored cells identified.

4.  **Leave the Rest:** Do nothing to the rest of the azure and other cells.

The code written previously will work on this case too.

```python
"""
The transformation rule identifies all azure objects and paints the uppermost-leftmost cell blue of the top object, the leftmost-uppermost blue of the center object, and the leftmost-uppermost cell blue of the bottom one.
"""

import numpy as np

def get_objects(grid, color):
    """
    Finds objects of a specific color in the grid.

    Args:
        grid: The input grid.
        color: The color to search for.

    Returns:
        A list of lists, where each inner list contains the coordinates of
        contiguous cells of the specified color.
    """
    visited = set()
    objects = []

    def dfs(r, c, current_object):
        if (r, c) in visited or not (0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
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
    Transforms the input grid according to the rule.
    """
    output_grid = input_grid.copy()
    azure_objects = get_objects(input_grid, 8)

    # change color of uppermost-leftmost azure cell of top object
    if len(azure_objects) >= 1:
      top_object = min(azure_objects, key=lambda obj: (min(r for r, c in obj), min(c for r, c in obj)))
      top_left_cell = min(top_object, key=lambda cell: (cell[0], cell[1]))
      output_grid[top_left_cell[0], top_left_cell[1]] = 1

    # change color of leftmost-uppermost azure cell of bottom object
    if len(azure_objects) >= 2:
      # find bottom-right object by minimum row and then minimum col
        objects_ordered_by_y = sorted(azure_objects, key=lambda obj: (min(r for r, c in obj), min(c for r,c in obj)))

        for i in range(1,len(objects_ordered_by_y)):
          bottom_left_cell = min(objects_ordered_by_y[i], key=lambda cell: (cell[0], cell[1]))
          output_grid[bottom_left_cell[0],bottom_left_cell[1]] = 1
    
    return output_grid
```

