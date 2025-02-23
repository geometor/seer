"""
The input grid appears to be expanded, but with the cells rotated and interlocked. The transformation
does *not* appear to be straightforward rotation or mirroring. The transformation uses a more complex
method of interlocking and repeating patterns.
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid with double the dimensions.
    input_height, input_width = input_grid.shape
    output_height = 2 * input_height
    output_width = 2 * input_width
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Iterate through input grid and perform interlocking expansion.
    for i in range(input_height):
        for j in range(input_width):
            color = input_grid[i, j]
            # Map each input pixel to a 2x2 block in output, interlocking.
            output_grid[ (i+j)%output_height, (i-j)%output_width] = color
            output_grid[ (i+j+1)%output_height, (i-j)%output_width] = color
            output_grid[ (i+j)%output_height, (i-j+1)%output_width] = color
            output_grid[ (i+j+1)%output_height, (i-j+1)%output_width] = color

    return output_grid