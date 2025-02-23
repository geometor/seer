"""
Transforms a 3x3 input grid to a 3x3 output grid based on the following rules:

1. Uniform Input Grid: If all cells in the input grid have the same color, set all cells in the *first row* of the output grid to gray (5) and all other cells to white (0).
2. Main Diagonal Rule: If Step 1 does *not* apply, set all cells on the main diagonal (where row index equals column index) of the output grid to gray(5).
3. Other Cells: If a cell is not handled above, make white (0).
"""

import numpy as np

def _is_uniform(grid):
    """Checks if all cells in the grid have the same color."""
    first_color = grid[0, 0]
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] != first_color:
                return False
    return True

def _is_on_diagonal(row, col):
    """Checks if a cell is on the main diagonal."""
    return row == col

def transform(input_grid):
    # Initialize output_grid
    output_grid = np.zeros_like(input_grid)
    
    # Check for Uniform Input of Any Color
    if _is_uniform(input_grid):
        #Set first row to Gray, rest to White
        output_grid[0, :] = 5
        output_grid[1:, :] = 0
        return output_grid
    
    #Iterate Through Each cell
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Diagonal Transformation
            if _is_on_diagonal(i, j):
                output_grid[i, j] = 5 # Set to Gray
            # Other cells default to white.
            else:
                output_grid[i,j] = 0

    return output_grid