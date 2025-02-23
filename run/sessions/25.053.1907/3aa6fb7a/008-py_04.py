"""
Identifies contiguous regions of azure (8) pixels in the input grid. 
Within each azure region, it changes the color of internal azure pixels 
(those with four cardinally adjacent azure neighbors) to blue (1). 
All other pixels remain unchanged.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """Gets the valid cardinal neighbors of a cell."""
    rows, cols = grid.shape
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))  # Up
    if row < rows - 1:
        neighbors.append((row + 1, col))  # Down
    if col > 0:
        neighbors.append((row, col - 1))  # Left
    if col < cols - 1:
        neighbors.append((row, col + 1))  # Right
    return neighbors

def is_internal_azure(grid, row, col):
    """Checks if a pixel is an internal azure pixel."""
    if grid[row, col] != 8:
        return False
    neighbors = get_neighbors(grid, row, col)
    for r, c in neighbors:
        if grid[r, c] != 8:
            return False
    return True

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)  # Initialize output_grid as a copy of input_grid

    rows, cols = input_grid.shape

    # Iterate through each cell in the grid
    for row in range(rows):
        for col in range(cols):
            # Check if the cell is an internal azure pixel
            if is_internal_azure(input_grid, row, col):
                # Change the color to blue (1)
                output_grid[row, col] = 1

    return output_grid