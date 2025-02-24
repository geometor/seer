# bdad9b1f • 004 • refine_coder

---
```python
"""
1.  **Find the Red Row:** Identify the row that contains red pixels.
2.  **Find the Azure Column:** Identify the column that contains azure pixels.
3.  **Mark Intersection:** Change the color of the cell where the red row and azure column intersect to yellow.
4.  **Extend Red:** Starting from the beginning of the red row, change all pixels to red until the intersection with the azure column is reached.
5.  **Extend Azure Conditionally:**  If there are azure pixels above the red row, extend the azure color upwards in the azure column to the top of the grid. If there are azure pixels *below* the red row, extend the azure color downwards in the azure column to the bottom of the grid. If both are true, connect them all.
"""

import numpy as np

def find_row_with_color(grid, color):
    for i, row in enumerate(grid):
        if color in row:
            return i
    return -1

def find_col_with_color(grid, color):
    grid_t = grid.transpose()
    for i, col in enumerate(grid_t):
        if color in col:
            return i
    return -1

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # find the red row and azure column
    red_row = find_row_with_color(input_grid, 2)
    azure_col = find_col_with_color(input_grid, 8)

    if red_row == -1 or azure_col == -1:
        return output_grid
    
    # intersection point to yellow
    output_grid[red_row, azure_col] = 4

    # extend red to intersection
    for j in range(azure_col + 1):
        output_grid[red_row,j] = 2
    
    # fill azure down the column conditionally
    azure_above = False
    azure_below = False

    for i in range(red_row):
        if input_grid[i, azure_col] == 8:
            azure_above = True
            break

    for i in range(red_row + 1, input_grid.shape[0]):
        if input_grid[i, azure_col] == 8:
            azure_below = True
            break

    if azure_above:
      for i in range(red_row):
          output_grid[i, azure_col] = 8
    if azure_below:
      for i in range(red_row+1, output_grid.shape[0]):
          output_grid[i, azure_col] = 8

    
    return output_grid
```
