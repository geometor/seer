"""
The transformation extracts a 3x3 subgrid from the input grid. The subgrid represents
a "zoomed-in" portion of the input, where each pixel in the output corresponds to a 3x3
block of the same color in the input. The transformation identifies the top-leftmost
occurrence of the repeating pattern.
"""

import numpy as np

def find_pattern_start(input_grid):
    """
    Finds the top-left corner of the repeating 3x3 pattern.
    """
    rows, cols = input_grid.shape
    for r in range(rows - 2):
        for c in range(cols - 2):
            # Check if the current 3x3 block is part of the repeating pattern
            if is_part_of_pattern(input_grid, r, c):
                return r, c
    return None, None

def is_part_of_pattern(input_grid, r, c):
    """
    Checks if the 3x3 subgrid at (r, c) is part of the repeating pattern.
    This involves checking if adjacent 3x3 blocks have the same color.
    """
    # Get the color of the current block
    block_color = input_grid[r, c]

    # Check adjacent blocks (right and down)
    if c + 3 < input_grid.shape[1] and input_grid[r, c + 3] != block_color:
        return False
    if r + 3 < input_grid.shape[0] and input_grid[r + 3, c] != block_color:
      return False
    
    # Check for non uniform colors neighboring
    if c > 0 and input_grid[r, c-1] == block_color:
      return False
    
    if r > 0 and input_grid[r-1, c] == block_color:
      return False

    # All adjacent same color blocks checked, and it is top-left.
    return True


def transform(input_grid):
    # Find the top-left corner of the repeating pattern
    r, c = find_pattern_start(input_grid)

    # If no pattern is found, return None (do not provide default output)
    if r is None or c is None:
        return None  # Or raise an exception, depending on desired behavior

    # Extract and return the 3x3 subgrid
    output_grid = input_grid[r:r+3, c:c+3]
    return output_grid