# 3aa6fb7a • 004 • refine_coder

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

def get_bottom_right(coord1, coord2):
    # Return the coordinate that is more bottom-right
     if coord1[0] > coord2[0] or (coord1[0] == coord2[0] and coord1[1] > coord2[1]):
        return coord1
     else:
        return coord2

def transform(input_grid):
    """
    Transforms the input grid according to the rule: If two azure pixels are
    diagonally adjacent, change one of them to blue, prioritizing the top-left one.
    """
    output_grid = np.copy(input_grid)
    azure_pixels = get_azure_pixels(output_grid)

    # Iterate through all pairs of azure pixels
    for i in range(len(azure_pixels)):
        for j in range(i + 1, len(azure_pixels)):
            if are_diagonally_adjacent(azure_pixels[i], azure_pixels[j]):
                # Determine top-left and bottom-right pixel
                top_left = get_top_left(azure_pixels[i], azure_pixels[j])
                bottom_right = get_bottom_right(azure_pixels[i], azure_pixels[j])

                # Change the top-left pixel
                output_grid[top_left[0], top_left[1]] = 1
                
    return output_grid
```
