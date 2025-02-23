"""
The transformation rule is a simple mapping:
- 1 (blue) becomes 5 (gray)
- 2 (red) becomes 6 (magenta)
- 3 (green) becomes 4 (yellow)
"""

import numpy as np

def transform(input_grid):
    """
    Transforms a grid of integers according to a predefined mapping.
    
    Args:
        input_grid (numpy.ndarray): A 2D numpy array representing the input grid.

    Returns:
        numpy.ndarray: A 2D numpy array representing the transformed output grid.
    """
    # initialize output_grid as a copy of the input grid
    output_grid = input_grid.copy()

    # change output pixels based on the mapping
    output_grid[input_grid == 1] = 5  # Replace 1s with 5s
    output_grid[input_grid == 2] = 6  # Replace 2s with 6s
    output_grid[input_grid == 3] = 4  # Replace 3s with 4s

    return output_grid