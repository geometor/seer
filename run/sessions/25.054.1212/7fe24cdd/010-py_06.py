"""
The input grid is replicated and mirrored to create a 6x6 output grid, effectively forming four quadrants. Each quadrant of the output corresponds to a transformed version of the input grid:

1.  **Top-Left Quadrant:** An exact copy of the input grid.
2.  **Top-Right Quadrant:** A horizontally mirrored copy of the input grid (flipped across the vertical axis).
3.  **Bottom-Left Quadrant:** A vertically mirrored copy of the input grid (flipped across the horizontal axis).
4.  **Bottom-Right Quadrant:** A double-mirrored copy of the input grid (flipped across both the horizontal and vertical axes). This is equivalent to a 180-degree rotation.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a 6x6 array filled with zeros.
    output_grid = np.zeros((6, 6), dtype=int)

    # Get the dimensions of the input grid.
    rows, cols = input_grid.shape

    # Fill the top-left quadrant (direct copy).
    output_grid[:rows, :cols] = input_grid

    # Fill the top-right quadrant (horizontal mirror).
    output_grid[:rows, cols:] = np.fliplr(input_grid)

    # Fill the bottom-left quadrant (vertical mirror).
    output_grid[rows:, :cols] = np.flipud(input_grid)

    # Fill the bottom-right quadrant (double mirror/rotation).
    output_grid[rows:, cols:] = np.rot90(input_grid, 2)  # 180-degree rotation

    return output_grid