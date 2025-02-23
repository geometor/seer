"""
1. Iterate through each column of the input grid.
2. Within each column, collect all non-zero values.
3. Maintain the original vertical order (top to bottom) of these non-zero values within the column.
4. Place these collected values in the *same* column of the output grid, starting from the top-most available row and stacking them downwards. Available row means empty (value 0).
5. If a non-zero value is encountered in input that already exist in the output and has empty cell in input, place the value to top-most available row
6. Fill any remaining cells in the output grid with zeros.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the refined rule."""

    output_grid = np.zeros_like(input_grid)
    rows, cols = output_grid.shape

    for j in range(cols):  # Iterate through columns
        column_values = []
        for i in range(rows):
            if input_grid[i, j] != 0:
                column_values.append((input_grid[i, j],i))

        # Place values in the same column, stacking downwards
        row_idx = 0
        
        for val, original_row in column_values:
            while row_idx < rows and output_grid[row_idx, j] != 0:
                row_idx += 1
            if row_idx < rows:
              output_grid[row_idx, j] = val
              row_idx +=1

    return output_grid