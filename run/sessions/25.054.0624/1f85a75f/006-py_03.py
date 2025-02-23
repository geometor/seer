"""
1.  **Find Core Object:** Search for a contiguous 3x3 block of pixels that all have the same color. This is the "core object." Record the color and top-left coordinates.

2.  **Check for White Border:**
    *   Examine the rows immediately above and below the core object. If all pixels in those rows, within the same columns as the core object, are white (0), mark it as having a "full" border for expansion.
    *   If only some are, mark it as a partial border

3. **Determine output height:**
   - If full border, and 3x3 object detected, output size is 5 x 3
   - If partial border, and 3x3 object, output height is 3, and 3 wide

4.  **Create Output Grid:** Create an output grid of the determined size, initialized with white (0).

5.  **Fill Output Grid:**
    *   If there's a *full* white border above and below: Fill the entire output grid with the core object's color, then replace the above and below rows, within the columns of the found object, with 0.
    *   If there is *partial* white border: Fill the output grid according the pattern of the partial border.
    * If there is no border: Fill the output grid with the color of the target object.

6.  **Return:** Return the output grid.
"""

import numpy as np

def find_3x3_square(grid):
    """Finds a 3x3 square of uniform color."""
    rows, cols = grid.shape
    for r in range(rows - 2):
        for c in range(cols - 2):
            color = grid[r, c]
            if np.all(grid[r:r+3, c:c+3] == color):
                return r, c, color
    return None, None, None

def check_border(input_grid, row, col, color):
    """Checks for full or partial white border above/below 3x3."""
    rows, cols = input_grid.shape
    full_border = False
    partial_border = False

    #check above
    if row > 0 and np.all(input_grid[row-1, col:col+3] == 0):
      #check below
      if row + 3 < rows and np.all(input_grid[row+3, col:col+3] == 0):
        full_border = True
      else:
        partial_border = True
    elif row + 3 < rows and np.all(input_grid[row+3, col:col+3] == 0):
        partial_border = True

    return full_border, partial_border

def transform(input_grid):
    """Transforms the input grid based on a 3x3 square and border."""
    row, col, color = find_3x3_square(input_grid)

    if row is None:
        return np.zeros((1, 1), dtype=int)

    full_border, partial_border = check_border(input_grid, row, col, color)
    
    if full_border:
        output_grid = np.full((5, 3), color, dtype=int)
        output_grid[0, :] = 0  # Top border
        output_grid[4, :] = 0  # Bottom border

    elif partial_border:
      output_grid = np.full((3, 3), color, dtype=int)        

    else: #no border
        output_grid = np.full((3, 3), color, dtype=int)

    return output_grid