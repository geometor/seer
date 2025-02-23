"""
The input grid is expanded to create an output grid that is three times the height and two times the width of the input. Each pixel in the input grid is replicated in a 3x2 block in the output grid, maintaining the original color.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid based on expansion factors.
    input_height, input_width = input_grid.shape
    output_height, output_width = input_height * 3, input_width * 2
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Iterate through each cell of the input grid.
    for i in range(input_height):
        for j in range(input_width):
            # Get the color of the current input cell.
            color = input_grid[i, j]
            
            # Replicate the color in a 3x2 block in the output grid.
            for row_offset in range(3):
                for col_offset in range(2):
                    output_grid[i*3 + row_offset, j*2 + col_offset] = color

    return output_grid