"""
1. **Identify Isolated Pixels:** Scan the input grid and identify all "isolated pixels." An isolated pixel is defined as a pixel whose color is different from all four of its immediate neighbors (up, down, left, and right).
2.  **For Each Isolated Pixel**:
    -   Record the pixel's original `color` and `position`.
    -   **Horizontal Extension:** 
       -    Fill empty positions to the left and to the right of the original position with same color.
    -   **Vertical Extension:**
        -  Fill empty positions on top and to the bottom of the original position with the same color.
3.  **Output:** The resulting grid, with extended lines from each of the isolated pixels, is the final output.
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
    if row < height - 1:
        neighbors.append(grid[row + 1, col])  # Down
    if col > 0:
        neighbors.append(grid[row, col - 1])  # Left
    if col < width - 1:
        neighbors.append(grid[row, col + 1])  # Right

    for neighbor_color in neighbors:
        if neighbor_color == color:
            return False  # Not isolated if any neighbor has the same color

    return True

def transform(input_grid):
    """Transforms the input grid according to the rules."""
    input_grid = np.array(input_grid)  # Ensure it is numpy array
    output_grid = np.copy(input_grid)
    height, width = input_grid.shape

    isolated_pixels = []
    for row in range(height):
        for col in range(width):
            if is_isolated(input_grid, row, col):
                isolated_pixels.append((row, col, input_grid[row, col]))

    for row, col, color in isolated_pixels:
        # Horizontal Extension
        for c in range(width):
            if output_grid[row,c] == 0: #fill if white
                output_grid[row, c] = color

        # Vertical Extension
        for r in range(height):
            if output_grid[r,col] == 0: #fill if white
                output_grid[r, col] = color

    return output_grid.tolist()