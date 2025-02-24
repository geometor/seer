"""
1. Double Dimensions: The output grid's height and width are each twice the corresponding dimensions of the input grid.
2. Pixel Replication: Each pixel in the input grid is represented by a 2x2 block of pixels in the output grid.
3. Color Preservation: The color of the 2x2 block in the output grid matches the color of the corresponding pixel in the input grid.
4. Block Placement: The top-left pixel of each 2x2 output block corresponds to the `[row * 2, column * 2]` position in the output grid, if `row` and `column` are the coordinates in the input grid. The whole block should match the original input pixel.
5. Iteration: The process is applied systematically, moving across each row of the input from left to right and then down the rows (top to bottom).
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

            # Create the 2x2 block in the output grid, correctly positioned.
            output_grid[i*2, j*2] = color         # Top-left
            output_grid[i*2 + 1, j*2] = color     # Bottom-left
            output_grid[i*2, j*2 + 1] = color     # Top-right
            output_grid[i*2 + 1, j*2 + 1] = color # Bottom-right

    return output_grid