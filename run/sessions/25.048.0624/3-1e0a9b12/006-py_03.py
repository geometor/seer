"""
Transformation Rule:

1. Identify all non-zero colored cells in the input grid.
2. Move these cells to the last available row of the output grid, except those in row 2.
3. Maintain the original column index of each cell during the move.
4. Copy row 2 from input to output.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-zero colored cells
    to the last available row, preserving their original column positions,
    and copying row 2 from the input grid to the output grid.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Find all non-zero cells and their column indices
    non_zero_cells = []
    for c in range(cols):
        for r in range(rows):
            if input_grid[r, c] != 0:
                non_zero_cells.append((r, c, input_grid[r, c]))

    # Create a dictionary to track the next available row for each column
    next_available_row = {col: rows - 1 for col in range(cols)}

    # Iterate through non-zero cells and place them in the output grid
    for r, c, value in non_zero_cells:
      if r != 2:
        output_grid[next_available_row[c], c] = value
        next_available_row[c] -= 1
      
    # Copy row 2
    output_grid[2,:] = input_grid[2,:]

    return output_grid.tolist()