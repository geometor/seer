"""
The transformation involves a direct color substitution, following the rule: 5 -> 1, 8 -> 9, and 6 -> 2. The spatial arrangement of cells remains constant; only the colors change.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by replacing colors based on a predefined mapping.

    Args:
        input_grid (numpy.ndarray): The input grid as a 2D numpy array.

    Returns:
        numpy.ndarray: The transformed output grid.
    """
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Define the color mapping
    color_map = {
        5: 1,  # Gray to Blue
        8: 9,  # Azure to Maroon
        6: 2   # Magenta to Red
    }

    # Iterate through the input grid and apply the color mapping
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] in color_map:
                output_grid[i, j] = color_map[output_grid[i, j]]

    return output_grid