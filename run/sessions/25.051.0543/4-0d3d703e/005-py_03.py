"""
The transformation involves a consistent color mapping where each color in the input is replaced by a specific corresponding color in the output, maintaining the geometric structure. The mapping is as follows: 5 (gray) -> 1 (blue), 8 (azure) -> 9 (maroon), and 6 (magenta) -> 2 (red). The grid dimensions and object shapes/positions are preserved.
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
        5: 1,  # Gray to Blue
        8: 9,  # Azure to Maroon
        6: 2   # Magenta to Red
    }

    # Iterate through the input grid and apply the color transformation.
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            input_color = input_grid[i, j]
            # Use the color map to determine the output color, default to 0 if not found.
            output_color = color_map.get(input_color, input_color)  # Default to input color if not in color_map.
            output_grid[i, j] = output_color

    return output_grid