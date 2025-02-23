"""
The transformation rule is a simple color substitution. Each pixel's color in the input grid is replaced by a corresponding color in the output grid according to the following mapping:

1.  Gray (5) is replaced by Blue (1).
2.  Azure (8) is replaced by Maroon (9).
3.  Magenta (6) is replaced by Red (2).

The grid dimensions (3x3) remain unchanged. Every instance of a particular color in the input is replaced by its mapped color in the output.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid by applying a color substitution mapping."""
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Define the color mapping.
    color_map = {
        5: 1,  # Gray to Blue
        8: 9,  # Azure to Maroon
        6: 2   # Magenta to Red
    }

    # Iterate through the input grid and apply the color mapping.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] in color_map:
                output_grid[i, j] = color_map[output_grid[i, j]]

    return output_grid