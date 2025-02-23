"""
Transforms an input grid by creating yellow (4) and orange (7) crosses centered
around the locations of red (2) and blue (1) pixels, respectively.
"""

import numpy as np

def find_pixels(grid, color):
    """Finds all pixels of a given color in a grid."""
    coords = np.where(grid == color)
    return list(zip(coords[0], coords[1]))

def create_cross(grid, center_row, center_col, color):
    """Creates a cross pattern in the grid with the given center and color."""
    rows, cols = grid.shape

    # Horizontal line, if those rows aren't already present
    if not np.any(grid[center_row-1, :] == color) and center_row -1 >= 0:
       grid[center_row - 1, :] = color
       grid[center_row - 1, center_col] = 0
    if not np.any(grid[center_row+1, :] == color) and center_row + 1 < rows:
        grid[center_row + 1, :] = color
        grid[center_row + 1, center_col] = 0


    # Vertical elements (extending from the center)
    if center_col - 1 >= 0:
        grid[center_row, center_col - 1] = color
    if center_col + 1 < cols:
        grid[center_row, center_col + 1] = color

    return grid

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    output_grid = np.copy(input_grid)

    # Find red pixels and create yellow crosses.
    red_pixels = find_pixels(input_grid, 2)
    for row, col in red_pixels:
        output_grid = create_cross(output_grid, row, col, 4)
        output_grid[row,col] = 2 # restore the original color


    # Find blue pixels and create orange crosses.
    blue_pixels = find_pixels(input_grid, 1)
    for row, col in blue_pixels:
        output_grid = create_cross(output_grid, row, col, 7)
        output_grid[row,col] = 1 # restore the original color

    return output_grid