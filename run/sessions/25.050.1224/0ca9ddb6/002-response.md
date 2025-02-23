# 0ca9ddb6 • 002 • example_1 - CODE

---
```python
"""
The transformation rule is as follows:
1.  The single red (color 2) cell and the single blue (color 1) cell in the input remain unchanged.
2.  A yellow (color 4) 1x1 "cross" or "+" shape appears centered on the row above and the row below the red cell.
3.  An orange (color 7) 1x1 "cross" or "+" shape appears centered on the column to the left and the column to the right of the blue cell.
"""

import numpy as np

def find_object(grid, color):
    # Find the coordinates of a specific color cell.
    coords = np.where(grid == color)
    if len(coords[0]) > 0:
        return (coords[0][0], coords[1][0])  # Returns (row, col)
    return None

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    
    # Find the red and blue cells
    red_pos = find_object(input_grid, 2)
    blue_pos = find_object(input_grid, 1)

    # Place yellow cells around the red cell
    if red_pos:
        row, col = red_pos
        if row > 0:
            output_grid[row - 1, col] = 4  # Above
        
        if row < output_grid.shape[0] -1:
            output_grid[row+1, col]=4 #below
        
        output_grid[row - 1, col -1]=0 # remove diagonals
        output_grid[row-1,col+1] = 0
        output_grid[row + 1, col-1]=0
        output_grid[row+1, col+1]=0

    # Place orange cells around the blue cell
    if blue_pos:
        row, col = blue_pos
        if col > 0:
            output_grid[row, col - 1] = 7  # Left
        if col < output_grid.shape[1] - 1:
            output_grid[row, col + 1] = 7  # Right

        output_grid[row-1,col-1]=0 # remove diagonals
        output_grid[row+1,col+1]=0 # remove diagonals
        output_grid[row-1, col+1] = 0 if (row > 0 and col< output_grid.shape[1]-1) else output_grid[row-1,col+1]
        output_grid[row+1,col-1] = 0 if (row < output_grid.shape[0] -1 and col>0) else output_grid[row+1,col-1]
        
        if row>0:
            output_grid[row - 1, col]=7 if output_grid[row-1,col]!=0 else 0 # avoid overlaps
        if row < output_grid.shape[0]-1:    
            output_grid[row+1,col]= 7 if output_grid[row+1,col]!=0 else 0

    return output_grid
```
