"""
1. **Preservation:**
    *   Single cells of color 8, color 2, color 1 and color 6 remain unchanged in the output grid.

2.  **Color 2 Transformation (Yellow Spawning):**
    *   For each cell of color 2 in the input grid:
        *   Place a cell of color 4 one row above and one column to the left.
        *   Place a cell of color 4 one row above and one column to the right.
        *   Place a cell of color 4 one row below and one column to the left.
        *   Place a cell of color 4 one row below and one column to the right.
    *   Ensure these new color 4 cells are only placed if the position is within the grid boundaries.

3.  **Color 1 Transformation (Orange Spawning):**
    *   For each cell of color 1 in the input grid:
        *   Place a cell of color 7 one row directly above.
        *   Place cells of color 7 in the entire 3x3 neighborhood *around* the original color 1 cell, *excluding* the cell itself.
    * Ensure that color 7 is placed within the grid boundaries.
"""

import numpy as np

def find_objects(grid, color):
    # Find coordinates of all cells with the specified color.
    return np.array(np.where(grid == color)).T

def transform(input_grid):
    # Initialize output grid as all zeros.
    output_grid = np.zeros_like(input_grid)

    # Preserve single cells of color 8, 2, 1 and 6.
    for color in [8, 2, 1, 6]:
        objects = find_objects(input_grid, color)
        for obj in objects:
            row, col = obj
            output_grid[row, col] = color

    # Find the objects of color 2 and 1.
    objects_2 = find_objects(input_grid, 2)
    objects_1 = find_objects(input_grid, 1)

    # Apply rules for object of color 2.
    for obj_2 in objects_2:
        row, col = obj_2
        # Place color 4 cells above and below, to the left and right.
        if row - 1 >= 0:
            if col - 1 >= 0:
                output_grid[row - 1, col - 1] = 4
            if col + 1 < output_grid.shape[1]:
                output_grid[row - 1, col + 1] = 4
        if row + 1 < output_grid.shape[0]:
            if col - 1 >= 0:
                output_grid[row + 1, col - 1] = 4
            if col + 1 < output_grid.shape[1]:
                output_grid[row + 1, col + 1] = 4

    # Apply rules for object of color 1.
    for obj_1 in objects_1:
        row, col = obj_1
        # Place color 7 above.
        if row - 1 >= 0:
            output_grid[row - 1, col] = 7
        # Place color 7 in the 3x3 neighborhood, excluding the center.
        for i in range(max(0, row - 1), min(row + 2, output_grid.shape[0])):
            for j in range(max(0, col - 1), min(col + 2, output_grid.shape[1])):
                if (i, j) != (row, col):  # Exclude the center cell itself.
                    output_grid[i, j] = 7

    return output_grid