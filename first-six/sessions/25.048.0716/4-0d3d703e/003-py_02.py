"""
The transformation rule is a simple color substitution:
- Red (2) becomes Magenta (6)
- Green (3) becomes Yellow (4)
- Azure (8) becomes Maroon (9)
The grid structure and dimensions remain unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a color substitution:
    2 -> 6, 3 -> 4, 8 -> 9.
    """
    # Create a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Apply the color transformations.
    output_grid[input_grid == 2] = 6  # Change all reds (2) to magentas (6)
    output_grid[input_grid == 3] = 4  # Change all greens (3) to yellows (4)
    output_grid[input_grid == 8] = 9  # Change all azures (8) to maroons (9)

    return output_grid