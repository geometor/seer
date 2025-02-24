"""
Extracts the central 3x3 subgrid from the input grid.
"""

import numpy as np

def get_center(grid):
    """Calculates the center coordinates of a grid."""
    rows, cols = grid.shape
    center_row = rows // 2
    center_col = cols // 2
    return center_row, center_col

def extract_3x3(grid, center_row, center_col):
    """Extracts a 3x3 subgrid centered at the given coordinates."""
    return grid[center_row-1:center_row+2, center_col-1:center_col+2]

def transform(input_grid):
    """Extracts the central 3x3 subgrid."""
    # Convert input to numpy array
    input_grid = np.array(input_grid)

    # Get the center coordinates
    center_row, center_col = get_center(input_grid)

    # Extract the 3x3 subgrid
    output_grid = extract_3x3(input_grid, center_row, center_col)

    return output_grid.tolist()