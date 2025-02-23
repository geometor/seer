"""
The transformation preserves the position and color of the initial red and blue cells and frames those cells with a cross of the same size. The cross surrounding the red cell is color 4, while the cross surrounding the blue cell is color 7.
"""

import numpy as np

def find_object(grid, color):
    # Find the coordinates of a single-cell object of the specified color.
    coords = np.where(grid == color)
    if len(coords[0]) > 0:
        return coords[0][0], coords[1][0]  # return row, col
    return None

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.
    output_grid = np.copy(input_grid)

    # Find the red object (color 2).
    red_pos = find_object(input_grid, 2)
    if red_pos:
        row, col = red_pos
        # Frame the red object with yellow (color 4).
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < output_grid.shape[0] and 0 <= new_col < output_grid.shape[1]:
                output_grid[new_row, new_col] = 4

    # Find the blue object (color 1).
    blue_pos = find_object(input_grid, 1)
    if blue_pos:
        row, col = blue_pos
        # Frame the blue object with orange (color 7).
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < output_grid.shape[0] and 0 <= new_col < output_grid.shape[1]:
                output_grid[new_row, new_col] = 7

    return output_grid