"""
The transformation preserves everything outside a central diamond shape.  Inside the diamond,
all pixels of color 4 are changed to color 2.
"""

import numpy as np

def find_diamond_center(grid):
    # Find the center of the grid
    center_row, center_col = grid.shape[0] // 2, grid.shape[1] // 2
    return center_row, center_col

def is_inside_diamond(row, col, center_row, center_col, size):
    # Determine if a given cell is within the diamond
    dist_row = abs(row - center_row)
    dist_col = abs(col - center_col)
    return dist_row + dist_col <= size

def get_diamond_size(grid):
    # Find diamond center
    center_row, center_col = find_diamond_center(grid)

    # expand outward to estimate the size/radius
    max_size = min(center_row, center_col)
    
    return max_size

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    
    grid = input_grid
    # Find diamond center
    center_row, center_col = find_diamond_center(grid)

    # expand outward to estimate the size/radius
    size = get_diamond_size(grid)

    # Iterate through each cell of the grid
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            # Check if the cell is inside the diamond
            if is_inside_diamond(row, col, center_row, center_col, size):
                # Apply color transformations inside the diamond
                if grid[row, col] == 4:
                    output_grid[row, col] = 2

    return output_grid