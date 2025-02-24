"""
The transformation rule is to "crop" the input grid by removing the outer "frame" from each edge. The frame consists of contiguous pixels of the same color starting from each edge and extending inwards until a different color is encountered.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts the internal region of the input grid by removing the border of the dominant color.
    The border is defined as contiguous blocks of the dominant color starting from edges.
    """
    grid = np.array(input_grid)
    rows, cols = grid.shape

    min_row, max_row = 0, rows - 1
    min_col, max_col = 0, cols - 1

    # Find top boundary
    top_color = grid[0, 0]
    for r in range(rows):
        if any(grid[r, :] != top_color):
            min_row = r
            break
        elif r == rows -1:
            min_row = rows

    # Find bottom boundary
    bottom_color = grid[-1, 0]
    for r in range(rows - 1, -1, -1):
        if any(grid[r, :] != bottom_color):
            max_row = r
            break
        elif r == 0:
            max_row = -1

    # Find left boundary
    left_color = grid[0,0]
    for c in range(cols):
        if any(grid[:, c] != left_color):
            min_col = c
            break
        elif c == cols -1:
            min_col = cols

    # Find right boundary
    right_color = grid[0, -1]
    for c in range(cols - 1, -1, -1):
        if any(grid[:, c] != right_color):
            max_col = c
            break
        elif c == 0:
           max_col = -1
            

    # Extract the internal region
    output_grid = grid[min_row:max_row+1, min_col:max_col+1]

    return output_grid.tolist()