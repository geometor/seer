# 1b2d62fb • 012 • refine_coder

---
```python
"""
1.  **Locate Blue Line:** Find the vertical line of blue (1) pixels in the input grid.  A vertical line is defined as two or more vertically adjacent pixels of the same color.
2.  **Define Region of Interest:**  Define a region to the immediate right of the blue line. This region has the same height as the input grid and a width of 3 columns.
3. **Transformation based on position:**
    Iterate following cells of the `input_grid`:
     - `input_grid[i, blue_line_col + 1]`:`output_grid[i,0]`
     - `input_grid[i, blue_line_col + 2]`:`output_grid[i,1]`
     - `input_grid[i, blue_line_col + 3]`:`output_grid[i,2]`
    Check cells of input grid, if not '0', replace the related position at output grid to '8'
4.  **Output:** Create a new grid (output_grid) which is the result of `transform_region`.
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
    if blue_line_col != -1 :
        for i in range(rows):
            for j in range(3):
                if blue_line_col + 1 + j < cols: #check out of bound
                    if input_grid[i,blue_line_col+1+j] != 0:
                        output_grid[i,j] = 8
                    else:
                        output_grid[i,j] = 0


    return output_grid
```
