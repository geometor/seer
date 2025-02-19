"""
The transformation rule is as follows: Find all azure (8) pixels in the input grid. Sort them based on the sum of their row and column indices (x + y).  For the two azure pixels with the smallest sums, place a blue pixel (1) one position below each (increase row index by 1). For the azure pixel with the largest sum, place a blue pixel (1) one position to the left (decrease column index by 1).
"""

import numpy as np

def find_azure_objects(grid):
    # Find coordinates of all azure (8) pixels.
    azure_coords = np.argwhere(grid == 8)
    return azure_coords

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.
    output_grid = np.copy(input_grid)

    # Find all azure objects.
    azure_coords = find_azure_objects(input_grid)

    if len(azure_coords) > 0:
        # Sort by sum of coordinates (x+y)
        coords_sum = azure_coords[:, 0] + azure_coords[:, 1]
        sorted_indices = np.argsort(coords_sum)
        sorted_coords = azure_coords[sorted_indices]

        # Place blue pixels based on sorted azure coordinates
        if len(sorted_coords) >= 1:
            output_grid[sorted_coords[0][0] + 1, sorted_coords[0][1]] = 1
        if len(sorted_coords) >= 2:
             output_grid[sorted_coords[1][0] + 1, sorted_coords[1][1]] = 1

        if len(sorted_coords) >=3:
            output_grid[sorted_coords[-1][0] - 1, sorted_coords[-1][1]] = 1

    return output_grid