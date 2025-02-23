"""
Extracts a subgrid from the input grid, based on the location of a multi-colored region in the lower part of the grid. The size of subgrid may vary.
Some color modification might be applied to the extracted subgrid, by replacing some color to 0.
"""

import numpy as np

def find_target_region(input_grid):
    """
    Finds the bounding box of the multi-colored region (non-0 and non-1 pixels) at the bottom.
    """
    rows, cols = input_grid.shape
    non_zero_one_indices = np.argwhere((input_grid != 0) & (input_grid != 1))

    if len(non_zero_one_indices) == 0:
        return None, None, None, None

    min_row = np.min(non_zero_one_indices[:, 0])
    max_row = np.max(non_zero_one_indices[:, 0])
    min_col = np.min(non_zero_one_indices[:, 1])
    max_col = np.max(non_zero_one_indices[:, 1])

    return min_row, max_row, min_col, max_col

def transform(input_grid):
    """
    Transforms the input grid by extracting a subgrid and applying color transformations.
    """
    # Find the location of target region.
    min_row, max_row, min_col, max_col = find_target_region(input_grid)

    if min_row is None:
        return input_grid

    # Determine output dimensions based on the target region.
    output_rows = max_row - min_row + 1
    output_cols = max_col - min_col + 1
    output_grid = np.zeros((output_rows, output_cols), dtype=int)

    # Extract subgrid and apply color transformation.
    for i in range(output_rows):
        for j in range(output_cols):
            input_row = min_row + i
            input_col = min_col + j
            color = input_grid[input_row, input_col]
            
            # Color transformation: change colors other than 1, 7, 9 to 0.
            if color not in [1, 7, 9]:
                output_grid[i, j] = color

    return output_grid