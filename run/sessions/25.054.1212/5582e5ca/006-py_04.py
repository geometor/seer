"""
1. Determine Output Dimensions: The output grid has the same dimensions (height and width) as the input grid.
2. Identify the Fill Color: Find the color value of the pixel located in the top-left corner (row 0, column 0) of the *input* grid.
3. Fill Output Grid: Create a new grid with the dimensions determined in step 1, and fill every cell of the output grid with the color identified in step 2.
"""

import numpy as np

def transform(input_grid):
    # Get the dimensions of the input grid.
    rows, cols = input_grid.shape

    # Get the color of the top-left pixel.
    fill_color = input_grid[0, 0]

    # Create an output grid filled with the identified color.
    output_grid = np.full((rows, cols), fill_color)

    return output_grid