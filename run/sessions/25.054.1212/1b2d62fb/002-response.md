# 1b2d62fb • 002 • example_1 • investigate_coder

---
```python
"""
1.  **Identify** the vertical line of blue (1) pixels in the input grid.
2.  **Extract** a 5x3 section of the input grid. The section contains only white and the two azure cells.
3.  **Locate** where the vertical blue line would be, at the center.
4.  **Substitute**: Create two azure cells side by side where the center of the blue vertical line was.
5.  **Return** the final 5x3 grid
"""

import numpy as np

def find_vertical_line(grid, color):
    # Find columns where all elements are of the specified color
    rows, cols = grid.shape
    for j in range(cols):
        if all(grid[i,j] == color for i in range(rows)):
            return j
    return -1 #not found

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, 3), dtype=int)
    
    # Find the vertical line of color 1 (blue).
    blue_column = find_vertical_line(input_grid, 1)

    # Determine the center column
    # Extract 5x3, with two azure cells.
    if blue_column !=-1:
      center_column = 1 # will place the azure cells on cols 1 and 2.
      output_grid[rows//2, center_column] = 8
      output_grid[rows//2, center_column+1] = 8

    
    return output_grid
```
