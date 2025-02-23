"""
The input is a grid of pixels. Find all blue (1) pixels and change their color to red (2). All other pixels retain their original colors. The grid structure and spatial arrangement of pixels remain unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by replacing all blue (1) pixels with red (2) pixels.

    Args:
        input_grid: A 2D numpy array representing the input grid.

    Returns:
        A 2D numpy array representing the output grid.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Find the coordinates of all blue (1) pixels.
    blue_pixels = np.where(output_grid == 1)

    # Change the color of the identified blue pixels to red (2).
    output_grid[blue_pixels] = 2

    return output_grid