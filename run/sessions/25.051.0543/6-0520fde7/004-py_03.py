"""
The program copies the input grid to the output, and changes to color 7 the color of the center of the object of color 3.
"""

import numpy as np

def transform(input_grid):
    # Create a copy of the input grid to serve as the output grid
    output_grid = np.copy(input_grid)

    # Find the positions of the green (color 3) object
    green_positions = np.argwhere(input_grid == 3)

    # Calculate the center of the green object
    center_y = np.mean(green_positions[:, 0]).astype(int)
    center_x = np.mean(green_positions[:, 1]).astype(int)
    
    # Change the color of the center position to 7 (orange)
    output_grid[center_y, center_x] = 7

    return output_grid