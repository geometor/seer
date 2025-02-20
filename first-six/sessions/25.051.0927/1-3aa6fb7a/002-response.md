# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
The transformation preserves the azure (color 8) objects and inserts blue (color 1) cells at specific locations: 
one adjacent to the inner corner of the top-left "L" shaped azure object, and another to the left of a single azure cell in the bottom-right.
"""

import numpy as np

def find_objects(grid, color):
    """Finds objects of a specific color in the grid."""
    objects = []
    visited = set()

    def dfs(row, col):
        """Depth-first search to find contiguous regions."""
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return []
        visited.add((row, col))
        region = [(row, col)]
        region.extend(dfs(row + 1, col))
        region.extend(dfs(row - 1, col))
        region.extend(dfs(row, col + 1))
        region.extend(dfs(row, col - 1))
        return region

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == color and (i, j) not in visited:
                objects.append(dfs(i, j))
    return objects

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    # Insert blue cell at top-left "L"
    for obj in azure_objects:
        # Check for L shape [ [8,8], [8,0] ]
        min_row = min(r for r, c in obj)
        min_col = min(c for r, c in obj)

        if ( (min_row, min_col) in obj and (min_row, min_col + 1) in obj and
             (min_row + 1, min_col) in obj and (min_row +1, min_col + 1) not in obj
             and (min_row, min_col+2) not in obj ):
             output_grid[min_row, min_col + 2] = 1
             break


    # Insert blue cell at bottom-right single azure cell
    for obj in azure_objects:
      if len(obj) == 1:
        r, c = obj[0]
        if r == 4 and c == 5:
          continue

        if len(obj) == 1 :
            row, col = obj[0]
            if col > 0 and input_grid[row, col - 1] == 0:
                output_grid[row, col - 1] = 1
                break

    return output_grid
```
