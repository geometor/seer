"""
Transforms an input grid by expanding a vertical orange line into a checkerboard pattern of orange and azure, leaving the area below the line unchanged.
"""

import numpy as np

def find_orange_line(grid):
    """Finds the vertical orange line in the grid."""
    rows, cols = grid.shape
    for j in range(cols):
        for i in range(rows):
            if grid[i, j] == 7:
                # Found start of potential line
                start_row = i
                end_row = i
                while end_row + 1 < rows and grid[end_row + 1, j] == 7:
                    end_row += 1
                return start_row, end_row, j
    return None, None, None

def expand_to_checkerboard(grid, start_row, end_row, col):
    """Expands the orange line to a checkerboard."""
    output_grid = np.copy(grid)
    rows, cols = grid.shape

    # Determine top row and fill with orange, working out from the line.
    top_row = start_row -1
    if top_row >= 0:
       if grid[top_row, col] == 0:
          output_grid[top_row,col] = 7
       #fill left
       for j in range(col - 1, -1, -1):
           if grid[top_row, j] == 0:
               output_grid[top_row, j] = 7
           else:
               break
       #fill right
       for j in range(col + 1, cols):
           if grid[top_row, j] == 0:
              output_grid[top_row, j] = 7
           else:
              break
    
    # Checkerboard expansion from top_row down to end_row (exclusive)
    for i in range(top_row, end_row):  # Iterate *down* to end_row
        for j in range(cols):
            if output_grid[i, j] == 7:  # Check if the current cell is part of the line
                # Fill to the right
                for k in range(j + 1, cols):
                    if output_grid[i, k] == 0:
                        if output_grid[i,k-1] == 7:
                           output_grid[i, k] = 8
                        else:
                           output_grid[i,k] = 7
                    else:
                        break  # Stop at non-white
                #Fill to the Left
                for k in range(j-1, -1,-1):
                    if output_grid[i, k] == 0:
                        if output_grid[i,k+1] == 7:
                           output_grid[i,k] = 8
                        else:
                           output_grid[i,k] = 7
                    else:
                       break
    return output_grid

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    start_row, end_row, col = find_orange_line(input_grid)

    if start_row is None:  # No orange line found
        return np.copy(input_grid)

    output_grid = expand_to_checkerboard(input_grid, start_row, end_row, col)
    return output_grid