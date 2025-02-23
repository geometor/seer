"""
1. Identify Non-White Colors: Examine the entire input grid and create an ordered list of all unique non-white colors present, maintaining their original order of appearance from top to bottom, left to right.
2. Process Each Column: Iterate through each column of the *output* grid.
3. Fill Columns with color sequence: Fill each cell down the column with the ordered color sequence, repeat until the end of the column.
"""

import numpy as np

def get_ordered_non_white_colors(grid):
    """
    Extracts unique non-white colors from the grid in order of appearance.
    """
    rows, cols = grid.shape
    colors = []
    for r in range(rows):
        for c in range(cols):
            color = grid[r, c]
            if color != 0 and color not in colors:
                colors.append(color)
    return colors

def transform(input_grid):
    """
    Transforms the input grid based on a repeating sequence of non-white colors.
    """
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols), dtype=int)

    # 1. Identify Non-White Colors
    non_white_colors = get_ordered_non_white_colors(input_grid)

    # 2. Process Each Column & 3. Fill with color sequence.
    num_colors = len(non_white_colors)
    if num_colors > 0:  # Avoid ZeroDivisionError if no non-white colors
        for c in range(cols):
           for r in range(rows):
                color_index = r % num_colors
                output_grid[r,c] = non_white_colors[color_index]
    return output_grid