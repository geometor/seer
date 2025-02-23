"""
The transformation rule involves inspecting the input integer value for each cell.

-   If the input is 1, it is transformed to 4. (+3)
-   If the input is 2, it is transformed to 6. (+4)
-   If the input is 3, it is transformed to 4. (+1)
"""

import numpy as np

def transform(input_grid):
    """
    Transforms an input grid based on a value-specific mapping.
    """
    # Initialize the output grid as a copy of the input grid.  Avoids in-place modification.
    output_grid = input_grid.copy()

    # Iterate through each cell of the input grid.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Apply the transformation based on the input value.
            if output_grid[i, j] == 1:
                output_grid[i, j] = 4
            elif output_grid[i, j] == 2:
                output_grid[i, j] = 6
            elif output_grid[i, j] == 3:
                output_grid[i, j] = 4
    return output_grid