"""
The transformation preserves the positions of the existing red and blue pixels and introduces new yellow pixels diagonally around the red pixel and orange pixels horizontally and vertically around the blue pixel.
"""

import numpy as np

def find_pixel(grid, color):
    """Finds the coordinates of the first occurrence of a specific color."""
    coords = np.where(grid == color)
    if len(coords[0]) > 0:
        return (coords[0][0], coords[1][0])
    return None

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""
    output_grid = np.zeros_like(input_grid)  # Initialize with zeros
    
    # Copy the input grid to preserve existing non-zero pixels
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
          if input_grid[i,j]!=0:
            output_grid[i,j] = input_grid[i,j]

    # Find the red (2) and blue (1) pixels
    red_pos = find_pixel(input_grid, 2)
    blue_pos = find_pixel(input_grid, 1)

    # Add yellow (4) pixels around the red pixel
    if red_pos:
        row, col = red_pos
        # Diagonally adjacent pixels
        if row > 0 and col > 0:
            output_grid[row - 1, col - 1] = 4
        if row > 0 and col < output_grid.shape[1] - 1:
            output_grid[row - 1, col + 1] = 4
        if row < output_grid.shape[0] - 1 and col > 0:
            output_grid[row + 1, col - 1] = 4
        if row < output_grid.shape[0] - 1 and col < output_grid.shape[1] - 1:
            output_grid[row + 1, col + 1] = 4

    # Add orange (7) pixels around the blue pixel
    if blue_pos:
        row, col = blue_pos
        # Horizontally and vertically adjacent pixels
        if row > 0:
            output_grid[row - 1, col] = 7
        if row < output_grid.shape[0] - 1:
            output_grid[row + 1, col] = 7
        if col > 0:
            output_grid[row, col - 1] = 7
        if col < output_grid.shape[1] - 1:
            output_grid[row, col + 1] = 7

    return output_grid