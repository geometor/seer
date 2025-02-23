"""
Preserves red (2) and azure (8) borders. Changes to green (3) the white pixels below the white pixel directly to the right of the Azure border.
Fills the rows below with green (3).
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
    min_azure_col = np.min(azure_cols)
    max_red_col = np.max(red_cols)

    # Find first vertical white line
    for c in range(min_azure_col+1, max_red_col):
        for r in range (min_red_row, max_azure_row):
            if output_grid[r, c] == 0:
                for inner_r in range(r, max_azure_row):
                    if output_grid[inner_r,c] != 2 and output_grid[inner_r,c] != 8:
                        output_grid[inner_r,c] = 3
                    else:
                        break
                break # Only the first one per column

    return output_grid