"""
Identifies a red pixel (value '2') in the input grid and changes its immediate top, left, and top-left, top-right, and bottom-left neighbors to blue (value '1') if those are '0' (white)
The original '2' pixel is left on the same place and same value.
The remaining '0' are left unchanged.
"""

import numpy as np

def find_pixel_by_color(grid, color):
    """Finds the coordinates of a pixel of the specified color."""
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color:
                return (r, c)
    return None

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""
    output_grid = np.copy(input_grid)
    target_color = 2
    surrounding_color = 1

    # Find the target pixel (red)
    target_pos = find_pixel_by_color(input_grid, target_color)

    if target_pos is None:
        return output_grid  # No target pixel found, return original grid

    target_row, target_col = target_pos

    # Define the relative positions of the neighbors to be changed
    neighbors = [
        (target_row - 1, target_col),  # Top
        (target_row, target_col - 1),  # Left
        (target_row - 1, target_col - 1),  # Top-left
        (target_row - 1, target_col + 1),  # Top-right
        (target_row + 1, target_col - 1)  # Bottom-left
    ]

    # Iterate through the neighbors and change their color if they are '0'
    for row, col in neighbors:
        if 0 <= row < output_grid.shape[0] and 0 <= col < output_grid.shape[1]:  # Check boundaries
            if output_grid[row, col] == 0:
                output_grid[row, col] = surrounding_color

    return output_grid