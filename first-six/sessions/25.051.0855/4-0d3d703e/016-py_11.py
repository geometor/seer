"""
The transformation rule is a one-to-one color mapping applied to each cell in the grid. The mapping is:

- 3 (green) -> 4 (yellow)
- 1 (blue) -> 5 (gray)
- 2 (red) -> 6 (magenta)
- 8 (azure) -> 9 (maroon)
- 5 (gray) -> 1 (blue)
- 6 (magenta) -> 2 (red)
- 9 (maroon) -> 8 (azure)
- 4 (yellow) -> 3 (green)
- 0 (white) -> 0 (white)

The structure and positions of all cells remain unchanged; only the colors are updated.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified color mapping rule.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Define the color mapping dictionary.
    color_map = {
        3: 4,
        1: 5,
        2: 6,
        8: 9,
        5: 1,
        6: 2,
        9: 8,
        4: 3,
        0: 0
    }

    # Iterate through each cell of the grid.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Get the input color.
            input_color = output_grid[i, j]
            # Apply the color mapping using the dictionary's get() method.
            # If the input color is not in the map, keep original color.
            output_grid[i, j] = color_map.get(input_color, input_color)

    # Return the transformed grid.
    return output_grid