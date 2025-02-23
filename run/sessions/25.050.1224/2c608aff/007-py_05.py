"""
Each yellow cell extends horizontally to the left up to the 3rd column.  The gray rectangle is preserved.
"""

import numpy as np

def find_object(grid, color):
    # Find coordinates of all cells with the given color
    coords = np.argwhere(grid == color)
    if coords.size == 0:
        return None  # Return None if no object of the specified color is found
    return coords

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule:
    Each yellow cell extends horizontally to the left, up to the third column.
    The gray rectangle and other elements are preserved.
    """
    output_grid = np.copy(input_grid)
    yellow_coords = find_object(input_grid, 4)

    if yellow_coords is not None:
        for coord in yellow_coords:
            row, col = coord
            # Extend horizontally to the left up to the third column (index 2)
            for i in range(2, col + 1):  # Inclusive of the starting column
                output_grid[row][i] = 4

    return output_grid