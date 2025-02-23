"""
1.  **Copy:** Copy all rows from the input grid to the output grid, except the first row and the last.
2.  **Combine and Sort for Last Row:** Gather all non-zero pixels from the entire input grid.  Sort these pixels in ascending order.
3.  **Place in Last Row:** Place the sorted non-zero pixels into the last row of the output grid, starting from the leftmost position.
4.  **Clear First Row:** The first row of the output is all zeros.
"""
import numpy as np

def transform(input_grid):
    # Create output with zeros, same dimensions as input
    output_grid = np.zeros_like(input_grid)

    # Copy all rows except the first and last
    for i in range(1, input_grid.shape[0] -1):
        output_grid[i] = input_grid[i]
    
    # Gather all non-zero pixels
    non_zero_pixels = []
    for row_index, row in enumerate(input_grid):
        for col_index, value in enumerate(row):
            if value != 0:
                non_zero_pixels.append(value)
                
    # Sort them
    non_zero_pixels.sort()

    # put them in the last row
    last_row = output_grid.shape[0] - 1
    for col_index, value in enumerate(non_zero_pixels):
        output_grid[last_row, col_index] = value
        
    return output_grid