"""
1.  **Copy Rows with Changes:** Copy rows 2, 3, and 4 (index 1,2,3) from the input grid to rows 3,4, and 5(index 2,3,4) of the output grid, respectively.
2.  **Clear First Rows:** Set the first two rows of the output grid to all zeros.
3.  **Consolidate Non-Zero in Last Row:**  Gather all non-zero pixels from the *input* grid, maintain their original order, and place them in the last row of the output grid, starting from the leftmost position.
"""
import numpy as np

def transform(input_grid):
    # Initialize the output_grid
    output_grid = np.zeros_like(input_grid)
    
    # Copy rows
    output_grid[2] = input_grid[1]
    output_grid[3] = input_grid[2]
    output_grid[4] = input_grid[3]
    
    # Gather non-zero pixels maintaining their order
    non_zero_pixels = []
    for row_index, row in enumerate(input_grid):
        for col_index, value in enumerate(row):
            if value != 0:
                non_zero_pixels.append(value)
    
    # overwrite the last row we just copied with non-zero pixels            
    last_row_index = output_grid.shape[0] - 1
    for col_index, value in enumerate(non_zero_pixels):
        output_grid[last_row_index, col_index] = value
        
    return output_grid