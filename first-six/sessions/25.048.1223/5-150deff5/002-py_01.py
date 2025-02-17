"""
The input grid contains a gray object (color 5) shaped like a mirrored and rotated "F". This object is decomposed and recolored: the top 2x2 square and the "arms" extending to the sides become azure (color 8), while the central vertical "stem" becomes red (color 2). The background (color 0) remains unchanged.
"""

import numpy as np

def find_object(grid, color):
    """Finds the coordinates of an object with the given color."""
    coords = []
    for r_idx, row in enumerate(grid):
        for c_idx, cell in enumerate(row):
            if cell == color:
                coords.append((r_idx, c_idx))
    return coords

def transform(input_grid):
    """Transforms the input grid according to the described rule."""

    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find the gray object (color 5)
    gray_object_coords = find_object(input_grid, 5)

    # Recolor the top 2x2 square and arms to azure (color 8)
    for r, c in gray_object_coords:
        if (r == gray_object_coords[0][0] or r == gray_object_coords[0][0] + 1) and \
           (c == gray_object_coords[0][1] or c== gray_object_coords[0][1] + 1):
            output_grid[r, c] = 8
        if (r == gray_object_coords[0][0] + 1) and ( c > gray_object_coords[0][1]+1 ):
            output_grid[r,c] = 8
        if (r == gray_object_coords[-1][0]-1) and (c == gray_object_coords[-1][1] or c == gray_object_coords[-1][1]+1):
            output_grid[r,c] = 8

    # Recolor the "stem" to red (color 2)

    for r, c in gray_object_coords:
      if r>=gray_object_coords[0][0]+2 and c > gray_object_coords[0][1]+1 and c < gray_object_coords[-1][1]:
        output_grid[r,c]=2

    return output_grid