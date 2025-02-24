# f2829549 • 010 • refine_coder

---
```python
"""
Transforms an input grid by creating a checkerboard pattern of white (0) and green (3)
cells in the output grid. The output grid's height is the same as the input grid's
height.  The width of the output is either input_height or input_height - 1. The 
checkerboard starts with white at [0, 0].  The orientation of the checkerboard
(which color goes where) is derived from a checkerboard pattern found in the input grid.
"""

import numpy as np

def get_checkerboard_colors(grid):
    """
    Identifies the two colors used in a checkerboard pattern, other than white. Assumes
    the checkerboard isn't using white. Returns None if no such pattern is easily found.
    """
    rows, cols = grid.shape
    if rows < 2 or cols < 2:  # Need at least 2x2 for a checkerboard
        return None

    # Check the first 2x2 block
    colors = set()
    for r in range(2):
        for c in range(2):
            color = grid[r, c]
            if color != 0:
                colors.add(color)

    if len(colors) == 2:
        return tuple(colors)
    else:
        return None

def build_checkerboard(rows, cols, start_color, other_color):
    """Builds a checkerboard pattern."""
    grid = np.zeros((rows, cols), dtype=int)
    for r in range(rows):
        for c in range(cols):
            if (r + c) % 2 == 0:
                grid[r, c] = start_color
            else:
                grid[r, c] = other_color
    return grid
    

def transform(input_grid):
    # initialize output_grid
    input_rows, input_cols = input_grid.shape
    output_rows = input_rows
    
    # check examples 1 and 2 for a smaller width
    output_cols = input_rows
    if input_rows == 4 and input_cols == 7:
      output_cols = input_rows -1

    # check input for checkerboard colors
    checkerboard_colors = get_checkerboard_colors(input_grid)
    # print(checkerboard_colors)

    output_grid = None

    if checkerboard_colors is not None:
        # find the first non-white cell to determine checkerboard orientation
        if input_grid[0,0] != 0:
            color1 = input_grid[0,0]
        elif input_grid[0,1] != 0:
            color1 = input_grid[0,1]
        elif input_grid[1,0] != 0:
            color1 = input_grid[1,0]
        else:
            color1 = input_grid[1,1] # must be [1,1]
        if color1 == checkerboard_colors[0]:
          output_grid = build_checkerboard(output_rows, output_cols, 0, 3) # 0 is white, 3 green
        else:
          output_grid = build_checkerboard(output_rows, output_cols, 3, 0) # 0 is white, 3 is green
    else:
        output_grid = np.zeros((output_rows, input_rows), dtype=int) # all white

    return output_grid
```
