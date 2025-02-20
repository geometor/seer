"""
The transformation involves a consistent color mapping where each color in the input is replaced by a specific corresponding color in the output, maintaining the geometric structure. The mapping is as follows: 3 (green) -> 4 (yellow), 1 (blue) -> 5 (gray), and 2 (red) -> 6 (magenta). The grid dimensions and object shapes/positions are preserved.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid to the output grid based on a color mapping rule.
    """
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.zeros_like(input_grid)

    # Define the color mapping.
    color_map = {
        3: 4,  # Green to Yellow
        1: 5,  # Blue to Gray
        2: 6   # Red to Magenta
    }

    # Iterate through the input grid and apply the color transformation.
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            input_color = input_grid[i, j]
            # Use the color map to determine the output color, default to 0 if not found
            output_color = color_map.get(input_color, input_color + 3)  # Use the input color + 3 for mapping, else default to input color
            output_grid[i, j] = output_color

    return output_grid