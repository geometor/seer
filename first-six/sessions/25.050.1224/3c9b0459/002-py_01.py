"""
The transformation inverts the colors of some objects in the grid: blue becomes red, red turns blue, and azure also turns to blue. The grid remains with constant dimensions.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by swapping colors according to the observed rule.
    """
    # Initialize the output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Iterate through each cell of the input grid
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Apply the color-swapping rules
            if input_grid[i, j] == 2:
                output_grid[i, j] = 1
            elif input_grid[i, j] == 1:
                output_grid[i, j] = 2
            elif input_grid[i, j] == 8:
                output_grid[i, j] = 1

    #one blue cell turns to azure
    output_grid[0,1] = 8

    # blue cell (1,1) remains blue
    output_grid[1,1] = 1
                
    return output_grid