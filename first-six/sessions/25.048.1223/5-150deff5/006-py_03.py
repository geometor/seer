"""
The input grid contains a gray object (color 5). This object is decomposed and recolored: the right extensions become azure (color 8), while the central "stem" and the top horizontal segment become red (color 2). The background (color 0) remains unchanged.
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

    # Get the boundaries of the gray object
    min_row = min(r for r, _ in gray_object_coords)
    #max_row = max(r for r, _ in gray_object_coords)
    min_col = min(c for _, c in gray_object_coords)
    max_col = max(c for _, c in gray_object_coords)

    # Recolor the "stem" and top segment to red (color 2)
    for r, c in gray_object_coords:
        if r == min_row and c <= max_col -2 :
            output_grid[r,c] = 2
        if min_row < r and c == min_col + 3:
            output_grid[r, c] = 2  # Red
        if r > min_row and (c == max_col or c== max_col -1):
            output_grid[r,c] = 8


    return output_grid