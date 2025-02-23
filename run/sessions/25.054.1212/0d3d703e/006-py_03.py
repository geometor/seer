"""
The transformation is a one-to-one pixel value mapping. Each pixel in the input
grid is mapped to a corresponding pixel in the output grid based on its color
value.  The mapping, derived from careful observation of all provided input
and output grids, is:

0 -> 0
1 -> 5
2 -> 6
3 -> 4
4 -> 3
5 -> 5
6 -> 6
7 -> 7
8 -> 8
9 -> 9
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified mapping.
    """
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)

    # Create a mapping dictionary
    mapping = {
        0: 0,
        1: 5,
        2: 6,
        3: 4,
        4: 3,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
    }

    # Apply the mapping to each element of the grid
    for key, value in mapping.items():
        output_grid[input_grid == key] = value

    return output_grid