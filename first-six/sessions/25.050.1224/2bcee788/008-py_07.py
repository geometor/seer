"""
The transformation involves two main actions. First, all the cells with value `2` have been replaced by value `4`, effectively combining all shapes into a single yellow cross shape. Then, the entire background, which was originally white (color 0), is changed to green (color 3). The yellow shape remains unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    output_grid = np.copy(input_grid)

    # Replace all instances of color 2 with color 4.
    output_grid[output_grid == 2] = 4

    # Create a new grid filled with color 3 (green).
    new_output_grid = np.full(input_grid.shape, 3)

    # Copy the yellow (color 4) object from output_grid to new_output_grid
    new_output_grid[output_grid == 4] = 4

    return new_output_grid