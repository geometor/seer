"""
Extracts the central 3x3 subgrid from the input grid.
Transforms Gray (5) to Red (2) in the entire subgrid.
Transforms Blue (1) to White (0) only on the center row of the subgrid.
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

    # Apply color transformation: 5 (gray) -> 2 (red) for the whole subgrid
    output_grid = np.where(output_grid == 5, 2, output_grid)
    
    # Apply color transformation: 1 (blue) -> 0 (white) for the center row only
    output_grid[1, :] = np.where(output_grid[1, :] == 1, 0, output_grid[1, :])

    return output_grid