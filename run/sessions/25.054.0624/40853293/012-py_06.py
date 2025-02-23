"""
1.  **Identify Isolated Pixels:** Find all non-white pixels that are surrounded by white pixels or the edge of the grid on all four sides (up, down, left, right).

2.  **Create Plus Shapes:** For each isolated pixel:
    *   Extend the pixel's color horizontally, both left and right. Stop the extension in each direction when a non-white pixel or the edge of the grid is reached.
    *   Extend the pixel's color vertically, both up and down. Stop the extension in each direction when a non-white pixel or the edge of the grid is reached.

3.  **Handle Overlaps:** If, during the extension, a pixel's extension would overwrite a pixel that is already part of *another* isolated pixel's extension, maintain the initial isolated pixel color.

4. **Output:** The final grid will consist of these plus-shaped objects, potentially with some overlaps handled as described in step 3.
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
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    height, width = input_grid.shape

    isolated_pixels = []
    for row in range(height):
        for col in range(width):
            if is_isolated(input_grid, row, col):
                isolated_pixels.append((row, col, input_grid[row, col]))

    for row, col, color in isolated_pixels:
        output_grid[row, col] = color # Start with the isolated pixel itself

        # Horizontal Extension
        # Left
        for c in range(col - 1, -1, -1):
            if input_grid[row, c] == 0:
                output_grid[row, c] = color
            else:
                break
        # Right
        for c in range(col + 1, width):
            if input_grid[row, c] == 0:
                output_grid[row, c] = color
            else:
                break

        # Vertical Extension
        # Up
        for r in range(row - 1, -1, -1):
            if input_grid[r, col] == 0:
                output_grid[r, col] = color
            else:
                break
        # Down
        for r in range(row + 1, height):
            if input_grid[r, col] == 0:
                 output_grid[r, col] = color
            else:
                break

    return output_grid.tolist()