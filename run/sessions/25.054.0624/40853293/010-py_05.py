"""
1.  **Identify Isolated Pixels:** Scan the input grid to find pixels that are not white (color 0) and are surrounded on all four sides (up, down, left, right) by either white pixels or the edge of the grid.

2.  **Create Plus Shapes:** For each isolated pixel:
    *   Extend the pixel's color horizontally to the left and right, stopping when a non-white pixel or the grid edge is encountered.
    *   Extend the pixel's color vertically up and down, stopping when a non-white pixel or the grid edge is encountered.
    * The result is a "plus" shape centered on the original isolated pixel's location.

3. **Output:** The transformed grid contains only plus-shaped objects created from these isolated pixels. If the horizontal and vertical extensions from different pixels overlap, the color of the horizontal extension in that cell is kept.
"""

import numpy as np

def is_isolated(grid, row, col):
    """Checks if a pixel at (row, col) is isolated."""
    color = grid[row, col]
    if color == 0:  # white pixels are not considered
        return False

    height, width = grid.shape
    neighbors = []

    if row > 0:
        neighbors.append(grid[row - 1, col])  # Up
    else:
        neighbors.append(0)
    if row < height - 1:
        neighbors.append(grid[row + 1, col])  # Down
    else:
        neighbors.append(0)
    if col > 0:
        neighbors.append(grid[row, col - 1])  # Left
    else:
        neighbors.append(0)
    if col < width - 1:
        neighbors.append(grid[row, col + 1])  # Right
    else:
        neighbors.append(0)

    for neighbor_color in neighbors:
        if neighbor_color != 0:
            return False  # Not isolated if any neighbor is not white

    return True

def transform(input_grid):
    """Transforms the input grid according to the rules."""
    input_grid = np.array(input_grid)  # Ensure it is numpy array
    output_grid = np.zeros_like(input_grid) # initialize with all zeros
    height, width = input_grid.shape

    isolated_pixels = []
    for row in range(height):
        for col in range(width):
            if is_isolated(input_grid, row, col):
                isolated_pixels.append((row, col, input_grid[row, col]))

    for row, col, color in isolated_pixels:
        # Horizontal Extension
        # Left
        for c in range(col, -1, -1):
            if input_grid[row,c] == 0:
                output_grid[row,c] = color
            else:
                output_grid[row,c] = color #include original
                break #stop extension
        # Right
        for c in range(col+1, width):
             if input_grid[row,c] == 0:
                output_grid[row,c] = color
             else:
                break #stop extension

        # Vertical Extension
        #Up
        for r in range(row, -1, -1):
            if input_grid[r,col] == 0:
                output_grid[r,col] = color
            else:
                output_grid[r,col] = color #include original
                break
        #Down
        for r in range(row + 1, height):
            if input_grid[r,col] == 0:
                output_grid[r,col] = color
            else:
                break


    return output_grid.tolist()