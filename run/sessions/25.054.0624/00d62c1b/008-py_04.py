"""
Finds a white (0) pixel that is completely surrounded by four green (3) pixels (above, below, left, and right, *not* diagonally), and changes the color of *only* that identified pixel to yellow (4).
"""

import numpy as np

def get_neighbors(grid, row, col):
    """Gets the values of the immediate neighbors (up, down, left, right)."""
    rows, cols = grid.shape
    neighbors = []
    if row > 0:
        neighbors.append(grid[row-1, col])  # Up
    if row < rows - 1:
        neighbors.append(grid[row+1, col])  # Down
    if col > 0:
        neighbors.append(grid[row, col-1])  # Left
    if col < cols - 1:
        neighbors.append(grid[row, col+1])  # Right
    return neighbors

def transform(input_grid):
    """Transforms the input grid according to the rule."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each pixel to check for the condition
    for row in range(rows):
        for col in range(cols):
            # Check if the current pixel is white (0)
            if input_grid[row, col] == 0:
                # Get the neighbors of current pix
                neighbors = get_neighbors(input_grid, row, col)
                # Check if all neighbors are green (3)
                if len(neighbors)==4 and all(n == 3 for n in neighbors):
                    output_grid[row, col] = 4  # Change to yellow (4)
                    return output_grid # return immediately after first change

    return output_grid