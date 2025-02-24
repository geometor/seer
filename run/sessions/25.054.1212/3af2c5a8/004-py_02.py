"""
1. Double Dimensions: The output grid has double the height and double the width of the input grid.
2. Pixel Replication: For every pixel in the input grid, create a 2x2 block of pixels in the output grid.
3. Color Matching: The 2x2 block in the output grid has the same color as the corresponding pixel in the input grid. The top-left pixel of each 2x2 block has a direct mapping with input pixel.
4. Iteration order: The actions are performed by iterating each row, and then each column of the input grid, which corresponds to a top-left to bottom-right.
"""

import numpy as np

def transform(input_grid):
    # Double Dimensions: Get input dimensions and calculate output dimensions.
    input_height, input_width = input_grid.shape
    output_height = input_height * 2
    output_width = input_width * 2

    # Initialize Output Grid: Create an output grid filled with zeros.
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Pixel Replication and Color Matching: Iterate through input and create 2x2 blocks.
    for i in range(input_height):
        for j in range(input_width):
            # Get the color of the current input pixel.
            color = input_grid[i, j]

            # Create the 2x2 block in the output grid.
            output_grid[2*i:2*i+2, 2*j:2*j+2] = color

    return output_grid