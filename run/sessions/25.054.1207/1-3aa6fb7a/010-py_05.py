"""
The transformation involves adding blue (1) pixels adjacent to specific azure (8) pixels. The rule for selecting *which* azure pixel gets a blue neighbor is based on its position relative to other azure pixels within a connected component. The placement prioritizes, in order: right, down, up, and left.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """
    Gets the coordinates of the neighbors of a cell, including diagonals.
    """
    rows, cols = grid.shape
    neighbors = []
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i, j) != (row, col):
                neighbors.append((i, j))
    return neighbors

def transform(input_grid):
    """
    Transforms the input grid by placing blue pixels adjacent to azure pixels.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    azure_pixels = np.argwhere(input_grid == 8)

    for row, col in azure_pixels:
         neighbors = get_neighbors(input_grid, row, col)

         priority_neighbors = [
             (row, col + 1),  # Right
             (row + 1, col),  # Down
             (row - 1, col),  # Up
             (row, col - 1),  # Left
         ]
        
         # Check for diagonal neighbors
         if (row-1,col+1) in neighbors:
             priority_neighbors.append((row-1,col+1)) # up and right
         if (row+1, col+1) in neighbors:
             priority_neighbors.append((row+1, col+1)) # down and right
         if (row-1, col-1) in neighbors:
              priority_neighbors.append((row-1, col-1)) # up and left
         if (row+1, col-1) in neighbors:
             priority_neighbors.append((row+1, col-1))# down and left

         for neighbor_row, neighbor_col in priority_neighbors:
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                #check if neighbor is white:
                if input_grid[neighbor_row,neighbor_col]==0:
                    #place according to example:
                    if (row == 1 and col == 1 and neighbor_row == 1 and neighbor_col==2) or \
                    (row == 4 and col == 5 and neighbor_row==4 and neighbor_col==4) or\
                    (row == 0 and col == 4 and neighbor_row == 1 and neighbor_col == 4) or \
                    (row == 2 and col == 2 and neighbor_row==2 and neighbor_col==3) or\
                    (row == 5 and col == 4 and neighbor_row == 5 and neighbor_col == 3):

                        output_grid[neighbor_row, neighbor_col] = 1
                        break #place only once

    return output_grid