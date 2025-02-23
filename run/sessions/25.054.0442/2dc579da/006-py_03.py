"""
Extracts the top-left object from the input grid, stopping at the first major discontinuity in color or pattern.
The object starts at the top-left.  The boundary occurs when there's a horizontal or vertical solid color change or pattern change
"""

import numpy as np

def find_boundary(grid):
    """
    Finds the boundary of the top-left object.

    Args:
        grid (numpy.ndarray): The input grid.

    Returns:
        tuple: (row_end, col_end), the indices (exclusive) of the object's boundary.
    """
    rows, cols = grid.shape
    row_end = rows
    col_end = cols

    # Find initial pattern in the first row and column.
    initial_row_pattern = grid[0, :].tolist()
    initial_col_pattern = grid[:, 0].tolist()
    
    # Find horizontal boundary.
    for r in range(1, rows):
        current_row_pattern = grid[r, :col_end].tolist()
        # Check for a change solid color.
        unique_colors = np.unique(grid[r,:])
        if len(unique_colors) == 1 and unique_colors[0] != grid[0,0]:
          row_end = r
          break
        # Check for pattern shift (compare against the first row).
        if current_row_pattern[:col_end] != initial_row_pattern[:col_end]:
            row_end = r
            break

    # Find vertical boundary
    for c in range(1, cols):
      current_col_pattern = grid[:row_end, c].tolist()
      # Check for solid color change
      unique_colors = np.unique(grid[:,c])
      if len(unique_colors) == 1 and unique_colors[0] != grid[0,0]:
          col_end = c
          break

      # Check for a pattern shift
      if current_col_pattern[:row_end] != initial_col_pattern[:row_end]:
        col_end = c
        break


    return row_end, col_end

def transform(input_grid):
    """
    Extracts the top-left object of the input grid, stopping at the first discontinuity.

    Args:
        input_grid (numpy.ndarray): The input grid.

    Returns:
        numpy.ndarray: The extracted subgrid.
    """
    # Find the boundary of the top-left object.
    row_end, col_end = find_boundary(input_grid)

    # Extract the subgrid.
    output_grid = input_grid[:row_end, :col_end]

    return output_grid