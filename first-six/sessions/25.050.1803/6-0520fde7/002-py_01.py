"""
The transformation process begins by examining the input grid for a specific pattern: a column where all cells are of color gray (color 5). If such a column is found anywhere in the input grid, the transformation rule is triggered. This rule dictates the generation of a fixed 3x3 output grid. In this output grid, the central cell (at row index 1, column index 1, using zero-based indexing) is set to red (color 2), and all other cells within this 3x3 grid are set to white (color 0). The presence of the gray column in the input grid serves as a condition to initiate this transformation, but its position or any other attributes do not further influence the resultant 3x3 output grid, which always remains the same once triggered.
"""

import numpy as np

def has_gray_column(grid):
    """
    Checks if the grid has a column where all cells are gray (color 5).
    """
    for j in range(grid.shape[1]):
        if all(grid[:, j] == 5):
            return True
    return False

def transform(input_grid):
    """
    Transforms the input grid based on the presence of a gray column.
    """
    input_grid = np.array(input_grid)

    # Check for the existence of a gray column
    if has_gray_column(input_grid):
        # Create a 3x3 grid filled with white (color 0)
        output_grid = np.zeros((3, 3), dtype=int)
        # Set the center cell to red (color 2)
        output_grid[1, 1] = 2
        return output_grid.tolist()  # Convert back to list for consistency with ARC
    else:
      return input_grid.tolist()