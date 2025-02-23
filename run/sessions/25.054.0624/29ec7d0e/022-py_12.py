"""
The transformation rule is to remove all pixels of color white (value 0) from the input grid, *but maintain the original grid dimensions*. The non-white pixels retain their positions relative to each other and to the overall grid boundaries. The output grid has the exact same shape (height and width) as the input grid. Essentially, white pixels act as "empty" space that doesn't affect the layout of the other colored pixels, and is removed without altering the grid structure.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Find the indices of all white (0) pixels.
    white_indices = np.where(output_grid == 0)

    # Set all white pixels to -1 to visually remove them, while keeping grid dimensions.
    output_grid[white_indices] = -1  # Use -1 as a placeholder

    return output_grid