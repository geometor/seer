"""
The transformation rule is a color substitution based on the following mapping:

- 9 (Maroon)  -> 8 (Azure)
- 4 (Yellow)  -> 3 (Green)
- 2 (Red)     -> 6 (Magenta)

The grid structure (dimensions and object shapes) is preserved.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a color substitution:
    9 -> 8, 4 -> 3, 2 -> 6.
    """
    # Create a copy.
    output_grid = np.copy(input_grid)

    # Apply the color transformations.
    output_grid[input_grid == 9] = 8  # Maroon to Azure
    output_grid[input_grid == 4] = 3  # Yellow to Green
    output_grid[input_grid == 2] = 6  # Red to Magenta

    return output_grid