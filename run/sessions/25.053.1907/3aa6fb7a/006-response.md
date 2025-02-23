# 3aa6fb7a • 006 • refine_coder

---
```python
"""
If two azure pixels are diagonally adjacent, change one of the pixel to blue.
Prioritize changing the top-left pixel in a diagonally adjacent pair.
If not top-left, change the bottom-right pixel.
"""

import numpy as np

def get_azure_pixels(grid):
    # find coordinates of all azure pixels
    return np.argwhere(grid == 8)

def are_diagonally_adjacent(coord1, coord2):
    # check if two coordinates are diagonally adjacent
    return abs(coord1[0] - coord2[0]) == 1 and abs(coord1[1] - coord2[1]) == 1

def get_top_left(coord1, coord2):
    # Return the coordinate that is more top-left.
    if coord1[0] < coord2[0] or (coord1[0] == coord2[0] and coord1[1] < coord2[1]):
        return coord1
    else:
        return coord2

def transform(input_grid):
    """
    Transforms the input grid according to the rule: If two azure pixels are
    diagonally adjacent, change the top-left one of the pair to blue.
    """
    output_grid = np.copy(input_grid)
    azure_pixels = get_azure_pixels(output_grid)
    changed_pixels = set()  # Keep track of changed pixels

    # Iterate through all pairs of azure pixels
    for i in range(len(azure_pixels)):
        for j in range(i + 1, len(azure_pixels)):
            coord1 = tuple(azure_pixels[i])
            coord2 = tuple(azure_pixels[j])

            if coord1 in changed_pixels or coord2 in changed_pixels:
                continue # skip if one has been changed already in a prior compare

            if are_diagonally_adjacent(coord1, coord2):
                # Determine top-left pixel in the pair
                top_left = get_top_left(coord1, coord2)

                # Change the top-left pixel in the pair to blue
                output_grid[top_left] = 1
                changed_pixels.add(top_left) # add to set to prevent re-checking

    return output_grid
```
