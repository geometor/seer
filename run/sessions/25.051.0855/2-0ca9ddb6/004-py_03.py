"""
The transformation rule identifies cells of color 2 and color 1 as anchor points for transformations. For each cell of color 2, it inserts cells of color 4 diagonally above and below it (one position away).  For each cell of color 1, it creates a 3x3 grid of color 7 centered on that cell, while preserving the original color 1 cell. Border conditions are handled to prevent out-of-bounds access. Overlapping regions caused by multiple color 1 cells are correctly merged.
"""

import numpy as np

def find_objects(grid, color):
    # Find coordinates of all cells with the specified color.
    return np.array(np.where(grid == color)).T

def transform(input_grid):
    # Initialize output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    
    # Find the objects of color 2 and 1.
    objects_2 = find_objects(input_grid, 2)
    objects_1 = find_objects(input_grid, 1)

    # Apply rules for object of color 2.
    for obj_2 in objects_2:
        row, col = obj_2
        if row > 0 and col > 0:
          output_grid[row - 1, col - 1] = 4
        if row > 0 and col < output_grid.shape[1]-1:
          output_grid[row - 1, col + 1] = 4
        if row < output_grid.shape[0]-1 and col > 0:
          output_grid[row + 1, col - 1] = 4
        if row < output_grid.shape[0]-1 and col < output_grid.shape[1]-1:
          output_grid[row + 1, col + 1] = 4
    
    # Apply rules for object of color 1
    for obj_1 in objects_1:
        row, col = obj_1
        for i in range(max(0, row - 1), min(output_grid.shape[0], row + 2)):
            for j in range(max(0, col - 1), min(output_grid.shape[1], col + 2)):
                if (i,j) != (row, col):
                     output_grid[i,j] = 7


    return output_grid