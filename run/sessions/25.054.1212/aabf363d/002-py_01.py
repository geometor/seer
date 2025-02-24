"""
Identifies a contiguous shape of red pixels and a single yellow pixel in the input grid. Replaces the red shape with yellow pixels and removes the original yellow pixel.
"""

import numpy as np

def find_object(grid, color):
    # Find coordinates of all pixels of the specified color.
    coords = np.argwhere(grid == color)
    if len(coords) == 0:
        return None

    # Check connectivity - only consider directly adjacent pixels.
    visited = set()
    object_coords = []

    def dfs(row, col):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return
        visited.add((row, col))
        object_coords.append((row, col))
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    start_row, start_col = coords[0]
    dfs(start_row, start_col)
    return object_coords

def find_single_pixel(grid, color):
    coords = np.argwhere(grid == color)
    if len(coords) == 1:
      return coords[0]
    return None


def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.
    output_grid = np.copy(input_grid)

    # Find the red object.
    red_object_coords = find_object(input_grid, 2)

    # find single yellow pixel
    yellow_pixel_coord = find_single_pixel(input_grid, 4)

    # Change the color of the red object to yellow in the output_grid.
    if red_object_coords:
        for row, col in red_object_coords:
            output_grid[row, col] = 4

    if yellow_pixel_coord:
      output_grid[yellow_pixel_coord[0], yellow_pixel_coord[1]] = 0

    return output_grid