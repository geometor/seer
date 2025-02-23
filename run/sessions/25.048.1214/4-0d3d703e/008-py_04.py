"""
The transformation rule is a simple color mapping:
- Maroon (9) in the input becomes Azure (8) in the output.
- Yellow (4) in the input becomes Green (3) in the output.
- Red (2) in the input becomes Magenta (6) in the output.
The structure (vertical lines) is preserved.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by mapping colors according to the rule:
    9 -> 8, 4 -> 3, 2 -> 6.  Preserves spatial structure.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Apply the color transformation.
    output_grid[input_grid == 9] = 8
    output_grid[input_grid == 4] = 3
    output_grid[input_grid == 2] = 6

    return output_grid