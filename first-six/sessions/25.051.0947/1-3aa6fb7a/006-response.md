# 1-3aa6fb7a • 006 • example_2 - CODE

---
Okay, let's analyze the provided input and output grids to determine the transformation rule.

**YAML Observation:**

```yaml
observations:
  input_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        positions: [(1, 1), (2, 1), (2, 2), (3, 4), (3, 5), (4, 5)]
        shape: Two separate azure blocks, one vertical (2x1) and one horizontal (1x2).
  output_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        positions: [(1, 1), (2, 1), (2, 2), (3, 4), (3, 5), (4, 5)]
        shape: Same as input.
      - color: 1 (blue)
        positions: [(1, 2), (4, 4)]
        shape: Two single blue cells.
```

**Natural Language Program:**

The transformation rule appears to be:

1.  **Preserve Azure:** Copy all azure (color 8) objects from the input grid to the output grid without any changes in position or shape.

2.  **Add Blue - Top:** Identify the azure object that has the smallest row number (uppermost). If multiple objects share the smallest row number, choose the one with smallest column.  Place a blue pixel (color 1) immediately to the right of the rightmost cell of this azure object.

3.  **Add Blue - Bottom:** Identify the azure object that has the largest row number (lowest). If multiple objects share the largest row number, choose the one with the smallest column. Place a blue pixel (color 1) immediately to the left of the leftmost cell of this object.

```python
"""
The transformation rule is:

1. Preserve Azure: Copy all azure (color 8) objects from the input grid to the output grid without changes.

2. Add Blue - Top: Find the uppermost azure object. Place a blue pixel (color 1) to the right of its rightmost cell.

3. Add Blue - Bottom: Find the lowermost azure object. Place a blue pixel (color 1) to the left of its leftmost cell.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = set()

    def dfs(row, col, current_object):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return
        visited.add((row, col))
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and (row, col) not in visited:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    # Find uppermost object
    if azure_objects:
      uppermost_object = min(azure_objects, key=lambda obj: (min(r for r, c in obj), min(c for r, c in obj)))
      rightmost_cell = max(uppermost_object, key=lambda cell: cell[1])
      if rightmost_cell[1] + 1 < output_grid.shape[1]:
        output_grid[rightmost_cell[0], rightmost_cell[1] + 1] = 1

    # Find lowermost object
      lowermost_object = max(azure_objects, key=lambda obj: (max(r for r, c in obj), min(c for r, c in obj)))
      leftmost_cell = min(lowermost_object, key=lambda cell: cell[1])
    
      if leftmost_cell[1] -1 >= 0:
        output_grid[leftmost_cell[0], leftmost_cell[1] - 1] = 1

    return output_grid
```

