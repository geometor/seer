"""
The transformation rule is as follows:
1.  The red (color 2) cells and the blue (color 1) cells in the input remain unchanged.
2.  A yellow (color 4) 1x1 "cross" or "+" shape appears centered on the row above and the row below each red cell.
3.  An orange (color 7) 1x1 "cross" or "+" shape appears centered on the column to the left and the column to the right of each blue cell.
"""

import numpy as np

def find_objects(grid, color):
    # Find the coordinates of all cells of a specific color.
    coords = np.where(grid == color)
    objects = []
    for i in range(len(coords[0])):
        objects.append((coords[0][i], coords[1][i]))  # Returns (row, col)
    return objects

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    
    # Find all red and blue cells
    red_positions = find_objects(input_grid, 2)
    blue_positions = find_objects(input_grid, 1)

    # Place yellow cells around each red cell
    for red_pos in red_positions:
        row, col = red_pos
        if row > 0:
            output_grid[row - 1, col] = 4  # Above
        if row < output_grid.shape[0] - 1:
            output_grid[row + 1, col] = 4  # Below
        
        if row > 0 and col > 0:
            output_grid[row - 1, col - 1] = 0 # remove diagonals
        if row > 0 and col < output_grid.shape[1] - 1:
            output_grid[row-1,col+1] = 0
        if row < output_grid.shape[0] - 1 and col > 0:    
            output_grid[row + 1, col-1]=0
        if row < output_grid.shape[0] - 1 and col < output_grid.shape[1] - 1:
            output_grid[row+1, col+1]=0    

    # Place orange cells around each blue cell
    for blue_pos in blue_positions:
        row, col = blue_pos
        if col > 0:
            output_grid[row, col - 1] = 7  # Left
        if col < output_grid.shape[1] - 1:
            output_grid[row, col + 1] = 7  # Right
        
        if row > 0 and col > 0:
            output_grid[row-1,col-1]=0 # remove diagonals
        if row < output_grid.shape[0]-1 and col < output_grid.shape[1]-1:
            output_grid[row+1,col+1]=0 # remove diagonals
        if row > 0 and col < output_grid.shape[1]-1:
            output_grid[row-1, col+1] = 0 
        if row < output_grid.shape[0]-1 and col > 0:
            output_grid[row+1,col-1] = 0
        
        if row > 0:
            output_grid[row-1,col] = 7 if output_grid[row-1,col] != 0 else 0 #avoid overlap
        if row < output_grid.shape[0]-1:
             output_grid[row+1,col] = 7 if output_grid[row+1,col] !=0 else 0

    return output_grid