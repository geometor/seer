"""
Extracts a 3x3 subgrid from the center of the input grid and applies a color transformation.
Gray (5) becomes Red (2).
Blue (1) becomes White (0).
"""

import numpy as np

def transform(input_grid):
    # Get input grid dimensions
    rows, cols = input_grid.shape

    # Define the subgrid size
    subgrid_size = 3

    # Calculate the starting column index for the center subgrid
    start_col = (cols - subgrid_size) // 2

    # Extract the 3x3 subgrid
    output_grid = input_grid[:, start_col:start_col + subgrid_size]

    # Apply color transformation: 5 (gray) -> 2 (red), 1 (blue) -> 0 (white)
    output_grid = np.where(output_grid == 5, 2, output_grid)
    output_grid = np.where(output_grid == 1, 0, output_grid)

    return output_grid