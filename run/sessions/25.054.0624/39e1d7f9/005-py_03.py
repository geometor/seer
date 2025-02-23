"""
1.  **Identify Objects:** Find all contiguous vertical columns of color green (3), magenta (6) and azure (8).
2.  **Define Quadrants:** Divide the input grid conceptually into four quadrants: top-left, top-right, bottom-left, and bottom-right. The boundaries of these quadrants are determined by the smallest rectangular area enclosing all azure(8) columns.
3. **Conditional color Swap:** the green and magenta vertical columns should be swapped, but only in the lower right quadrant.
4.  **Output:** Generate the modified grid with the colors swapped in the specified region.
"""

import numpy as np

def find_vertical_columns(grid, color):
    """Finds contiguous vertical columns of a specified color."""
    columns = []
    rows, cols = grid.shape
    for j in range(cols):
        current_column = []
        for i in range(rows):
            if grid[i, j] == color:
                current_column.append((i, j))
            elif current_column:
                columns.append(current_column)
                current_column = []
        if current_column:  # Handle columns that extend to the bottom edge
            columns.append(current_column)
    return columns

def define_quadrants(grid, azure_columns):
    """Defines quadrant boundaries based on azure columns."""
    if not azure_columns: # if no azure columns, return None
      return None

    # Get all row and col coordinates of the azure columns
    azure_rows = sorted(list(set([r for col in azure_columns for r, _ in col])))
    azure_cols = sorted(list(set([c for col in azure_columns for _, c in col])))

    # get min/max to find bounding box, use this for the quadrants
    min_row, max_row = azure_rows[0], azure_rows[-1]
    min_col, max_col = azure_cols[0], azure_cols[-1]

    quadrants = {
        "top-left": (0, min_row, 0, min_col),  # (row_start, row_end, col_start, col_end)
        "top-right": (0, min_row, max_col + 1, grid.shape[1]),
        "bottom-left": (max_row + 1, grid.shape[0], 0, min_col),
        "bottom-right": (max_row + 1, grid.shape[0], max_col + 1, grid.shape[1]),
    }
    return quadrants

def is_in_quadrant(position, quadrant):
    """Checks if a position is within a given quadrant."""
    r, c = position
    row_start, row_end, col_start, col_end = quadrant
    return row_start <= r < row_end and col_start <= c < col_end

def transform(input_grid):
    # initialize output_grid
    output_grid = input_grid.copy()
    
    # find vertical columns
    green_columns = find_vertical_columns(input_grid, 3)
    magenta_columns = find_vertical_columns(input_grid, 6)
    azure_columns = find_vertical_columns(input_grid, 8)
    
    # define quadrant boundaries
    quadrants = define_quadrants(input_grid, azure_columns)
    if not quadrants:
      return output_grid

    # swap colors in lower right
    bottom_right = quadrants["bottom-right"]
    for col in green_columns:
        if all(is_in_quadrant(pos, bottom_right) for pos in col):
            for r, c in col:
                output_grid[r, c] = 6
    for col in magenta_columns:
        if all(is_in_quadrant(pos, bottom_right) for pos in col):
            for r, c in col:
                output_grid[r, c] = 3

    return output_grid