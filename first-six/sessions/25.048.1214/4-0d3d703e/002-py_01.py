"""
The transformation rule is a simple color mapping:
- Green (3) in the input becomes Yellow (4) in the output.
- Blue (1) in the input becomes Gray (5) in the output.
- Red (2) in the input becomes Magenta (6) in the output.
The structure (vertical lines) is preserved.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by mapping colors according to the rule:
    3 -> 4, 1 -> 5, 2 -> 6.  Preserves spatial structure.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Apply the color transformation.
    output_grid[input_grid == 3] = 4
    output_grid[input_grid == 1] = 5
    output_grid[input_grid == 2] = 6

    return output_grid