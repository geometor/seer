"""
Identifies all azure (8) pixels in the input grid. Creates an output grid of
the same size, filled with grey (0) pixels. Copies the azure pixels from the
input to the output, maintaining their original positions. Sets all other
pixels in the output grid to grey (0).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by isolating azure pixels and setting all
    other pixels to grey.
    """
    # Initialize the output grid with all grey pixels.
    output_grid = np.zeros_like(input_grid)

    # Iterate through the input grid.
    height, width = input_grid.shape
    for y in range(height):
        for x in range(width):
            # If the pixel is azure, copy it to the output grid.
            if input_grid[y, x] == 8:
                output_grid[y, x] = 8

    return output_grid