"""
The transformation rule is a simple color mapping:
- Gray (5) in the input becomes Blue (1) in the output.
- Azure (8) in the input becomes Maroon (9) in the output.
- Magenta (6) in the input becomes Red (2) in the output.
The structure (vertical lines) is preserved.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by mapping colors according to the rule:
    5 -> 1, 8 -> 9, 6 -> 2.  Preserves spatial structure.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Apply the color transformation.
    output_grid[input_grid == 5] = 1
    output_grid[input_grid == 8] = 9
    output_grid[input_grid == 6] = 2

    return output_grid