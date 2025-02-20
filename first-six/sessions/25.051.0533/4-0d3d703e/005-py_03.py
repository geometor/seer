"""
The input grid is composed of three horizontal lines, each characterized by the color sequence 5, 8, 6. The output grid maintains the same structure of three horizontal lines but exhibits a different color sequence, determined by a specific color mapping:

1.  Color 5 (gray) in the input is transformed to color 1 (blue) in the output.
2.  Color 8 (azure) in the input is transformed to color 9 (maroon) in the output.
3.  Color 6 (magenta) in the input is transformed to color 2 (red) in the output.

The transformation is purely a color substitution. The spatial attributes of the objects—the horizontal lines—remain consistent between the input and output grids. There are no changes in position, size, or shape; only the colors of the constituent elements are altered according to the defined mapping.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid to the output grid based on a color mapping.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Define the color mapping.
    color_map = {
        5: 1,  # gray -> blue
        8: 9,  # azure -> maroon
        6: 2   # magenta -> red
    }

    # Iterate through the input grid and apply the color mapping.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] in color_map:
                output_grid[i, j] = color_map[output_grid[i, j]]

    return output_grid