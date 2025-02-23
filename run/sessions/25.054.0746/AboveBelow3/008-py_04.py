"""
The transformation rule is a downward shift of only the top red region by two rows, leaving the other colored regions untouched.
"""

import numpy as np

def find_top_red_region(grid):
    """Finds the top red region in the grid."""
    rows, cols = grid.shape
    top_red_region = []
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 2:
                top_red_region.append((r, c))
        if any(grid[r,c] == 6 for c in range(cols)): #stop after encounter magenta object
            break
    return top_red_region

def find_magenta_region(grid):
     # find magenta object
    rows, cols = grid.shape
    magenta_region = []
    for r in range(rows):
        for c in range(cols):
            if grid[r,c] == 6:
                magenta_region.append((r,c))
    return magenta_region

def find_bottom_red_region(grid):
    # Find bottom red region.
    rows, cols = grid.shape
    bottom_red_region = []

    for r in range(rows):
        for c in range(cols):
            if grid[r,c] == 2:
                if not any(grid[row,c] == 2 for row in range(0,r)):
                    bottom_red_region.append((r,c))
    return bottom_red_region
    

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find the top red region
    top_red_region = find_top_red_region(input_grid)
    
    #Find magenta region
    magenta_region = find_magenta_region(input_grid)

    # find the bottom red regions
    bottom_red_region = find_bottom_red_region(input_grid)

    # Clear the original top red region in the output grid
    for r, c in top_red_region:
        output_grid[r, c] = 0

    # Shift the top red region down by two rows
    for r, c in top_red_region:
        new_r = r + 2
        if new_r < rows:  # Ensure we don't go out of bounds
            output_grid[new_r, c] = 2
            
    return output_grid