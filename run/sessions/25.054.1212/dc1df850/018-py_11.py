"""
Identifies all red pixels (value '2') in the input grid and changes all adjacent white pixels (value '0') to blue (value '1').
The red pixels themselves, and pixels of any color other than white, remain unchanged.
"""

import numpy as np

def find_all_pixels_by_color(grid, color):
    """Finds the coordinates of all pixels of the specified color."""
    pixels = []
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color:
                pixels.append((r, c))
    return pixels

def get_neighbors(row, col, grid_shape):
    """Gets the coordinates of all eight neighbors of a pixel."""
    neighbors = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue  # Skip the cell itself
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < grid_shape[0] and 0 <= new_col < grid_shape[1]:
                neighbors.append((new_row, new_col))
    return neighbors

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""
    output_grid = np.copy(input_grid)
    red_pixels = find_all_pixels_by_color(input_grid, 2)

    for row, col in red_pixels:
        neighbors = get_neighbors(row, col, input_grid.shape)
        for neighbor_row, neighbor_col in neighbors:
            if output_grid[neighbor_row, neighbor_col] == 0:
                output_grid[neighbor_row, neighbor_col] = 1

    return output_grid