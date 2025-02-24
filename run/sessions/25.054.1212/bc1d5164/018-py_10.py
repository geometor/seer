"""
The transformation rule identifies the outermost pixels of a non-zero color within a bounding box in the input grid and maps them onto a 3x3 output grid, preserving their relative positions. The remaining cells in the output grid are filled with white (0) pixels.
"""

import numpy as np

def get_bounding_box(input_grid):
    """
    Finds the bounding box of the non-zero pixels in the input grid.
    Returns (min_row, min_col, max_row, max_col).
    """
    rows, cols = len(input_grid), len(input_grid[0])
    min_row, min_col = rows, cols
    max_row, max_col = -1, -1

    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] != 0:
                min_row = min(min_row, r)
                min_col = min(min_col, c)
                max_row = max(max_row, r)
                max_col = max(max_col, c)

    return min_row, min_col, max_row, max_col

def get_outermost_pixels(input_grid, bounding_box, outermost_color):
    """
    Extracts the outermost pixels within the bounding box.
    """
    min_row, min_col, max_row, max_col = bounding_box
    outermost_pixels = []

    for r in range(min_row, max_row + 1):
        for c in range(min_col, max_col + 1):
            if input_grid[r][c] == outermost_color:
                if r == min_row or r == max_row or c == min_col or c == max_col:
                  outermost_pixels.append((r, c))
    return outermost_pixels

def transform(input_grid):
    """
    Transforms the input grid according to the rule: extracts outermost pixels
    within a bounding box, places them on 3x3 grid, and fills the rest with '0's.
    """
    # initialize output_grid
    output_grid = np.zeros((3, 3), dtype=int)

    # Find the bounding box
    bounding_box = get_bounding_box(input_grid)
    min_row, min_col, max_row, max_col = bounding_box

    # Handle empty bounding box (all zeros)
    if min_row > max_row or min_col > max_col:
        return output_grid.tolist()
    
    # get the color
    outermost_color = input_grid[min_row][min_col]

    # Extract outermost pixels
    outermost_pixels = get_outermost_pixels(input_grid, bounding_box, outermost_color)

    # Map outermost pixels to the output grid
    for r, c in outermost_pixels:
        # Normalize row and col to fit in the 3x3 grid
        if r == min_row:
            norm_row = 0
        elif r == max_row:
            norm_row = 2
        else:
            norm_row = 1

        if c == min_col:
            norm_col = 0
        elif c == max_col:
            norm_col = 2
        else:
            norm_col = 1

        output_grid[norm_row, norm_col] = outermost_color

    return output_grid.tolist()