"""
The transformation rule identifies distinct colored regions in the input grid and represents each with a single cell in the output grid. The output is a Nx1 grid with cells ordered vertically by their color codes.
"""

import numpy as np

def get_distinct_colors(grid):
    """
    Returns a list of distinct colors present in the grid.
    """
    return np.unique(grid).tolist()

def transform(input_grid):
    """
    Transforms the input grid into a Nx1 grid representing the distinct colors in a specific vertical order.
    """
    # Get the distinct colors from the input grid
    distinct_colors = get_distinct_colors(input_grid)

    # Initialize the output grid as an empty list
    output_grid = []

    # Add each distinct color to the output grid list
    for color in distinct_colors:
        output_grid.append(color)

    # Reshape the output to Nx1 (where N is the number of distinct colors)
    return np.array(output_grid).reshape(-1, 1)