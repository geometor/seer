"""
The transformation rule identifies a trigger color in the input grid and generates a corresponding pattern in the output grid. The trigger color is the non-zero, non-black color present in the input. The output grid is filled with the trigger color, except for cells which are enclosed by other trigger color cells.
"""

import numpy as np

def get_trigger_color(grid):
    """
    Finds the non-zero, non-black color in the grid.
    """
    colors = np.unique(grid)
    for color in colors:
        if color != 0:
            return color
    return 0  # Default to black if no trigger color is found

def is_enclosed(grid, row, col, trigger_color):
    """
    Checks if a cell at the given coordinates is surrounded by the trigger color.
    """
    rows, cols = grid.shape

    # Check boundaries
    if row <= 0 or row >= rows - 1 or col <= 0 or col >= cols - 1:
        return False

    # Check surrounding neighbors
    if (grid[row-1, col] == trigger_color and
        grid[row+1, col] == trigger_color and
        grid[row, col-1] == trigger_color and
        grid[row, col+1] == trigger_color):
        return True
    return False

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # get trigger color
    trigger_color = get_trigger_color(input_grid)

    # if no trigger color, return blank grid
    if trigger_color == 0:
      return output_grid
    
    # mark cells that are enclosed by trigger_color
    enclosed_cells = np.zeros_like(input_grid, dtype=bool)
    for r in range(rows):
      for c in range(cols):
        if input_grid[r,c] == 0:
          enclosed_cells[r,c] = is_enclosed(input_grid, r, c, trigger_color)

    # change output pixels based on whether they should be filled
    for r in range(rows):
        for c in range(cols):
            if not enclosed_cells[r,c]:
                output_grid[r,c] = trigger_color

    return output_grid