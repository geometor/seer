"""
The transformation rule is as follows:
1. Identify a green "L" shaped object and a red cell in the input grid.
2. Remove the red object.
3. Expand the green object into a partial, downwards-pointing 5x5 tilted "square" shape.

"""

import numpy as np

def find_object(grid, color):
    """Finds coordinates of cells with a specific color."""
    coords = []
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r,c] == color:
                coords.append((r, c))
    return coords

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""
    output_grid = np.zeros_like(input_grid)

    # 1. Identify Objects
    green_coords = find_object(input_grid, 3)
    # red_coords = find_object(input_grid, 2)

    # 2 & 3. Expand green and remove red
    if len(green_coords) > 0:
        start_row = green_coords[0][0]
        start_col = green_coords[0][1]

        for i in range(5):
            for j in range(5):
                row = start_row + i - j
                col = start_col + i + j-1
                if 0 <= row < output_grid.shape[0] and 0 <= col < output_grid.shape[1] and not(i<3 and j<3):
                    output_grid[row, col] = 3

    return output_grid