"""
The transformation rule is a simple color substitution. Each color in the input grid is replaced by a corresponding color in the output grid, according to the following mapping:

1.  Gray (5) is replaced with Blue (1).
2.  Azure (8) is replaced with Maroon (9).
3.  Magenta (6) is replaced with Red (2).

The spatial arrangement of pixels remains unchanged; only the color values are altered based on this direct mapping.
"""

import numpy as np

def transform(input_grid):
    """Applies a color substitution to the input grid."""
    # Initialize the output grid with the same dimensions as the input.
    output_grid = np.copy(input_grid)

    # Define the color mapping.
    color_map = {
        5: 1,  # Gray to Blue
        8: 9,  # Azure to Maroon
        6: 2   # Magenta to Red
    }

    # Iterate through the input grid and apply the color mapping.
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            output_grid[i, j] = color_map.get(input_grid[i, j], input_grid[i,j]) #use .get() and return original if not in map

    return output_grid