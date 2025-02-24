"""
Transforms a 3x3 input grid by changing blue pixels to red, while keeping white pixels unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.

    Args:
        input_grid: A 3x3 numpy array representing the input grid.

    Returns:
        A 3x3 numpy array representing the transformed output grid.
    """
    # initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Iterate through each pixel
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # change output pixels: If the pixel is blue (1), change it to red (2)
            if output_grid[i, j] == 1:
                output_grid[i, j] = 2
            # Otherwise (if it's white/0), it remains unchanged.

    return output_grid