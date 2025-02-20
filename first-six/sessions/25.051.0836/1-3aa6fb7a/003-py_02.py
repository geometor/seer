"""
For each azure pixel in the input image:
    If it is not neighbor with an azure pixel to the right and bottom, then
        Change its color to blue.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each cell of the input grid
    for i in range(rows):
        for j in range(cols):
            # Check if the current cell is azure (8)
            if input_grid[i, j] == 8:
                # Check neighbors (right and bottom)
                is_right_neighbor_azure = False
                is_bottom_neighbor_azure = False

                if j + 1 < cols:  #check the right neighbor
                    if input_grid[i,j+1] == 8:
                        is_right_neighbor_azure = True
                if i + 1 < rows:  #check the bottom neighbor
                    if input_grid[i+1,j] == 8:
                        is_bottom_neighbor_azure = True

                # Apply the transformation rule: change color to blue (1)
                if (not is_right_neighbor_azure) and (not is_bottom_neighbor_azure):
                    output_grid[i, j] = 1

    return output_grid