"""
Extracts the central 3x3 region of the input grid. 
Changes the color of the central pixel from gray (5) to red (2) if it is gray.
Preserves the surrounding pixels' colors.
"""

import numpy as np

def get_center(grid):
    # Calculate the center row and column indices
    center_row = grid.shape[0] // 2
    center_col = grid.shape[1] // 2
    return center_row, center_col

def extract_central_region(grid, center_row, center_col):
    # Extract the 3x3 subgrid centered at (center_row, center_col)

    row_start = center_row - 1
    row_end = center_row + 2
    col_start = center_col - 1
    col_end = center_col + 2
    
    return grid[row_start:row_end, col_start:col_end]

def transform(input_grid):
    # Convert input to numpy array
    input_grid = np.array(input_grid)

    # Get center row, col
    center_row, center_col = get_center(input_grid)

    # initialize output_grid by extracting 3x3 central region
    output_grid = extract_central_region(input_grid, center_row, center_col)

    # Change center pixel color from gray (5) to red (2)
    if output_grid[1, 1] == 5:
        output_grid[1, 1] = 2

    return output_grid.tolist()