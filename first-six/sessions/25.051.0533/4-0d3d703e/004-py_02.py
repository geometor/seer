"""
The input grid consists of three horizontal lines, each displaying the color sequence 2, 3, 8.  The output grid mirrors this structure with three horizontal lines, but the colors are transformed according to a consistent mapping:

1.  Color 2 (red) in the input is replaced by color 6 (magenta) in the output.
2.  Color 3 (green) in the input is replaced by color 4 (yellow) in the output.
3.  Color 8 (azure) in the input is replaced by color 9 (maroon) in the output.

Similar to the previous example, the transformation involves only a color change. The spatial characteristics—positions, sizes, and shapes of the horizontal lines—are preserved. The operation is a straightforward color substitution based on the defined mapping. No geometric transformations are applied.
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
        2: 6,  # red -> magenta
        3: 4,  # green -> yellow
        8: 9   # azure -> maroon
    }

    # Iterate through the input grid and apply the color mapping.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] in color_map:
                output_grid[i, j] = color_map[output_grid[i, j]]

    return output_grid