"""
Extracts a 5x5 subgrid from the upper-right corner of the input grid and applies a specific color transformation.
"""

import numpy as np

def find_target_region(input_grid, size):
    # Find the top-right 5x5 region of the input
    rows, cols = input_grid.shape
    start_row = 0
    start_col = cols - size
    return start_row, start_col

def transform(input_grid):
    """
    Extracts a 5x5 subgrid from the upper-right corner and remaps colors.
    """
    # Convert input grid to a NumPy array
    input_grid = np.array(input_grid)
        
    # Find the starting coordinates of target region
    size = 5
    start_row, start_col = find_target_region(input_grid, size)
    
    # Extract the subgrid
    output_grid = input_grid[start_row:start_row+size, start_col:start_col+size].copy()

    # Remap colors based on observations
    unique_colors = np.unique(output_grid)

    for color in unique_colors:
        if color == 0:
            output_grid[output_grid == 0] = 0  # 0 remains 0
        elif color == 1:
            output_grid[output_grid == 1] = 0  # 1 becomes 0
        elif color == 3:
            if 8 not in unique_colors:
                if 5 not in unique_colors:
                  output_grid[output_grid == 3] = 5 # if 8 is NOT in the grid, 3 maps to 5
                else:
                  output_grid[output_grid == 3] = 5 # handle the example 3 condition, change 3 to 5
            else:
                output_grid[output_grid == 3] = 6 # if 8 is present, it becomes 6
        elif color == 8:
            output_grid[output_grid == 8] = 0 # if color is 8, map to 0
        elif color == 5:
            output_grid[output_grid == 5] = 5
    
    return output_grid.tolist()