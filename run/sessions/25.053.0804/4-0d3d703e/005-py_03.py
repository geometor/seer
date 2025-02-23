"""
The transformation rule involves subtracting a specific number from each cell, with the subtracted number dependent on the original cell value. Subtract 4 from cells with 5 (gray), subtract 9 from cell with 8, and subtract 4 from cell with 6. The operation appears to use a modulus 10 to manage cases that results in values below 0.
"""
import numpy as np

def transform(input_grid):
    # Create a copy of the input grid to modify
    output_grid = np.copy(input_grid)
    
    # Apply transformations using modulo arithmetic
    output_grid[input_grid == 5] = (output_grid[input_grid == 5] - 4) % 10  # 5 becomes 1
    output_grid[input_grid == 8] = (output_grid[input_grid == 8] - 9) % 10  # 8 becomes 9
    output_grid[input_grid == 6] = (output_grid[input_grid == 6] - 4) % 10  # 6 becomes 2

    return output_grid