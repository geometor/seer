"""
The transformation rule repositions the maroon colored pixel (value '9') to the bottom-right corner of the grid and removes isolated azure (value '8') pixels.
It preserves a cluster of other colors ('4', '7', and an adjacent '8') at their original locations.
"""

import numpy as np

def find_pixel(grid, color_value):
    # Find the coordinates of a specific color value.
    coords = np.where(grid == color_value)
    if len(coords[0]) > 0:
        return [coords[0][0], coords[1][0]]  # Return first occurrence
    return None

def is_isolated(grid, row, col, color_value):
    # check to make sure the grid is at least 2x2
    if grid.shape[0] < 2 or grid.shape[1] < 2:
      return True

    # Check if a pixel of a specific color is isolated.
    rows, cols = grid.shape
    
    # Define adjacent positions (including diagonals)
    adjacent_positions = [
        (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
        (row, col - 1),                     (row, col + 1),
        (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)
    ]
    
    for r, c in adjacent_positions:
        if 0 <= r < rows and 0 <= c < cols:
            if grid[r, c] != 0 and grid[r,c] != color_value:
                return False  # Adjacent to a different color
    return True

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find and move the maroon pixel (9)
    maroon_coords = find_pixel(input_grid, 9)
    if maroon_coords:
        output_grid[maroon_coords[0], maroon_coords[1]] = 0  # Clear original position
        output_grid[rows - 1, cols - 1] = 9  # Move to bottom-right

    # Find and zero out isolated azure pixels (8)
    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] == 8:
                if is_isolated(output_grid, r, c, 8):
                    output_grid[r, c] = 0

    return output_grid