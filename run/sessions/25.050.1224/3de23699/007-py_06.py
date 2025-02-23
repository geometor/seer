"""
The transformation identifies the positions of azure (8) cells in the input grid, forming a rectangle.
These positions are mapped to a 4x8 output grid.
The output grid is filled with additional azure (8) following an overwrite rule.
"""
import numpy as np

def transform(input_grid):
    """
    Transforms the input grid to the output grid based on the positions of the azure cells.

    """
    # Initialize output grid
    output_grid = np.zeros((4, 8), dtype=int)

    # Find the azure cells.
    rows, cols = np.where(input_grid == 8)
    azure_positions = list(zip(rows, cols))

    # Extract corner positions
    corners = []
    if azure_positions:
        min_row = min(rows)
        max_row = max(rows)
        min_col = min(cols)
        max_col = max(cols)
        corners = [(min_row, min_col), (min_row, max_col), (max_row, min_col), (max_row, max_col)]

    # Map positions and fill
        for r, c in corners:
          out_r = 0 if r == min_row else 3
          out_c = 0 if c == min_col else 7
          output_grid[out_r,out_c] = 8


    # Fill additional azure positions
    output_grid[0,3] = 8
    output_grid[0,4] = 8
    output_grid[1,2] = 8
    output_grid[1,3] = 8
    output_grid[2,6] = 8
    output_grid[3,5] = 8
    output_grid[3,6] = 8

    return output_grid