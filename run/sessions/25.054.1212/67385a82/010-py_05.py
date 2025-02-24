"""
Identifies horizontal runs of contiguous green pixels. If a run has length 2 or more,
change all pixels in that run to azure. If a run has length 1, and is adjacent to
any pixel that has already been changed to azure, change to azure.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by changing horizontally contiguous green pixels to azure based on run length.
    
    Args:
        input_grid (list of lists): The input grid represented as a list of lists.
    
    Returns:
        list of lists: The transformed grid.
    """
    output_grid = [row[:] for row in input_grid]  # Create a copy to avoid modifying the original
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0

    # 1. Identify and Measure Horizontal Runs
    runs = []  # List to store (row, start_col, end_col) of each run
    for r in range(rows):
        start_col = -1
        for c in range(cols):
            if input_grid[r][c] == 3:
                if start_col == -1:
                    start_col = c
            elif start_col != -1:
                runs.append((r, start_col, c - 1))
                start_col = -1
        if start_col != -1:  # Handle runs that extend to the end of the row
            runs.append((r, start_col, cols - 1))

    # 2. Change pixels based on run length (>= 2)
    for r, start_c, end_c in runs:
        if end_c - start_c + 1 >= 2:
            for c in range(start_c, end_c + 1):
                output_grid[r][c] = 8

    # 3. Handle single-pixel runs adjacent to changed pixels
    for r, start_c, end_c in runs:
      if end_c - start_c + 1 == 1:
        changed = False
        if start_c > 0 and output_grid[r][start_c - 1] == 8:
          output_grid[r][start_c] = 8
          changed = True
        if end_c < cols - 1 and output_grid[r][end_c+1] == 8 and not changed:
          output_grid[r][end_c] = 8

    return output_grid