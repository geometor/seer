"""
The transformation identifies isolated pixels (of any color) in the input grid.  For each isolated pixel, it extends a cross of the same color horizontally and vertically.  These lines stop when they encounter a pixel of a different color (not white/0, and not the same color) or the edge of the grid.
"""

import numpy as np

def is_isolated_revised(grid, row, col):
    """Checks if a pixel is isolated (not adjacent to same-color pixels)."""
    color = grid[row, col]
    if color == 0: #white, can't be isolated by definition in this challenge.
        return False

    height, width = grid.shape
    for i in range(max(0, row - 1), min(height, row + 2)):
        for j in range(max(0, col - 1), min(width, col + 2)):
            if (i, j) != (row, col) and grid[i, j] == color:
                return False  # Found an adjacent pixel of same color
    return True

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    height, width = input_grid.shape

    # Iterate through each cell in the grid
    for row in range(height):
        for col in range(width):
            # Check for isolated pixels
            if is_isolated_revised(input_grid, row, col):
                color = input_grid[row,col]
                # Horizontal expansion (left)
                for j in range(col - 1, -1, -1):
                    if input_grid[row, j] == 0 or input_grid[row,j] == color:
                        output_grid[row, j] = color
                    else:
                        break
                # Horizontal expansion (right)
                for j in range(col + 1, width):
                    if input_grid[row, j] == 0 or input_grid[row,j] == color:
                        output_grid[row, j] = color
                    else:
                        break
                # Vertical expansion (up)
                for i in range(row - 1, -1, -1):
                    if input_grid[i, col] == 0 or input_grid[i,col] == color:
                        output_grid[i, col] = color
                    else:
                        break
                # Vertical expansion (down)
                for i in range(row + 1, height):
                    if input_grid[i, col] == 0 or input_grid[i,col] == color:
                        output_grid[i, col] = color
                    else:
                        break

    return output_grid