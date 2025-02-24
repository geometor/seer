"""
Transforms an input grid by identifying a vertical orange line and creating a checkerboard pattern of orange and azure above it, extending to the edges of the grid. The checkerboard starts one row above the orange line and ends one row above where the orange line ends. The area below the orange line remains unchanged.
"""

import numpy as np

def find_orange_line(grid):
    """Finds the vertical orange line in the grid."""
    rows, cols = grid.shape
    for j in range(cols):
        for i in range(rows):
            if grid[i, j] == 7:
                # Found start of potential line
                start_row = i
                end_row = i
                while end_row + 1 < rows and grid[end_row + 1, j] == 7:
                    end_row += 1
                return start_row, end_row, j
    return None, None, None

def create_checkerboard(grid, top_row, bottom_row, cols):
    """Creates the checkerboard pattern."""
    output_grid = np.copy(grid)
    for i in range(top_row, bottom_row):
        for j in range(cols):
           if (i + j) % 2 == 0:
              output_grid[i,j] = 7
           else:
              output_grid[i,j] = 8
    return output_grid

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    # Find the orange line
    start_row, end_row, col = find_orange_line(input_grid)

    if start_row is None:  # No orange line found
        return np.copy(input_grid)

    # Define checkerboard boundaries
    top_row = max(0, start_row - 1)  # One row above start, but not negative
    bottom_row = end_row # One row above the end of line
    rows, cols = input_grid.shape

    # Create checkerboard pattern
    output_grid = create_checkerboard(input_grid, top_row, bottom_row, cols)

    return output_grid