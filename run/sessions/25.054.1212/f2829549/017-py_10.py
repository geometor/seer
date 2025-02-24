"""
Replace all orange, blue, and gray pixels with green pixels, leaving white pixels untouched. Combine all green pixels to form one object.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the rule."""

    # Create a copy of the input grid to modify.  We do *not* want to change the original.
    output_grid = input_grid.copy()

    # Replace all instances of colors 7, 1, and 5 with color 3.
    output_grid[output_grid == 7] = 3
    output_grid[output_grid == 1] = 3
    output_grid[output_grid == 5] = 3

    return output_grid