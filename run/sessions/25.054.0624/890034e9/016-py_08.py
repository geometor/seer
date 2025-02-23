"""
Identify a central shape made of yellow (color 4) pixels. The yellow shape itself is unchanged.
Only colors on the border of the yellow shape can change, and only if they are different in the input vs the output grid. Colors other than yellow on the border of the central shape are updated. If a border pixel
has the same color in both input and output, it remains unchanged. Otherwise, the border pixel's color is updated
to its color in the output grid.
"""

import numpy as np

def find_central_shape(grid, shape_color=4):
    # Find all shape_color pixels
    shape_pixels = np.argwhere(grid == shape_color)
    
    # if no shape color is found, return empty list
    if len(shape_pixels) == 0:
        return []

    # Return the coordinates
    return shape_pixels.tolist()

def find_border_pixels(grid, shape_pixels):
    border_pixels = set()
    rows, cols = grid.shape
    
    # Directions to check for neighbors (including diagonals)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    for r, c in shape_pixels:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] != 4:
                border_pixels.add((nr, nc))

    return list(border_pixels)

def transform(input_grid, output_grid):
    # Create a copy of the input grid to modify
    output_grid_copy = np.copy(input_grid)

    # Find the central yellow shape
    shape_pixels = find_central_shape(input_grid)

    # Find pixels on border of shape
    border_pixels = find_border_pixels(input_grid, shape_pixels)

    # Modify colors other than yellow at border
    for r, c in border_pixels:
        #if the colors in the input and the given output grids are the same
        if input_grid[r,c] == output_grid[r,c]:
            #keep colors
            output_grid_copy[r,c] = input_grid[r,c]
        else:
            #update border color to the color in the output_grid
            output_grid_copy[r, c] = output_grid[r,c]

    return output_grid_copy