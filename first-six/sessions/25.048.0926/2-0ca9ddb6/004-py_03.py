"""
The transformation rule involves drawing a yellow cross centered one cell above each red cell and an orange cross centered on each blue cell. The original red, blue, and any other single-color cells remain unchanged.
"""

import numpy as np

def find_objects(grid, color):
    """Find all occurrences of a specific color in the grid."""
    coords = np.where(grid == color)
    positions = []
    for i in range(len(coords[0])):
        positions.append((coords[0][i], coords[1][i]))
    return positions

def transform(input_grid):
    """Transforms the input grid according to the defined rule."""
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find all red objects (color 2)
    red_positions = find_objects(input_grid, 2)
    for row, col in red_positions:
        # Create the yellow cross one cell above each red cell
        output_grid[row - 1, col - 1] = 4  # Top-left of the red cell
        output_grid[row - 1, col + 1] = 4  # Top-right of the red cell
        output_grid[row - 2, col] = 4      # Two cells above the red cell
        output_grid[row , col] = 2        # preserve location of red cell
        output_grid[row, col -1] = 0       # remove existing colors
        output_grid[row , col + 1] = 0    # remove existing colors
        output_grid[row + 1, col] = 0       # remove existing colors
        output_grid[row -1, col] = 0       # remove existing colors

    # Find all blue objects (color 1)
    blue_positions = find_objects(input_grid, 1)
    for row, col in blue_positions:
        # Create the orange cross around each blue cell
        output_grid[row - 1, col] = 7  # Cell above
        output_grid[row + 1, col] = 7  # Cell below
        output_grid[row, col - 1] = 7  # Cell to the left
        output_grid[row, col + 1] = 7  # Cell to the right

    return output_grid