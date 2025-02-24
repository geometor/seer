"""
The input grid is replicated to form a larger grid. A central area of the expanded grid is filled with zeros (white color).
"""

import numpy as np

def transform(input_grid):
    # Create a 3x3 replication of the input grid
    input_array = np.array(input_grid)
    tiled_array = np.tile(input_array, (3, 3))

    # Get dimensions of the tiled array
    rows, cols = tiled_array.shape

    # Calculate the start and end indices for the central 3x3 area to be zeroed
    center_start_row = (rows - 3) // 2
    center_end_row = center_start_row + 3
    center_start_col = (cols - 3) // 2
    center_end_col = center_start_col + 3

    # Set the central 3x3 area to 0
    tiled_array[center_start_row:center_end_row, center_start_col:center_end_col] = 0
    
    output_grid = tiled_array.tolist() #convert back to list of lists
    return output_grid