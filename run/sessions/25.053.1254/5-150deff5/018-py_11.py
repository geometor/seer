"""
Identifies a shape formed by the color gray (value 5) in the input grid and replaces the leftmost part of the shape with red (value 2) and the rightmost part with azure (value 8). The background (white, value 0) remains unchanged.
"""

import numpy as np

def find_shape(grid, shape_value):
    """Finds the coordinates of all pixels belonging to the shape."""
    coords = []
    for r_idx, row in enumerate(grid):
        for c_idx, value in enumerate(row):
            if value == shape_value:
                coords.append((r_idx, c_idx))
    return coords

def find_leftmost_segment(coords):
    """Finds the leftmost vertical segment of the shape."""
    min_col = min(c for _, c in coords)
    leftmost_segment_coords = []
    
    # get the range of the first vertical segment
    for r, c in coords:
      if c == min_col:
        leftmost_segment_coords.append((r,c))

    return leftmost_segment_coords

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    
    shape_coords = find_shape(input_grid, 5)
    if not shape_coords:
        return output_grid

    leftmost_segment = find_leftmost_segment(shape_coords)
    
    # Color Substitution - Left
    for r, c in leftmost_segment:
      output_grid[r,c] = 2

    # Color Substitution - Right
    for r, c in shape_coords:
      if (r,c) not in leftmost_segment:
        output_grid[r, c] = 8

    return output_grid.tolist()