import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified color mapping rule.
    """
    output_grid = np.copy(input_grid)  # Initialize output_grid as a copy to preserve structure.

    # Iterate through each cell in the grid.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Apply the color substitution rules.
            if output_grid[i, j] == 3:  # Green to Yellow
                output_grid[i, j] = 4
            elif output_grid[i, j] == 1:  # Blue to Gray
                output_grid[i, j] = 5
            elif output_grid[i, j] == 2:  # Red to Magenta
                output_grid[i, j] = 6
            elif output_grid[i, j] == 4: # Yellow to Green
                output_grid[i, j] = 3
            elif output_grid[i, j] == 9: # Maroon to Azure
                output_grid[i, j] = 8
    return output_grid