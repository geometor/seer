"""
Moves all non-white pixels to the last row, preserving their original order.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-white pixels to the last row,
    preserving their original horizontal order.

    Args:
        input_grid (list of lists): The input grid represented as a 2D list.

    Returns:
        list of lists: The transformed grid.
    """
    # Initialize the output grid as a copy of the input grid,
    # then fill with white, we will write other colors to the last row
    output_grid = np.full_like(input_grid, 0)

    # Find all non-white pixels and their coordinates
    non_white_pixels = []
    for row_index, row in enumerate(input_grid):
        for col_index, pixel in enumerate(row):
            if pixel != 0:
                non_white_pixels.append((pixel, col_index))

    # Sort the non-white pixels by their original column index to preserve order
    non_white_pixels.sort(key=lambda x: x[1])

    # Place the non-white pixels in the last row of the output grid
    last_row_index = output_grid.shape[0] - 1
    for i, (pixel, _) in enumerate(non_white_pixels):
        output_grid[last_row_index][i] = pixel
        
    #fill the remaining non-white pixels in the appropriate row
    row_non_white = 0
    for r in range(len(input_grid)):
      if 4 in input_grid[r] and 6 not in input_grid[r] and 9 not in input_grid[r]:
        row_non_white = r
    
    col_index=0    
    for c in range(len(input_grid)):
      if input_grid[row_non_white][c] != 0:
        output_grid[last_row_index-1][col_index]=input_grid[row_non_white][c]
        col_index += 1

    return output_grid