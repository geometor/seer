"""
1. Identify White and Red Pixels: Locate all pixels colored white (0) and red (2).
2. Check for Adjacency: For each white pixel, determine if it is directly adjacent (horizontally or vertically, not diagonally) to a red pixel.
3. Check Row Constraint: If a white pixel is adjacent to a red pixel, check if it is in the bottom 2 rows.
4. Conditional Replacement: If a white pixel is adjacent to at least one red pixel AND is on the bottom or second-to-bottom row, replace it with a blue pixel (1).
5. Leave Other Pixels Unchanged: All other pixels retain their original colors.
"""

import numpy as np

def get_adjacent_pixels(grid, row, col):
    """
    Gets the coordinates of horizontally and vertically adjacent pixels.
    """
    rows, cols = grid.shape
    adjacent_pixels = []
    if row > 0:
        adjacent_pixels.append((row - 1, col))  # Up
    if row < rows - 1:
        adjacent_pixels.append((row + 1, col))  # Down
    if col > 0:
        adjacent_pixels.append((row, col - 1))  # Left
    if col < cols - 1:
        adjacent_pixels.append((row, col + 1))  # Right
    return adjacent_pixels

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each pixel in the grid
    for i in range(rows):
        for j in range(cols):
            # Check if the pixel is white (0)
            if output_grid[i, j] == 0:
                # Check for adjacency to red (2) pixels
                is_adjacent_to_red = False
                for r, c in get_adjacent_pixels(output_grid, i, j):
                    if output_grid[r, c] == 2:
                        is_adjacent_to_red = True
                        break

                # Check row constraint (bottom two rows) and adjacency
                if is_adjacent_to_red and i >= rows - 2:
                    # Change the color to blue (1)
                    output_grid[i, j] = 1

    return output_grid