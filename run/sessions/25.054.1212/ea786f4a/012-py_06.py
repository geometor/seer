"""
Transforms a grid by inverting the color of the frame pixels (changing non-zero pixels to 0) 
and setting adjacent pixels to 0 as well, while preserving the center pixel's original color.
"""

import numpy as np

def get_frame_indices(grid):
    """Returns a list of (row, col) tuples representing the frame indices."""
    rows, cols = grid.shape
    frame = []
    for r in range(rows):
        for c in range(cols):
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                frame.append((r, c))
    return frame

def get_adjacent_indices(grid, row, col):
    """Returns a list of valid adjacent indices (up, down, left, right)."""
    rows, cols = grid.shape
    adjacent = []
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            adjacent.append((new_row, new_col))
    return adjacent

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Identify the center pixel coordinates
    center_row = rows // 2
    center_col = cols // 2

    # Get frame indices
    frame_indices = get_frame_indices(input_grid)
    
    # Find adjacent pixels to non-zero frame pixels *before* inverting
    adjacent_to_frame = []
    for r, c in frame_indices:
        if input_grid[r, c] != 0:
            adjacent_to_frame.extend(get_adjacent_indices(input_grid, r, c))

    # Invert frame pixels (non-zero to 0)
    for r, c in frame_indices:
        if output_grid[r, c] != 0:
             output_grid[r, c] = 0

    # Set adjacent pixels to 0
    for r, c in adjacent_to_frame:
        if (r,c) != (center_row, center_col): #don't change center pixel
           output_grid[r, c] = 0

    return output_grid