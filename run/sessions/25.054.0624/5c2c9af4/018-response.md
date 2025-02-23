# 5c2c9af4 • 018 • refine_coder

---
```python
"""
The transformation identifies isolated pixels (of any color) in the input grid. A pixel is isolated if it's not white (0) and none of its four immediate neighbors (up, down, left, right) have the same color. For each isolated pixel, a cross of the same color is drawn, extending horizontally and vertically. The arms of the cross stop when they reach the edge of the grid or a pixel that is neither white (0) nor the same color as the isolated pixel.
"""

import numpy as np

def is_isolated(grid, row, col):
    """Checks if a pixel is isolated (not adjacent to same-color pixels, excluding diagonals)."""
    color = grid[row, col]
    if color == 0:  # White pixels are not considered isolated
        return False

    height, width = grid.shape
    neighbors = []

    # Check up, down, left, and right neighbors
    if row > 0:
        neighbors.append(grid[row - 1, col])  # Up
    if row < height - 1:
        neighbors.append(grid[row + 1, col])  # Down
    if col > 0:
        neighbors.append(grid[row, col - 1])  # Left
    if col < width - 1:
        neighbors.append(grid[row, col + 1])  # Right

    # Check if any neighbor has the same color
    for neighbor_color in neighbors:
        if neighbor_color == color:
            return False  # Not isolated

    return True  # Isolated


def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    height, width = input_grid.shape

    # Iterate through each pixel
    for row in range(height):
        for col in range(width):
            # Check if the pixel is isolated
            if is_isolated(input_grid, row, col):
                color = input_grid[row, col]

                # Expand horizontally to the left
                j = col - 1
                while j >= 0 and (output_grid[row, j] == 0 or output_grid[row,j] == color):
                    output_grid[row, j] = color
                    j -= 1

                # Expand horizontally to the right
                j = col + 1
                while j < width and (output_grid[row, j] == 0 or output_grid[row,j] == color):
                    output_grid[row, j] = color
                    j += 1

                # Expand vertically upwards
                i = row - 1
                while i >= 0 and (output_grid[i, col] == 0 or output_grid[i,col] == color):
                    output_grid[i, col] = color
                    i -= 1

                # Expand vertically downwards
                i = row + 1
                while i < height and (output_grid[i, col] == 0 or output_grid[i,col] == color):
                    output_grid[i, col] = color
                    i += 1

    return output_grid
```
