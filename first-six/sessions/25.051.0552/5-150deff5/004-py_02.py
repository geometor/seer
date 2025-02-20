"""
1. Find every gray (color 5) pixel.
2. Recolor them to azure (8).
3. Check the neighbors of each gray pixel *before* recoloring.
4. If the neighbors are all gray, replace the center with red (2).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule:
    Gray (5) pixels are recolored to azure (8), and if a gray pixel has
    all gray neighbors (up, down, left, right), it's replaced with red (2).
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if output_grid[i, j] == 5:
                # Recolor gray pixels to azure
                output_grid[i, j] = 8

                # Check neighbors (up, down, left, right) in the input grid
                up = i > 0 and input_grid[i - 1, j] == 5
                down = i < rows - 1 and input_grid[i + 1, j] == 5
                left = j > 0 and input_grid[i, j - 1] == 5
                right = j < cols - 1 and input_grid[i, j + 1] == 5

                # If all neighbors are gray, replace with red
                if up and down and left and right:
                    output_grid[i, j] = 2

    return output_grid