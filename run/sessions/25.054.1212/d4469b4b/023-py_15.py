"""
1.  **Initialization:** Create a 3x3 output grid.
2.  **Border Creation and Center Fill Rule:** Iterate through the inner 3x3 region of the 5x5 input grid.
    *   Consider each pixel within the inner 3x3 region and it's *immediate horizontal and vertical neighbors* (up, down, left, right). Diagonal neighbors are *not* considered.
    *   If the considered pixel and all immediate horizontal and vertical neighbors are 0 (background), then the corresponding pixel in the output grid is set to 0.
    *    Otherwise, the corresponding output pixel *and its immediate horizontal and vertical neighbors* are set to 5. This creates the border around the central pixel.
3.  **Output:** The 3x3 output grid is the result.
"""

import numpy as np

def get_neighbors(grid, row, col):
    # Get immediate horizontal and vertical neighbors
    neighbors = []
    rows, cols = grid.shape
    if row > 0:
        neighbors.append(grid[row-1, col])  # Up
    if row < rows - 1:
        neighbors.append(grid[row+1, col])  # Down
    if col > 0:
        neighbors.append(grid[row, col-1])  # Left
    if col < cols - 1:
        neighbors.append(grid[row, col+1])  # Right
    return neighbors

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros((3, 3), dtype=int)

    # Iterate through the inner 3x3 region of the input grid
    for i in range(1, 4):
        for j in range(1, 4):
            # Get the pixel value and its neighbors
            center_pixel = input_grid[i, j]
            neighbors = get_neighbors(input_grid, i, j)

            # Check if the center pixel and all neighbors are 0
            if center_pixel == 0 and all(n == 0 for n in neighbors):
                output_grid[i-1, j-1] = 0
            else:
                # Set the corresponding output pixel and its neighbors to 5
                output_grid[i-1, j-1] = 5
                if i - 1 > 0:
                    output_grid[i-2,j-1] = 5
                if i - 1 < 2:
                    output_grid[i,j-1] = 5
                if j - 1 > 0:
                    output_grid[i-1,j-2] = 5
                if j - 1 < 2:
                    output_grid[i-1, j] = 5

    return output_grid