"""
The output grid has the same dimensions as the input grid.
If the input grid has an odd number of rows, all cells at and below the middle row in the output grid become gray (value 5).
All other cells become white (value 0). If the input grid has an even number of rows, the behavior is undefined, but for now all become white.
"""

import numpy as np

def transform(input_grid):
    # Create an output grid with the same dimensions as the input, filled with zeros (white).
    output_grid = np.zeros_like(input_grid)
    
    # Get the number of rows in the grid.
    rows = input_grid.shape[0]
    
    # Calculate the index of the middle row.
    middle_row_index = rows // 2

    # Iterate through each cell of the input grid.
    for i in range(rows):
        for j in range(input_grid.shape[1]):
            # Check if the number of rows is odd.
            if rows % 2 != 0:
                # Check if the current row is at or below the middle row.
                if i >= middle_row_index:
                    # Set the corresponding cell in the output grid to 5 (gray).
                    output_grid[i, j] = 5
            # else leave as zero (white)
            
    return output_grid