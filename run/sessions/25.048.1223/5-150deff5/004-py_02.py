"""
The input grid contains a gray object (color 5). This object is decomposed and recolored: The pixels in the first two rows that are color 5 are changed to color 8 (azure) if they are in the extremes, and color 2 if they are in between. The vertical "stem" of the shape (pixels of color 5 at column 3 from the second row) are changed to color 2 (red). The pixels in the "arms" (pixels connected horizontally with the shape) change to color 8 in rows where they are connected to the azure pixels. The background (color 0) remains unchanged.
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
    
    # Recolor the top two rows
    for r, c in gray_object_coords:
        if r == min_row or r == min_row + 1:
            if c == min_col or c == min_col + 1 or c == max_col or c == max_col -1:
                output_grid[r, c] = 8  # Azure
            elif c>min_col+1 and c < max_col -1:
                output_grid[r,c] = 2

    # Recolor the "stem" to red (color 2)
    for r, c in gray_object_coords:
        if min_row + 1 < r and c == min_col + 2 :
          output_grid[r, c] = 2  # Red
        if r > min_row + 1 and (c == max_col -2 or c == max_col-3):
            if output_grid[r-1,c] == 8 :
                output_grid[r,c] = 8

    return output_grid