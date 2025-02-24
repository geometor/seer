"""
Divide the 9x9 input grid into nine 3x3 subgrids. For each subgrid, identify the color of the top-left pixel. 
Construct a 3x3 output grid and populate each cell with the color identified for the corresponding input subgrid.
"""

import numpy as np

def get_representative_color(subgrid):
    # Iterate through the subgrid to find the first non-white pixel.
    for row in range(subgrid.shape[0]):
        for col in range(subgrid.shape[1]):
            if subgrid[row, col] != 0:
                return subgrid[row, col]
    return 0  # Return white if the entire subgrid is white.

def transform(input_grid):
    # Initialize the output grid as a 3x3 array filled with zeros (white).
    output_grid = np.zeros((3, 3), dtype=int)

    # Iterate through the input grid, dividing it into 3x3 subgrids.
    for i in range(3):
        for j in range(3):
            # Extract the 3x3 subgrid.
            subgrid = input_grid[i*3:(i+1)*3, j*3:(j+1)*3]
            # Get the representative color of the subgrid.
            representative_color = get_representative_color(subgrid)
            # Set the corresponding pixel in the output grid.
            output_grid[i, j] = representative_color

    return output_grid