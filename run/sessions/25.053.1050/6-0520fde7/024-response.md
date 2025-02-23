# 6-0520fde7 • 024 • refine_coder

---
```python
"""
1.  **Excise:** Remove the fourth column (containing only gray pixels) from the input grid.
2.  **Condense:** Create a 3x3 output grid. For each row in the modified input grid, select the first three non-gray color values and use them to form the corresponding row in the output grid.
3.  **Conditional Color Conversion:** Iterate through the 3x3 *output* grid. If a cell is blue, check the following:
    *   IF a pixel in the first or third column is BLUE:
        *   IF it has a horizontally adjacent neighbor that is NOT blue (1), change it to red (2).
        *   IF it has a horizontally adjacent neighbor that is IS blue (1), keep it as blue (1).
"""

import numpy as np

def get_horizontal_neighbors(grid, r, c):
    """Gets the horizontal neighbors of a cell in a grid."""
    neighbors = []
    rows, cols = grid.shape
    if c > 0:
        neighbors.append(grid[r, c-1])
    if c < cols - 1:
        neighbors.append(grid[r, c+1])
    return neighbors

def transform(input_grid):
    # initialize output_grid
    grid = np.array(input_grid)

    # 1. Excise Column: Remove the fourth column (index 3).
    grid = np.delete(grid, 3, axis=1)

    # 2. Condense: Create 3x3, taking first three non-gray values in each row.
    output_grid = np.zeros((3, 3), dtype=int)
    for i in range(3):
        non_gray_cols = [val for val in grid[i] if val != 5]
        output_grid[i] = non_gray_cols[:3]


    # 3. Color Conversion: Check for blue pixels and their column.
    for r in range(3):
        for c in range(3):
            if output_grid[r, c] == 1:  # If the cell is blue
                if c == 0 or c == 2: # and in the first or third column
                  neighbors = get_horizontal_neighbors(output_grid,r,c)
                  if any(neighbor != 1 for neighbor in neighbors):
                    output_grid[r,c] = 2


    return output_grid
```
