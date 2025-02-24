"""
Replaces gray (5) pixels with green (3) pixels in the input grid if they are:
1. Located in the first or second column (from left).
2. Vertically or horizontally adjacent to a white (0) pixel.
All other pixels retain their original colors.
"""

import numpy as np

def get_adjacent_pixels(grid, row, col):
    """
    Gets the adjacent pixels (up, down, left, right) of a given cell in the grid.

    Args:
        grid: The 2D numpy array representing the grid.
        row: The row index of the cell.
        col: The column index of the cell.

    Returns:
        A list of tuples, where each tuple represents an adjacent pixel
        and contains (row, col, color).
    """
    rows, cols = grid.shape
    adjacent_pixels = []
    # Check up, down, left, right.
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            adjacent_pixels.append((new_row, new_col, grid[new_row, new_col]))
    return adjacent_pixels

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through the grid, focusing on the first two columns.
    for row in range(rows):
        for col in range(min(2, cols)): # Only check the first two columns.
            if output_grid[row, col] == 5:  # If the pixel is gray.
                adjacent_pixels = get_adjacent_pixels(output_grid, row, col)
                for r, c, color in adjacent_pixels:
                     if color == 0:  # if there is a horizontally or vertically adjacent white pixel
                        output_grid[row,col] = 3 # Set start of sequence, move right
                        break # found a white, move on
    return output_grid