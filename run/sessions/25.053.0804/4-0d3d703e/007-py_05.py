"""
The transformation rule involves subtracting a number, which can be different depending on the original value of the cell. Specifically, subtract 1 from cells that are 9 (maroon), subtract 1 from cell that are 4 and subtract -4 from cells that are 2. Modulo 10 is needed if results are negative.
"""
import numpy as np

def transform(input_grid):
    # Create a copy of the input grid to modify
    output_grid = np.copy(input_grid)
    
    # Apply transformations using modulo arithmetic
    output_grid[input_grid == 9] = (output_grid[input_grid == 9] - 1) % 10  # 9 becomes 8
    output_grid[input_grid == 4] = (output_grid[input_grid == 4] - 1) % 10  # 4 becomes 3
    output_grid[input_grid == 2] = (output_grid[input_grid == 2] - -4) % 10  # 2 becomes 6

    return output_grid