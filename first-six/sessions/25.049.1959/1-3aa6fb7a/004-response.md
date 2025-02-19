# 1-3aa6fb7a • 004 • example_2 - CODE

---
```python
"""
Transformation Rule: For each azure (color 8) L-shaped object in the input grid, a blue (color 1) cell is added to their north-east, considering the most western cell of each azure shape.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds objects of a specific color in the grid.
    Returns a list of coordinates (top-left cell) of each object.
    For simplicity, this function identifies each isolated groups of cells
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return []
        visited.add((r, c))
        cluster = [(r, c)]
        # Explore adjacent cells (including diagonals)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                cluster.extend(dfs(r + dr, c + dc))
        return cluster

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                cluster = dfs(r, c)
                #find most western cell
                most_western_cell = cluster[0]
                for cell in cluster:
                    if cell[1] < most_western_cell[1]:
                        most_western_cell = cell
                objects.append(most_western_cell)

    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    For each azure (color 8) L-shaped object, a blue (color 1) cell is added
    to their north-east, considering the most western cell of each azure shape.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    # Add a blue cell to the specified position relative to each azure object
    for r, c in azure_objects:
        new_r, new_c = r,c+1
        if 0 <= new_r < output_grid.shape[0] and 0 <= new_c < output_grid.shape[1]:
          output_grid[new_r, new_c] = 1
        

    return output_grid
```

