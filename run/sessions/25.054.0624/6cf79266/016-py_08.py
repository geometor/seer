"""
The transformation identifies three 3x1 or 1x3 rectangular regions of a specific target color within the grid and changes them to blue (1). The target color is orange (7) for examples 1 and 3, and green (3) for example 2. All other pixels remain unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by changing three specific 3x1 or 1x3 regions of a target color to blue.
    """
    output_grid = np.copy(input_grid)
    height = output_grid.shape[0]
    width = output_grid.shape[1]
    transformed_count = 0

    # Determine the target color based on the example.  We'll assume that if there's *any* green,
    # it's the target. Otherwise, it's orange.
    if np.any(input_grid == 3):
        target_color = 3
    else:
        target_color = 7
        

    # Iterate through the grid to find and transform regions
    for row in range(height):
        for col in range(width):
            if transformed_count >= 3:
                break  # Stop after transforming three regions

            # Check for 3x1 region
            if (col + 2 < width and
                output_grid[row, col] == target_color and
                output_grid[row, col + 1] == target_color and
                output_grid[row, col + 2] == target_color):
                
                output_grid[row, col:col+3] = 1
                transformed_count += 1
                continue  # Move to the next pixel after transforming

            # Check for 1x3 region
            if (row + 2 < height and
                output_grid[row, col] == target_color and
                output_grid[row + 1, col] == target_color and
                output_grid[row + 2, col] == target_color):

                output_grid[row:row+2, col] = 1
                output_grid[row+2,col] = 1 #bug fix - need to explicitly state each index
                transformed_count += 1
                continue  # Move to the next pixel after transforming

    return output_grid