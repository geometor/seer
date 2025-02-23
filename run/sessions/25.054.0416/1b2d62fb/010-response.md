# 1b2d62fb • 010 • refine_coder

---
```python
"""
1.  **Locate**: Find the vertical line of blue (1) pixels within the input grid.
2.  **Define Region:** A region of interest will be the same height as input and start from the immediate right of blue line, with width of 3
3. **Transform**: If the region to extract has cell with value other than '0', change it to '8'.
4.  **Output**: Create a new grid that represents the extracted region.
"""

import numpy as np

def find_vertical_line(grid, color):
    # Find the column index of the vertical line of the specified color
    rows, cols = grid.shape
    for j in range(cols):
        for i in range(rows):
            if grid[i, j] == color:
                # Check if it's a vertical line
                if i + 1 < rows and grid[i+1, j] == color:
                    return j
    return -1  # Return -1 if no vertical line is found

def transform(input_grid):
    # initialize output_grid
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, 3), dtype=int)

    # Find the vertical blue line (color 1)
    blue_line_col = find_vertical_line(input_grid, 1)

    # Extract the region to the right of the blue line
    if blue_line_col != -1 and blue_line_col + 1 < cols:
        region = input_grid[:, blue_line_col + 1: min(blue_line_col + 4, cols)]
    
        # Convert non-white (0) pixels in the region to azure (8)
        for i in range(region.shape[0]):
             for j in range(min(3,region.shape[1])):
                if region[i,j] != 0:
                  output_grid[i,j] = 8
                else:
                  output_grid[i,j] = region[i,j]

    return output_grid
```
