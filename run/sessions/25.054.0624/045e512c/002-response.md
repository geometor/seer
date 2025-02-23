# 045e512c • 002 • example_1 • investigate_coder

---
```python
"""
Identify an azure rectangle, a green pixel, and a red rectangle. Replicate the green pixel horizontally to the right, alternating with blank spaces. Replicate the red rectangle vertically downwards, alternating between the full rectangle and a version with the center pixel removed. The Azure shape is unchanged.
"""

import numpy as np

def find_object(grid, color):
    # Find the coordinates of pixels of the specified color.
    coords = np.argwhere(grid == color)
    if coords.size == 0:
      return None, None
    min_row, min_col = coords.min(axis=0)
    max_row, max_col = coords.max(axis=0)
    return (min_row, min_col), (max_row, max_col)

def replicate_green(grid, start_row, start_col):
    # Replicate the green pixel horizontally.
    output_grid = np.copy(grid)
    output_grid[start_row, start_col] = 3 #ensure it exists
    for col in range(start_col + 1, grid.shape[1]):
        if (col - start_col) % 2 == 0:
          output_grid[start_row, col] = 3
        else:
          output_grid[start_row,col] = 0
    return output_grid

def replicate_red(grid, start_row, start_col, end_row, end_col):
    # Replicate the red rectangle vertically.
    output_grid = np.copy(grid)
    height = end_row - start_row + 1
    width = end_col - start_col + 1
    
    row_cursor = end_row + 1

    while row_cursor + height <= grid.shape[0]:
        for r in range(height):
            for c in range(width):
                output_grid[row_cursor + r, start_col + c] = 2
        
        row_cursor += height
        if row_cursor + height > grid.shape[0]:
            break
        #now the one with the center removed
        for r in range(height):
            for c in range(width):
                if r==1 and c == 1 and height==3: #check for 3x3 specifically
                  output_grid[row_cursor + r, start_col + c] = 0 # remove center
                else:
                  output_grid[row_cursor + r, start_col + c] = 2
        row_cursor += height

    return output_grid

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Find azure rectangle (do nothing with it)
    azure_top_left, azure_bottom_right = find_object(input_grid, 8)

    # Find green pixel
    green_top_left, green_bottom_right = find_object(input_grid, 3)
    if green_top_left is not None:
      output_grid = replicate_green(output_grid, green_top_left[0], green_top_left[1])
    # Find red rectangle
    red_top_left, red_bottom_right = find_object(input_grid, 2)
    if red_top_left is not None:
      output_grid = replicate_red(output_grid, red_top_left[0], red_top_left[1], red_bottom_right[0], red_bottom_right[1])


    return output_grid
```
