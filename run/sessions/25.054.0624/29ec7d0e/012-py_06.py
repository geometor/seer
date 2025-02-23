"""
The output grid retains the same dimensions as the input grid. Pixels with the color black (0) in the input remain black in the output. All other pixels in the input grid also remain unchanged. Therefore, Copy the input grid to the output grid, but only modify non-black pixels if they should be black according to some rule.  The rule appears to be that if a pixel is NOT black, and it is in a specific set of columns (the columns that contain black pixels), then it is changed to black in the output. If not black, and not one of these columns, it should remain unchanged.
"""

import numpy as np

def get_columns_with_black(grid):
    """
    Returns a set of column indices that contain at least one black (0) pixel.
    """
    black_columns = set()
    for col in range(grid.shape[1]):
        if 0 in grid[:, col]:
            black_columns.add(col)
    return black_columns

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.

    Args:
        input_grid: A 2D numpy array representing the input grid.

    Returns:
        A 2D numpy array representing the transformed output grid.
    """
    output_grid = input_grid.copy()  # Start with a copy
    black_cols = get_columns_with_black(input_grid)

    # Iterate through *all* cells, not just where errors were
    for row in range(output_grid.shape[0]):
        for col in range(output_grid.shape[1]):
            # if not black, check if the current column exists in black columns
            if output_grid[row, col] != 0 and col in black_cols:
                output_grid[row,col] = 0

    return output_grid