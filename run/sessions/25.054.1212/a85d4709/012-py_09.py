"""
The input grid is transformed into an output grid of the same dimensions. The color of each row in the output grid is determined by the row index, cycling through the colors green (3), yellow (4), and red (2). Specifically:

1. The first row of the output grid is always green (3).
2. The second row of the output grid is always yellow (4).
3. The third row of the output grid is always red (2).
4. The process repeats if there are more than three rows, so row 4 would be green again, row 5 yellow, etc.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid based on row index to assign colors.

    Args:
        input_grid: A 2D numpy array representing the input grid.

    Returns:
        A 2D numpy array representing the output grid.
    """
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.zeros_like(input_grid)
    height = output_grid.shape[0]

    # Iterate over each row and set the color according to the row index.
    for i in range(height):
        if i % 3 == 0:
            output_grid[i, :] = 3  # Green
        elif i % 3 == 1:
            output_grid[i, :] = 4  # Yellow
        else:
            output_grid[i, :] = 2  # Red

    return output_grid