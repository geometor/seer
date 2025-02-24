"""
The transformation rule takes a 3x3 input grid and expands it into a 6x6 output grid. Each pixel in the input grid is replicated as a 2x2 block of the same color in the output grid.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_height, input_width = input_grid.shape
    output_height, output_width = input_height * 2, input_width * 2
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # change output pixels 
    for i in range(input_height):
        for j in range(input_width):
            # Get the color of the current pixel
            color = input_grid[i, j]
            
            # Replicate the pixel to a 2x2 block in output_grid
            output_grid[2*i:2*i+2, 2*j:2*j+2] = color

    return output_grid