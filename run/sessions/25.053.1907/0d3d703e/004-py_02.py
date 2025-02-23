"""
The transformation rule is a one-to-one color mapping. Every pixel in the input
grid is replaced by a corresponding, predefined color in the output grid. The
specific color mapping is as follows:

*   Blue (1) becomes Gray (5)
*   Red (2) becomes Magenta (6)
*   Green (3) becomes Yellow (4)
*   Yellow (4) becomes Green (3)
*   Gray (5) becomes Blue (1)
*   Magenta (6) becomes Red (2)
*   Azure (8) becomes Maroon (9)
*   Maroon (9) becomes Azure (8)
*   White (0) and Orange (7) remain unchanged.
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

    # change output pixels based on the complete mapping
    output_grid[input_grid == 1] = 5
    output_grid[input_grid == 2] = 6
    output_grid[input_grid == 3] = 4
    output_grid[input_grid == 4] = 3
    output_grid[input_grid == 5] = 1
    output_grid[input_grid == 6] = 2
    output_grid[input_grid == 8] = 9
    output_grid[input_grid == 9] = 8

    return output_grid