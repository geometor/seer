"""
Collect all non-zero elements from the input grid and place them in order, starting from the last row of the output grid and filling upwards. Maintain right-alignment. The output grid is the same size as the input.
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid of the same size, filled with zeros.
    output_grid = np.zeros_like(input_grid)
    
    # Extract non-zero elements, preserving order.
    non_zero_elements = input_grid[input_grid != 0]
    
    # Get grid width and number of non-zero elements.
    grid_width = input_grid.shape[1]
    num_elements = len(non_zero_elements)
    
    # Calculate starting row and column for placement.
    row = output_grid.shape[0] - 1
    col = 0
    
    # Iterate through the non-zero elements and place them in the output grid.
    for i in range(num_elements):
        output_grid[row, col] = non_zero_elements[i]
        col += 1
        if col == grid_width:
            col = 0
            row -= 1

    return output_grid