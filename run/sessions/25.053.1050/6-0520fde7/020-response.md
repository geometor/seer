# 6-0520fde7 • 020 • refine_coder

---
```python
"""
1.  **Excise:** Remove the fourth column (the gray column) from the input grid.
2.  **Condense:** Create a 3x3 output grid. For each row, select the first three non-gray color values to fill output.
3. **Color Conversion:** Examine each cell in the *output* grid.
   * Change cell to red if:
     * Output cell is blue
     * Output cell is not at an edge of the grid
     * The cell immediately to the left and right of the cell are not blue
     * The cell immediately to the top and bottom of the cell are not blue
"""

import numpy as np

def get_neighbors(grid, r, c):
    neighbors = []
    if r > 0:
        neighbors.append(grid[r-1][c])  # Up
    if r < len(grid) - 1:
        neighbors.append(grid[r+1][c])  # Down
    if c > 0:
        neighbors.append(grid[r][c-1])  # Left
    if c < len(grid[0]) - 1:
        neighbors.append(grid[r][c+1])  # Right
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


    # 3. Color Conversion: Check for blue pixels and their neighbors.
    for r in range(3):
        for c in range(3):
            if output_grid[r, c] == 1:
                neighbors = get_neighbors(output_grid, r, c)
                
                # Check for transitions on opposite sides
                is_horizontally_surrounded = (c > 0 and c < 2 and output_grid[r, c-1] != 1 and output_grid[r, c+1] != 1)
                is_vertically_surrounded = (r > 0 and r < 2 and output_grid[r-1, c] != 1 and output_grid[r+1, c] != 1)

                if is_horizontally_surrounded or is_vertically_surrounded:
                  output_grid[r,c] = 2

    return output_grid
```
