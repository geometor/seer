"""
Transforms a 3x2 input grid into a 9x4 output grid by rotating a 2x2 subgrid and tiling it.
"""

import numpy as np

def rotate_subgrid(subgrid):
    """Rotates a 2x2 subgrid 90 degrees clockwise."""
    return np.rot90(subgrid, k=-1)

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    input_grid = np.array(input_grid)
    # 1. Define Sub-Grid: Extract the top-left 2x2 region.
    subgrid = input_grid[:2, :2]

    # 2. Transform 2x2: Rotate the sub-grid 90 degrees clockwise.
    rotated_subgrid = rotate_subgrid(subgrid)

    # 3. Output Dimensions and initialization
    output_rows = input_grid.shape[0] * 3
    output_cols = input_grid.shape[1] * 2
    output_grid = np.zeros((output_rows, output_cols), dtype=int)

    # 4. Tile and Replicate: Tile the transformed 2x2 sub-grid.
    for i in range(output_rows):
        for j in range(output_cols):
            output_grid[i, j] = rotated_subgrid[i % 2, j % 2]

    return output_grid.tolist()