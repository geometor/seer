"""
1.  **Identify Target Pixels:** Examine the input grid and locate all pixels with the value '3' (green).
2.  **Check for Adjacency:** For each identified '3' pixel, check if it has any adjacent pixels (horizontally or vertically, but not diagonally) that also have the value '3'.
3.  **Modify Central Pixels :** If a '3' pixel *has one neighbor*, keep original '3' value.
4.  **Modify Connected Pixels:** If a '3' pixel has more than one horizontal/vertical adjacent pixels with value '3', change its value to '4' (yellow).
5.  **Output:** Create the output grid with the modified pixel values, leaving all other pixels unchanged.
"""

import numpy as np

def get_adjacent_pixels(grid, row, col):
    """
    Gets the values of adjacent pixels (up, down, left, right).
    """
    rows, cols = grid.shape
    adjacent = []
    if row > 0:
        adjacent.append(grid[row-1, col])  # Up
    if row < rows - 1:
        adjacent.append(grid[row+1, col])  # Down
    if col > 0:
        adjacent.append(grid[row, col-1])  # Left
    if col < cols - 1:
        adjacent.append(grid[row, col+1])  # Right
    return adjacent

def transform(input_grid):
    # initialize output_grid with a copy of the input grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # iterate through each pixel in the input grid
    for row in range(rows):
        for col in range(cols):
            # identify target pixels (value '3')
            if input_grid[row, col] == 3:
                # check for adjacency
                adjacent_pixels = get_adjacent_pixels(input_grid, row, col)
                count_of_3_neighbors = adjacent_pixels.count(3)

                # modify connected pixels based on the number of adjacent '3' pixels
                if count_of_3_neighbors > 1:
                    output_grid[row, col] = 4

    return output_grid