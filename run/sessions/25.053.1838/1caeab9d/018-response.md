# 1caeab9d • 018 • refine_coder

---
```python
"""
1.  **Identify Connected Components:** Scan the input grid to identify all vertically connected components. A vertically connected component is a group of one or more pixels of the same color that are directly adjacent to each other in the same column.
2.  **Merge to single row:** Merge each vertically connected group into a single combined row.
3. **Shift Down:** shift each merged row down, adding blank rows at the top until the correct row count is achieved.
"""

import numpy as np

def get_vertical_components(grid):
    """Identifies vertically connected components in the grid."""
    rows, cols = grid.shape
    components = []
    visited = np.zeros((rows, cols), dtype=bool)

    def dfs(r, c, color, component):
        if r < 0 or r >= rows or c < 0 or c >= cols or visited[r, c] or grid[r, c] != color:
            return
        visited[r, c] = True
        component.append((r, c))
        dfs(r + 1, c, color, component)  # Check only downwards

    for r in range(rows):
        for c in range(cols):
            if not visited[r, c] and grid[r,c] != 0:
                component = []
                dfs(r, c, grid[r, c], component)
                if component:
                    components.append(component)
    return components

def transform(input_grid):
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # 1. Identify Connected Components
    components = get_vertical_components(input_grid)
    
    # 2. Merge components to a single row
    merged_rows = []
    for component in components:
        first_cell = component[0]
        merged_rows.append(input_grid[first_cell[0],first_cell[1]])


    # 3. shift merged components
    start_row = rows - len(merged_rows)
    for i, val in enumerate(merged_rows):
      if start_row + i < rows:
        output_grid[start_row + i, i] = val


    return output_grid.tolist()
```
