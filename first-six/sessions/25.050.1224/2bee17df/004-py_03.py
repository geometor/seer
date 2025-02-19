"""
Preserves red (2) and azure (8) borders. Changes to green (3) two adjacent white pixels or the white pixels vertically aligned with the red frame.
Then fills the interior region bounded by the red, azure frames and two adjacent pixels with green (3).
"""

import numpy as np

def find_borders(grid, color):
    # Find the row and column indices where the border color exists.
    rows, cols = np.where(grid == color)
    return rows, cols

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find red (2) and azure (8) borders.
    red_rows, red_cols = find_borders(input_grid, 2)
    azure_rows, azure_cols = find_borders(input_grid, 8)

    # Determine the bounding box of the interior region.
    min_red_row = np.min(red_rows)
    max_azure_row = np.max(azure_rows)
    min_azure_col = np.min(azure_cols) if len(azure_cols) > 0 else 0
    max_red_col = np.max(red_cols)

    # Find and fill two adjacent pixels
    adjacent_filled = False
    for r in range(min_red_row, max_azure_row):
        for c in range (min_azure_col, max_red_col -1):
            if output_grid[r,c] == 0 and output_grid[r, c+1] == 0:
                output_grid[r,c] = 3
                output_grid[r,c+1] = 3
                adjacent_filled = True
        if adjacent_filled:
          break

    # Find first vertical white line if no adjacent were found
    if not adjacent_filled:
        for c in range(min_red_col, max_red_col):
          if output_grid[min_red_row + 1, c] == 0:
            for r in range(min_red_row + 1, max_azure_row):
                if output_grid[r,c] == 0:
                    output_grid[r,c] = 3
            break


    # Fill the interior with green (3) - second pass
    for r in range(min_red_row + 1, max_azure_row):
        for c in range(min_azure_col + 1 , max_red_col ):
             if output_grid[r, c] == 0:
                output_grid[r, c] = 3

    return output_grid