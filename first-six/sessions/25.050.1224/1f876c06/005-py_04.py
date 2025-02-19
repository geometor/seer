"""
The transformation rule takes each isolated colored cell (not white) in the input grid and extends it diagonally (down and to the right). The length of the diagonal depends on the row index of the original cell.  If the cell is in rows 0-4, the diagonal extends for a total of five cells (including the original cell).  If the cell is in rows 5-9, the diagonal extends until the bottom-right edge of the grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each cell of the input grid
    for i in range(rows):
        for j in range(cols):
            # Check if the cell is not white (0)
            if input_grid[i, j] != 0:
                # Extend diagonally based on row index
                if i < 5:
                    length = 5
                else:
                    length = rows - i
                
                # Draw the diagonal line
                for k in range(length):
                    if i + k < rows and j + k < cols:
                        output_grid[i + k, j + k] = input_grid[i, j]

    return output_grid