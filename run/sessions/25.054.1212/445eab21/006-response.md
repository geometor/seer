# 445eab21 • 006 • refine_coder

---
```python
"""
1. Find all 2x2 Squares: Scan the input grid and identify *all* 2x2 squares
   consisting of the same color. Record the color of each square found.
2. Match with Output (If Possible): If any of the colors found in step 1
   match a color in the example output, create a 2x2 output grid using that
   color.
3. Return: Return the 2x2 grid.
"""

import numpy as np

def find_all_2x2_squares(grid):
    """Finds all colors that form 2x2 squares in the grid."""
    grid = np.array(grid)
    rows, cols = grid.shape
    found_colors = set()
    for i in range(rows - 1):
        for j in range(cols - 1):
            color = grid[i, j]
            if (grid[i + 1, j] == color and
                grid[i, j + 1] == color and
                grid[i + 1, j + 1] == color):
                found_colors.add(color)
    return found_colors

def transform(input_grid):
    # Find all colors that make up 2x2 squares
    colors = find_all_2x2_squares(input_grid)

    # if colors are found, return the first one, otherwise, black (0)
    if colors:
      output_color = list(colors)[0]
      output_grid = np.full((2, 2), output_color, dtype=int)
    else:
      output_grid = np.zeros((2, 2), dtype=int)

    return output_grid.tolist()
```
