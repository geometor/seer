"""
The program takes a 3x3 grid of integers as input. Each integer in the input grid is transformed to a new integer based on a fixed mapping. The mapping is not a simple increment but a specific re-assignment of values: 1 becomes 5, 2 becomes 6, 3 becomes 4, 4 becomes 3, 5 becomes 1, 6 becomes 2, 8 becomes 9, and 9 becomes 8.  The spatial position of the integers within the grid does not change. The transformed integers form the output 3x3 grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms a 3x3 grid by mapping input values to output values.
    """
    # Initialize the output grid with the same dimensions as the input.
    output_grid = np.zeros_like(input_grid)

    # Define the mapping.  This is NOT a simple increment.
    mapping = {
        1: 5,
        2: 6,
        3: 4,
        4: 3,
        5: 1,
        6: 2,
        8: 9,
        9: 8,
    }

    # Iterate through each cell in the input grid.
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Map the input value to its corresponding output value.
            input_value = input_grid[i, j]
            output_grid[i, j] = mapping.get(input_value, input_value) # Keep original if no mapping

    return output_grid