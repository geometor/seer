"""
The transformation adds mirrored "L" shapes above a boundary line in the input grid. The boundary is the line between rows of uniform color at the bottom and rows with multiple colors. The color of the "L" shapes is determined by the color of the cell immediately below the boundary. The "L" shapes are added in every possible position above the boundary.
"""

import numpy as np

def find_boundary_row(grid):
    """Finds the boundary row index."""
    rows, _ = grid.shape
    for i in range(rows - 1, -1, -1):
        if len(np.unique(grid[i])) > 1:
            return i + 1
    return 0

def get_shape_color(grid, row, col):
    """Gets the color for the 'L' shape based on the cell below the boundary."""
    rows, cols = grid.shape
    if row < rows:
        return grid[row, col]
    return 0  # Default color if no color is found below

def transform(input_grid):
    # Initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find the boundary row
    boundary_row = find_boundary_row(output_grid)

    # Add "L" shapes above the boundary
    for r in range(boundary_row - 1, -1, -1):
        for c in range(cols):
            if output_grid[r, c] == 0 and r+1 < rows :
                shape_color = get_shape_color(output_grid, r + 1, c)
                if shape_color != 0:
                   output_grid[r,c] = shape_color
                   if r-1 >= 0:
                    if c+1 < cols and output_grid[r, c+1] == 0 and output_grid[r-1, c+1] == 0:
                      output_grid[r-1,c+1] = shape_color
                    elif c-1 >=0 and output_grid[r, c-1] == 0 and output_grid[r-1, c-1] == 0:
                      output_grid[r-1, c-1] = shape_color
    return output_grid