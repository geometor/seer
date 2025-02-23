"""
The transformation rule is a color substitution cipher. Each pixel's color in the input grid is replaced by a corresponding color in the output grid according to a fixed mapping.  The mapping is as follows:

- Blue (1) becomes Gray (5).
- Red (2) becomes Magenta (6).
- Green (3) becomes Yellow (4).
- Yellow (4) becomes Green (3).
- Gray (5) becomes Blue (1).
- Magenta (6) becomes Red (2).
- Azure (8) becomes Maroon (9).
- Maroon (9) becomes Azure (8).

The position of the pixel within the grid does not affect the transformation.  The output grid has the same dimensions as the input grid.
"""

import numpy as np

def transform(input_grid):
    """Applies a color substitution cipher to the input grid."""

    # Create the mapping dictionary.  This could be passed in as an argument,
    # but for clarity, it's defined here.
    value_mapping = {
        1: 5,
        2: 6,
        3: 4,
        4: 3,
        5: 1,
        6: 2,
        8: 9,
        9: 8,
    }

    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.zeros_like(input_grid)

    # Iterate through each pixel in the input grid.
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Get the input color.
            input_color = input_grid[i, j]

            # Get the corresponding output color from the mapping.
            # If a color isn't in the mapping, keep original.
            output_color = value_mapping.get(input_color, input_color)

            # Set the output pixel to the new color.
            output_grid[i, j] = output_color

    return output_grid