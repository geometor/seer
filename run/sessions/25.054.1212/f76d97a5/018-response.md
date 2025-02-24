# f76d97a5 • 018 • refine_coder

---
```python
"""
1.  Iterate through each cell in the input grid.
2.  Identify the color of the current cell.
3.  Check Adjacency: For each cell, check if it's adjacent (up, down, left, or right) to a cell of a specific color based on these rules:
4.  Transformation Rules:
    *   If the current cell is gray (5), it becomes black (0), regardless of surrounding colors.
    *   If the current cell is yellow (4) and is adjacent to gray (5), it becomes black (0).
    *   If the current cell is maroon (9) and is adjacent to gray (5), it becomes black (0).
    *   If the current cell is magenta (6), it remains unchanged.
    *  All other colors remain unchanged
"""

import numpy as np

def is_adjacent_to_color(grid, r, c, target_color):
    """Checks if cell at (r,c) is adjacent to a cell of target_color"""
    rows, cols = grid.shape
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr, nc] == target_color:
                return True
    return False

def transform(input_grid):
    # initialize output_grid as a copy of the input grid.
    output_grid = input_grid.copy()
    rows, cols = input_grid.shape

    # iterate through each cell
    for r in range(rows):
        for c in range(cols):
            #apply transformation rules
            if input_grid[r,c] == 5:
                output_grid[r,c] = 0
            elif input_grid[r,c] == 4 and is_adjacent_to_color(input_grid, r,c, 5):
                output_grid[r,c] = 0
            elif input_grid[r,c] == 9 and is_adjacent_to_color(input_grid, r,c, 5):
                output_grid[r,c] = 0
            # color 6 is always unchanged
            # other colors are unchanged by default because of copy

    return output_grid
```
