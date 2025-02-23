"""
The input grid consists of three horizontal lines, each with the color sequence 3, 1, 2. The output grid also has three horizontal lines. However, the colors have been transformed according to a specific mapping:

1.  Color 3 (green) in the input is replaced by color 4 (yellow) in the output.
2.  Color 1 (blue) in the input is replaced by color 5 (gray) in the output.
3.  Color 2 (red) in the input is replaced by color 6 (magenta) in the output.

The positions, sizes, and shapes of the objects (horizontal lines) remain unchanged; only the colors are altered based on the above mapping. There are no rotations, reflections or translations. The transformation consists on a color mapping.
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
        3: 4,  # green -> yellow
        1: 5,  # blue -> gray
        2: 6   # red -> magenta
    }

    # Iterate through the input grid and apply the color mapping.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] in color_map:
                output_grid[i, j] = color_map[output_grid[i, j]]

    return output_grid