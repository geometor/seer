"""
Moves all non-zero single-cell objects to the last row of the grid,
maintaining their relative horizontal order. Single-cell objects are those
that have no adjacent cells (horizontally, vertically, or diagonally) with the
same color. Multi-cell objects already in the last row occupy their positions.
"""

import numpy as np

def is_single_cell(grid, r, c):
    """Checks if a cell is a single-cell object (no neighbors of same color)."""
    rows = len(grid)
    cols = len(grid[0])
    color = grid[r][c]
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= r + i < rows and 0 <= c + j < cols:
                if (i != 0 or j != 0) and grid[r + i][c + j] == color:
                    return False
    return True

def transform(input_grid):
    """
    Transforms the input grid by moving non-zero single-cell objects to the last row,
    maintaining their relative horizontal order.

    Args:
        input_grid (list of lists): The input grid.

    Returns:
        list of lists: The transformed output grid.
    """
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = [row[:] for row in input_grid]  # Deep copy of the input grid
    last_row = [0] * cols

    # Occupy spaces in last row by multi-cell objects present in the last row
    for c in range(cols):
      if input_grid[rows-1][c] != 0:
        if not is_single_cell(input_grid, rows-1, c):
          last_row[c] = input_grid[rows-1][c]


    # Find and move single-cell non-zero objects
    for c in range(cols):
        for r in range(rows):
            if input_grid[r][c] != 0:
                # Check if it's a single-cell object
                if is_single_cell(input_grid, r, c):
                    # If it's a single-cell object, move it to last row if space available
                    if last_row[c] == 0:
                      last_row[c] = input_grid[r][c]
                      # Clear original position only if it wasn't already in the last row
                      if r != rows -1:
                        output_grid[r][c] = 0

    # Replace the last row of the output grid with the processed last row
    output_grid[rows - 1] = last_row

    return output_grid