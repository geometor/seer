"""
Iterate through the grid. If a non-background pixel (a pixel with color other than 0) is adjacent to the background color of the row it is in, change the pixel's color to 0.
"""

import numpy as np

def get_background_color(row):
    """Gets the most frequent color in a row, assumed to be background."""
    # Use bincount to count occurrences of each color.
    counts = np.bincount(row)
    # argmax returns the index of the maximum value, which corresponds to the color.
    return np.argmax(counts)

def is_adjacent(grid, row, col, target_color):
    """Checks if a pixel at grid[row][col] is adjacent to the target_color."""
    height, width = grid.shape
    for i in range(max(0, row - 1), min(height, row + 2)):
        for j in range(max(0, col - 1), min(width, col + 2)):
            if (i != row or j != col) and grid[i, j] == target_color:
                return True
    return False

def transform(input_grid):
    """Transforms the input grid according to the rule."""
    output_grid = np.copy(input_grid)
    height, width = input_grid.shape

    for row in range(height):
        background_color = get_background_color(input_grid[row])
        for col in range(width):
            # Check if the pixel is not the background color and is adjacent to background
            if input_grid[row, col] != background_color and is_adjacent(input_grid, row, col, background_color):
                output_grid[row, col] = 0

    return output_grid