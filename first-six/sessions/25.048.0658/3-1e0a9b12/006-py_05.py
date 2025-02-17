"""
Copy all non-background colored cells from the input grid to the last row,
preserving their relative left-to-right order.
"""

import numpy as np

def find_non_background_cells(grid):
    """
    Finds all non-background (non-zero) cells in the grid.
    Returns a list of tuples: (row, col, value).
    """
    non_background_cells = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != 0:
                non_background_cells.append((r, c, grid[r][c]))
    return non_background_cells

def transform(input_grid):
    """
    Transforms the input grid by copying all non-zero colored cells to the last row,
    preserving their original left-to-right order.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Find all non-zero elements.
    non_zero_elements = find_non_background_cells(input_grid)

    # Sort non-zero elements by column then by row.
    non_zero_elements.sort(key=lambda x: (x[1], x[0]))


    # Place the sorted non-zero elements in the last row.
    last_row_index = 0
    for _, _, value in non_zero_elements:
        output_grid[rows - 1, last_row_index] = value
        last_row_index += 1
        
    # copy elements from the last row of input if background at that place
    for c in range(cols):
        if input_grid[rows-1,c]!=0 and output_grid[rows-1,c]==0:
           for r in range(rows-1,-1,-1):
              if input_grid[r,c]!=0:
                output_grid[rows-1,c]=input_grid[r,c]
                break

    return output_grid.tolist()