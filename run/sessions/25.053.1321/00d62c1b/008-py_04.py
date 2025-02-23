"""
Identifies green (3) pixels in the input grid.
For each green pixel, determines if it is the center of a "+" shaped object formed by green pixels.
A pixel is the center of a "+" if the continuous lines of green pixels extending horizontally and vertically are at least 3 pixels long (including the center).
Changes the color of the center pixel of valid "+" shaped objects to yellow (4).
All other pixels remain unchanged.
Returns the modified grid.
"""

import numpy as np

def get_line_length(grid, row, col, direction):
    """
    Calculates the length of a contiguous line of green pixels starting from a given position.

    Args:
        grid: The input grid.
        row: Starting row index.
        col: Starting column index.
        direction: A tuple (row_change, col_change) indicating the direction to check.
                   (0, 1) for horizontal (right), (0, -1) for horizontal (left),
                   (1, 0) for vertical (down), (-1, 0) for vertical (up).

    Returns:
        The length of the contiguous line of green pixels in the specified direction.
    """
    rows, cols = grid.shape
    length = 0
    r, c = row, col
    dr, dc = direction

    while 0 <= r < rows and 0 <= c < cols and grid[r, c] == 3:
        length += 1
        r += dr
        c += dc
    return length

def is_plus_center(grid, row, col):
    """
    Checks if a green pixel is the center of a '+' shape with arms of length >= 3.

    Args:
        grid: The input grid.
        row: Row index of the pixel.
        col: Column index of the pixel.

    Returns:
        True if the pixel is a valid '+' center, False otherwise.
    """
    if grid[row, col] != 3:
        return False

    # Calculate lengths in all four directions
    left_length = get_line_length(grid, row, col - 1, (0, -1))
    right_length = get_line_length(grid, row, col + 1, (0, 1))
    up_length = get_line_length(grid, row - 1, col, (-1, 0))
    down_length = get_line_length(grid, row + 1, col, (1, 0))

    # Check if horizontal and vertical lengths are >= 3 (including the center pixel)
    horizontal_length = left_length + 1 + right_length
    vertical_length = up_length + 1 + down_length

    return horizontal_length >= 3 and vertical_length >= 3


def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each pixel
    for row in range(rows):
        for col in range(cols):
            # Check if the pixel is green and a '+' center
            if is_plus_center(output_grid, row, col):
                # Change the color to yellow
                output_grid[row, col] = 4

    return output_grid