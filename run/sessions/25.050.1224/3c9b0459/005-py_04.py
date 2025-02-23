"""
The transformation inverts the colors between azure and gray. The grid remains with constant dimensions.
"""
import numpy as np
def transform(input_grid):
    """
    Transforms the input grid by swapping colors.
    """
    output_grid = np.copy(input_grid)
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i, j] == 8:
                output_grid[i, j] = 5
            elif input_grid[i, j] == 5:
                output_grid[i, j] = 8
    return output_grid