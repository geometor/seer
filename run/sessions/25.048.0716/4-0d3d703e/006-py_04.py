"""
The transformation rule is a color substitution based on the following mapping:

- 5 (Gray)    -> 1 (Blue)
- 8 (Azure)   -> 9 (Maroon)
- 6 (Magenta) -> 2 (Red)

The grid structure (dimensions and object shapes) is preserved. The
transformation acts uniformly on all cells of a given color.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a color substitution:
    5 -> 1, 8 -> 9, 6 -> 2.
    """
    # Create a copy of the input grid to serve as the output grid.
    output_grid = np.copy(input_grid)

    # Apply the color transformations using boolean indexing.
    output_grid[input_grid == 5] = 1  # Gray to Blue
    output_grid[input_grid == 8] = 9  # Azure to Maroon
    output_grid[input_grid == 6] = 2  # Magenta to Red

    return output_grid