"""
Transformation Rule:
The azure (8) objects remain unchanged.
A blue (1) pixel is added to the immediate left of the topmost horizontal azure line.
A blue (1) pixel is added to the immediate right of the topmost vertical azure line.
A blue (1) pixel is added to the immediate left of the top of the next vertical line.

"""

import numpy as np

def find_topmost_horizontal_line(grid, color):
    """Finds the topmost horizontal line of a given color."""
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols - 1):
            if grid[r, c] == color and grid[r, c+1] == color:
                return r, c
    return None

def find_topmost_vertical_lines(grid, color):
    """Finds the topmost vertical lines of a given color, handling duplicates."""
    rows, cols = grid.shape
    vertical_lines = []
    for c in range(cols):
        for r in range(rows - 1):
            if grid[r, c] == color and grid[r+1, c] == color:
                vertical_lines.append((r, c))
    # Sort by row and then by column to handle duplicates, returning distinct lines
    vertical_lines = sorted(set(vertical_lines), key=lambda x: (x[0], x[1]))
    return vertical_lines
    

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""
    output_grid = np.copy(input_grid)

    # Find the topmost horizontal line of color 8
    top_horizontal = find_topmost_horizontal_line(output_grid, 8)
    if top_horizontal:
        r, c = top_horizontal
        # Add a blue pixel (1) to the left
        if c > 0:
            output_grid[r, c - 1] = 1

    # Find the topmost vertical lines of color 8
    top_verticals = find_topmost_vertical_lines(output_grid, 8)
    if top_verticals:
      if len(top_verticals) >= 1:
        # Add a blue pixel (1) to the right of the first (topmost) line
        r,c = top_verticals[0]
        if c+1 < output_grid.shape[1]:
          output_grid[r, c + 1] = 1
      if len(top_verticals) >= 2:  #check there is enough vertical lines
        # Add a blue pixel (1) to the left of the second (next topmost)
        r,c = top_verticals[1]
        if c > 0:
          output_grid[r,c-1] = 1


    return output_grid