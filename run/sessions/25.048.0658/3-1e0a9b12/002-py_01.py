"""
Collect all non-background colored cells.
Move all of them to the last row.
Preserve the relative order of appearance from left to right.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-zero colored cells to the last row,
    preserving their original left-to-right order.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Find all non-zero (non-background) elements and their coordinates
    non_zero_elements = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                non_zero_elements.append((input_grid[r, c], c))

    # Sort the non-zero elements based on their original column position (left-to-right)
    non_zero_elements.sort(key=lambda x: x[1])

    # Place the non-zero elements in the last row of the output grid
    last_row_index = 0
    for value, _ in non_zero_elements:
        output_grid[rows - 1, last_row_index] = value
        last_row_index += 1
    
    # copy elements from the last row of input if background
    for c in range(cols):
        if input_grid[rows-1,c]!=0 and output_grid[rows-1,c]==0:
           for r in range(rows-1,-1,-1):
              if input_grid[r,c]!=0:
                output_grid[rows-1,c]=input_grid[r,c]
                break
                

    return output_grid.tolist()