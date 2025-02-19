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
            if input_grid[i, j] == 9:
                output_grid[i, j] = 2
            elif input_grid[i, j] == 2:
                output_grid[i, j] = 9
            elif input_grid[i, j] == 4:
                output_grid[i, j] = 4
                
    return output_grid