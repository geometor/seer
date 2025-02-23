"""
The program performs a direct substitution of pixel values based on the following rules:

*   1 becomes 5
*   2 becomes 6
*   3 becomes 4
*   4 becomes 3
*   5 becomes 1
*   6 becomes 2
*   8 becomes 9
*   9 becomes 8

The structure (size and shape) of the grid remains unchanged. Only the values within the grid are altered according to this substitution cipher.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # change output pixels based on the complete substitution rules
    output_grid[input_grid == 1] = 5
    output_grid[input_grid == 2] = 6
    output_grid[input_grid == 3] = 4
    output_grid[input_grid == 4] = 3
    output_grid[input_grid == 5] = 1
    output_grid[input_grid == 6] = 2
    output_grid[input_grid == 8] = 9
    output_grid[input_grid == 9] = 8

    return output_grid