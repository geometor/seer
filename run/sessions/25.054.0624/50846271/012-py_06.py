"""
1.  **Iterate through Pixels:** Iterate through each pixel of the input grid.

2.  **Check for Gray:** If the current pixel is gray (color value 5), proceed to the next step. Otherwise, keep the pixel's original color in the output.

3.  **Check Cardinal Neighbors for Red:** For the current gray pixel, check its four cardinally adjacent neighbors (up, down, left, right).

4.  **Conditional Color Change (Pixel-Based):** If *any* of the cardinal neighbors is red (color value 2), change the current gray pixel to azure (color value 8) in the output grid.

5.  **Preserve Other Pixels:** If the current pixel is not gray, or if it is gray but none of its cardinal neighbors are red, keep its original color in the output grid.  This is handled implicitly by copying the input grid initially.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """Gets the cardinal neighbors of a pixel."""
    rows, cols = grid.shape
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))  # Up
    if row < rows - 1:
        neighbors.append((row + 1, col))  # Down
    if col > 0:
        neighbors.append((row, col - 1))  # Left
    if col < cols - 1:
        neighbors.append((row, col + 1))  # Right
    return neighbors

def transform(input_grid):
    """Transforms the input grid according to the described rule."""

    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # 1. Iterate through Pixels
    for row in range(rows):
        for col in range(cols):
            # 2. Check for Gray
            if input_grid[row, col] == 5:
                # 3. Check Cardinal Neighbors for Red
                neighbors = get_neighbors(input_grid, row, col)
                for n_row, n_col in neighbors:
                    if input_grid[n_row, n_col] == 2:
                        # 4. Conditional Color Change (Pixel-Based)
                        output_grid[row, col] = 8
                        break  # Change color and move to the next pixel

    # 5. Preserve Other Pixels (already handled by initializing output_grid as a copy)
    return output_grid