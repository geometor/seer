"""
Transforms the input grid by extracting a specific sub-region based on the input grid's characteristics.
The sub-region's size and location vary:
- 2x2 central sub-region for grids with a central "focus".
- 1x1 top-left pixel for grids with alternating colors.
- 2x1 central sub-region for grids with repeating patterns.
"""

import numpy as np

def get_dimensions(input_grid):
    """
    Determines the output dimensions based on input characteristics.
    """
    rows, cols = len(input_grid), len(input_grid[0])
    unique_colors = np.unique(input_grid)

    # Check for alternating colors (like example 2)
    is_alternating = True
    for r in range(rows):
        for c in range(cols):
            if r + 1 < rows and input_grid[r][c] == input_grid[r+1][c]:
                is_alternating = False
                break
            if c + 1 < cols and input_grid[r][c] == input_grid[r][c+1]:
                is_alternating = False
                break
        if not is_alternating:
            break
    if is_alternating and len(unique_colors) > 1:
        return 1, 1

    # check for 2x1 pattern, like in example 1
    has_2x1_pattern = False
    if rows > 1 and cols > 1:  # need min 2x2
        first_two_rows_str = str(input_grid[0][0:2])
        if first_two_rows_str.count(str(input_grid[0][0])) == 1:   # make sure colors are different
          all_match = True
          for r in range(0,rows, 2):
            for c in range(0, cols, 2):
              if r+1 >= rows or c+1 >= cols:
                continue
              if str(input_grid[r][c:c+2]) != first_two_rows_str:
                all_match = False
                break
            if not all_match:
              break
          if all_match:
            has_2x1_pattern = True
            return 2, 1

    # default, use 2x2, for example 3
    return 2, 2

def get_key_region(input_grid, out_rows, out_cols):
    """
    Extracts the key region from the input grid.
    """
    in_rows, in_cols = len(input_grid), len(input_grid[0])

    if out_rows == 1 and out_cols == 1:
        return [[input_grid[0][0]]]
    elif out_rows == 2 and out_cols == 1:
        start_row = (in_rows - 2) // 2
        start_col = (in_cols - 1) // 2
        return [
            [input_grid[start_row][start_col]],
            [input_grid[start_row + 1][start_col]]
            ]
    else:  # 2x2
        start_row = (in_rows - 2) // 2
        start_col = (in_cols - 2) // 2
        return [
            [input_grid[start_row][start_col], input_grid[start_row][start_col + 1]],
            [input_grid[start_row + 1][start_col], input_grid[start_row + 1][start_col + 1]],
        ]

def transform(input_grid):
    """
    Transforms the input grid based on identified characteristics.
    """
    # Determine output dimensions.
    out_rows, out_cols = get_dimensions(input_grid)

    # Extract the key region.
    output_grid = get_key_region(input_grid, out_rows, out_cols)

    return output_grid