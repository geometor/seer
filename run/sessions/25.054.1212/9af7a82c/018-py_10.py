"""
The transformation identifies columns containing the colors 3, 8, 4, or 2, preserves the elements from the top of the column down to and including the first occurrence of these colors within those columns, stacks these preserved sections downwards in the output grid, and sets all cells below the stacked sections to 0. The preserved column sections maintain their 3, 8, 4, 2 order.
"""

import numpy as np

def find_first_occurrence(grid, color):
    """Finds the first occurrence of a color in a grid, column-wise."""
    rows, cols = grid.shape
    for j in range(cols):
        for i in range(rows):
            if grid[i, j] == color:
                return i, j
    return None, None

def transform(input_grid):
    # initialize output_grid
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols), dtype=int)
    color_order = [3, 8, 4, 2]
    
    # find first occurrences and their original column indices
    occurrences = []
    for color in color_order:
        row, col = find_first_occurrence(input_grid, color)
        if row is not None:
            occurrences.append((row, col, color))
    
    # Determine output height based on stacked sections
    output_rows = rows


    output_grid = np.zeros((output_rows, cols), dtype=int)

    # preserve, reorder, and stack in the new grid
    target_col = 0
    for row, col, color in occurrences:
        # Copy the relevant section of the column
        if target_col < cols:
          for i in range(row + 1):
              output_grid[i, target_col] = input_grid[i, col]
          target_col += 1
    
    #zero-out
    for j in range(cols):
       first_non_zero_row = -1
       for i in range(output_rows):
          if output_grid[i][j] != 0:
             first_non_zero_row = i
             break

       if first_non_zero_row != -1:  # found the color
           for i in range(first_non_zero_row + 1, output_rows):
              output_grid[i][j] = 0  # zero out
    

    return output_grid