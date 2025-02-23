"""
The transformation rule is to simplify the input grid into a single row output grid.
The output grid contains one pixel of each unique color present in the input grid.
The order of colors in the output grid corresponds to the horizontal order from left to right in the input grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms an input grid into a single-row output grid, preserving one pixel
    of each unique color and their original order, encountered from left to right.
    """
    # Find unique colors in the input grid
    unique_colors = np.unique(input_grid)

    # Initialize the output grid with a width equal to the number of unique colors
    output_grid = np.zeros((1, len(unique_colors)), dtype=int)
    
    # Fill the output grid with one pixel of each unique color
    output_grid[0, :] = unique_colors[:]

    return output_grid