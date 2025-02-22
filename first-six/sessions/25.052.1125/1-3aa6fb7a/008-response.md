# 1-3aa6fb7a • 008 • refine_code - CODE

---
```python
"""
The transformation rule identifies azure (8) objects and places blue (1) cells adjacent to them based on their shape. Vertical lines get a blue cell to the right of the top cell. Horizontal lines get a blue cell to the left of the rightmost cell. L-shapes get a blue cell above the corner if the corner is at the top. Other shapes are ignored. Boundary checks prevent out-of-bounds placement.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        if (r, c) in visited or r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or grid[r, c] != color:
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
    # Initialize output_grid as a copy of the input
    output_grid = np.copy(input_grid)
    # Find all azure objects
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
        # Sort object cells for easier processing
        obj.sort(key=lambda x: (x[0], x[1]))
        rows = [cell[0] for cell in obj]
        cols = [cell[1] for cell in obj]

        # Check if it's a vertical line
        if len(set(cols)) == 1 and len(obj) > 1:
            top_cell = obj[0]
            # Boundary check for placing blue cell to the right
            if top_cell[1] + 1 < output_grid.shape[1]:
              output_grid[top_cell[0], top_cell[1] + 1] = 1

        # Check if it's a horizontal line
        elif len(set(rows)) == 1 and len(obj) > 1:
            right_cell = obj[-1]
            # Boundary check for placing blue cell to the left
            if right_cell[1] - 1 >= 0:
                output_grid[right_cell[0], right_cell[1] - 1] = 1

        # Check if it's an L-shape
        elif len(obj) == 3:
            # Find the corner cell by counting row and column occurrences
            row_counts = {}
            col_counts = {}
            for r in rows:
                row_counts[r] = row_counts.get(r, 0) + 1
            for c in cols:
                col_counts[c] = col_counts.get(c, 0) + 1

            corner_row = [r for r, count in row_counts.items() if count > 1][0]
            corner_col = [c for c, count in col_counts.items() if count > 1][0]
            
            # Place blue cell above the corner if it's a top corner and within bounds
            if corner_row > min(rows) and corner_row -1 >= 0:
              output_grid[corner_row - 1, corner_col] = 1

    return output_grid
```

