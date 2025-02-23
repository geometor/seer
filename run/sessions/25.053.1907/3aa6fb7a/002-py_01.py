"""
If two azure pixels are diagonally adjacent, change one of the pixel to blue.
"""

import numpy as np

def get_azure_pixels(grid):
    # find coordinates of all azure pixels
    return np.argwhere(grid == 8)

def are_diagonally_adjacent(coord1, coord2):
    # check if two coordinates are diagonally adjacent
    return abs(coord1[0] - coord2[0]) == 1 and abs(coord1[1] - coord2[1]) == 1

def transform(input_grid):
    """
    Transforms the input grid according to the rule: If two azure pixels are
    diagonally adjacent, change one of them to blue.
    """
    output_grid = np.copy(input_grid)
    azure_pixels = get_azure_pixels(output_grid)

    # Iterate through all pairs of azure pixels
    for i in range(len(azure_pixels)):
        for j in range(i + 1, len(azure_pixels)):
            if are_diagonally_adjacent(azure_pixels[i], azure_pixels[j]):
                # Change one of the diagonally adjacent azure pixels to blue (1)
                output_grid[azure_pixels[i][0], azure_pixels[i][1]] = 1
                # only change one, then break the inner loop
                break

    return output_grid